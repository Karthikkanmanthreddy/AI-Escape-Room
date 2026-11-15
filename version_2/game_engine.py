from validation import (
    investigate_object,
    solve_drawer_puzzle,
    inspect_painting,
    unlock_exit
)


def process_action(state, action):

    """
    Processes player actions using Python game logic.
    """

    action = action.lower().strip()

    # Investigate desk
    if action == "desk":

        success, message = investigate_object(
            state, "desk"
        )

        return message + (
            "\n\nYou notice a dusty note on the desk. "
            "It mentions four marked books."
        )

    # Investigate bookshelf
    elif action == "bookshelf":

        success, message = investigate_object(
            state, "bookshelf"
        )

        if success:

            return (
                "You discover four marked books:\n\n"
                "📕 Crimson: 2\n"
                "📘 Navy Blue: 7\n"
                "📗 Forest Green: 4\n"
                "📓 Charcoal Black: 1\n\n"
                "Enter the four-digit combination "
                "to unlock the drawer."
            )

        return message

    # Investigate drawer
    elif action == "drawer":

        success, message = investigate_object(
            state, "drawer"
        )

        if state["drawer_unlocked"]:

            return "The drawer is already unlocked. You have the Brass Key."

        return (
            "The drawer is secured by a four-digit combination lock. "
            "Investigate the bookshelf to find the clue."
        )

    # Investigate painting
    elif action == "painting":

        success, message = investigate_object(
            state, "painting"
        )

        success, message = inspect_painting(state)

        return message

    # Investigate exit door
    elif action == "door":

        success, message = investigate_object(
            state, "door"
        )

        return (
            "The exit door has a four-digit security lock "
            "and a brass keyhole. You must solve the puzzles "
            "before escaping."
        )

    return "Unknown action. Please select a valid object."


def submit_puzzle(state, puzzle, answer):

    """
    Processes puzzle answers through Python validation.
    """

    if puzzle == "drawer":

        success, message = solve_drawer_puzzle(
            state, answer
        )

    elif puzzle == "exit":

        success, message = unlock_exit(
            state, answer
        )

    else:

        return False, "Unknown puzzle."

    return success, message