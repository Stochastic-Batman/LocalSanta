import json
import logging
import os
import time


def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def save_assignment_prompt(assignment: dict[str, str]) -> None:
    response = input("Do you want to save the assignment as a JSON file? (yes/y): ").strip().lower()

    if response == "yes" or response == "y":
        filename = "WARNING_secret_santa_assignments.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(assignment, f, indent=4, ensure_ascii=False)
        logging.info(f"Assignment saved to {filename}")
    else:
        logging.info("Assignment not saved")


def display_remaining_people(people: list[str]) -> None:
    logging.info("=" * 50)
    logging.info("REMAINING PEOPLE")
    logging.info("=" * 50)
    for person in sorted(people):
        logging.info(f" ჻ {person}")
    logging.info("=" * 50)


def interactive_reveal(assignment: dict[str, str], screen_time: int = 5) -> None:
    remaining = list(assignment.keys())

    while remaining:
        clear_screen()
        display_remaining_people(remaining)

        name = input("\nWho are you? ").strip()

        if name not in assignment:
            logging.info(f"Name '{name}' not found in the assignment list. Please try again.")
            time.sleep(screen_time)
            continue

        if name not in remaining:
            logging.info(f"{name}, you have already seen your assignment!")
            time.sleep(screen_time)
            continue

        clear_screen()
        logging.info("=" * 50)
        logging.info("YOUR SECRET SANTA ASSIGNMENT")
        logging.info("=" * 50)
        logging.info(f"{name}, you shall give a gift to: {assignment[name]}\n")
        logging.info("=" * 50)
        logging.info(f"This message will disappear in {screen_time} seconds...")

        time.sleep(screen_time)
        remaining.remove(name)

    clear_screen()
    logging.info("=" * 50)
    logging.info("ALL ASSIGNMENTS REVEALED!")
    logging.info("=" * 50)
    logging.info("Everyone has seen their Secret Santa assignment.")
    logging.info("Happy gifting!")
    logging.info("=" * 50)


if __name__ == "__main__":
    logging.warning("You should not be running this file. Instead, run: python main.py INPUT_FILE_NAME.(csv|xlsx|json)")