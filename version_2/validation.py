from game_state import (
    explore_object,
    add_inventory_item,
    has_item
)


DRAWER_CODE = "2741"
EXIT_CODE = "1936"


def investigate_object(state, object_name):

    """
    Validates whether an object exists
    in the library.
    """

    valid_objects = [
        "desk",
        "bookshelf",
        "painting",
        "drawer",
        "door"
    ]

    object_name = object_name.lower().strip()

    if object_name not in valid_objects:

        return False, "This object does not exist."

    explore_object(state, object_name)

    return True, f"You investigate the {object_name}."


def solve_drawer_puzzle(state, answer):

    """
    Validates the four-digit drawer combination.
    """

    if "bookshelf" not in state["explored_objects"]:

        return False, "Investigate the bookshelf first."

    if state["drawer_unlocked"]:

        return True, "The drawer is already unlocked."

    if str(answer).strip() == DRAWER_CODE:

        state["drawer_unlocked"] = True
        state["bookshelf_clue_found"] = True

        add_inventory_item(state, "Brass Key")

        return True, (
            "Correct! The drawer opens. "
            "You collected the Brass Key."
        )

    state["failed_attempts"] += 1

    return False, "Incorrect combination. Try again."


def inspect_painting(state):

    """
    Validates access to the painting clue.
    """

    if not has_item(state, "Brass Key"):

        return False, "You need the Brass Key first."

    state["painting_clue_found"] = True

    return True, (
        "You discover the hidden sequence: "
        "Moon=1, Sun=9, Star=3, Key=6."
    )


def unlock_exit(state, answer):

    """
    Validates the final escape condition.
    """

    if not state["drawer_unlocked"]:

        return False, "You must unlock the drawer first."

    if not has_item(state, "Brass Key"):

        return False, "You need the Brass Key."

    if not state["painting_clue_found"]:

        return False, "You must investigate the painting."

    if str(answer).strip() != EXIT_CODE:

        state["failed_attempts"] += 1

        return False, "Incorrect exit code. Access denied."

    state["exit_unlocked"] = True
    state["game_completed"] = True

    return True, (
        "CONGRATULATIONS! You escaped the Locked Library!"
    )