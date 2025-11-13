import logging
import random
import sys
import time

from files2dict import read
from output_formatting import save_assignment_prompt, interactive_reveal


# make sure there are no people who are only gifters ox only gift recipients.
def ensure_key_domain_equals_value_domain(d: dict[str, list[str]]) -> bool:
    gifters = set(d.keys())
    recipients = {x for l in d.values() for x in l}

    only_gifters = gifters - recipients
    only_recipients = recipients - gifters

    if only_gifters:
        logging.error(f"People who are only gifters: {only_gifters}")
    if only_recipients:
        logging.error(f"People who are only recipients: {only_recipients}")
    if not (only_gifters or only_recipients):
        logging.info("Such a great group! There is no person who is either only gifter or only recipient!")

    return not (only_gifters or only_recipients)


def attempt_assignment(d: dict[str, list[str]]) -> dict[str, str] | None:
    # sort by smallest recipient list size to handle most constrained people first
    sorted_gifters = sorted(d.keys(), key=lambda person: len(d[person]))

    res = {}
    assigned_recipients = set()

    for gifter in sorted_gifters:
        # filter out people who have already been assigned as recipients
        available = [person for person in d[gifter] if person not in assigned_recipients]

        if not available:
            return None

        recipient = random.choice(available)
        res[gifter] = recipient
        assigned_recipients.add(recipient)

    return res


def find_assignment(d: dict[str, list[str]], max_seconds: int = 100) -> dict[str, str] | None:
    start_time = time.time()
    attempts = 0

    while time.time() - start_time < max_seconds:
        attempts += 1
        result = attempt_assignment(d)
        if result is not None:
            elapsed = time.time() - start_time
            logging.info(f"Assignment found!")
            return result

    elapsed = time.time() - start_time
    logging.error(f"Timeout after {attempts} attempts in {elapsed:.2f} seconds")
    logging.error("Either assignment is not possible or the program needs to be rerun (rerunning might actually help, as the program is pseudo-random).")
    return None


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    if len(sys.argv) != 2:
        logging.error(
            "You must input a single file(.csv, .xlsx, or .json). Run the script like: python main.py INPUT_FILE_NAME.(csv|xlsx|json)")
        sys.exit(1)

    d = read(sys.argv[1])
    if d == {}:
        logging.critical("Supported file extensions are: .csv, .xlsx and .json. Please input one of those files.")
        sys.exit(1)

    if not ensure_key_domain_equals_value_domain(d):
        logging.error("Please ensure there are no people who are only gifters or only recipients.")
        sys.exit(1)

    assignment = find_assignment(d, max_seconds=100)

    if assignment:
        save_assignment_prompt(assignment)
        interactive_reveal(assignment)
    else:
        logging.critical("Failed to find a valid Secret Santa assignment")
        sys.exit(1)