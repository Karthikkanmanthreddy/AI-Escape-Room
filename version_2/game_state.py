def create_initial_state():

    """
    Creates the initial state of the escape room.
    """

    return {

        # Game progress
        "game_started": True,
        "game_completed": False,

        # Objects explored
        "explored_objects": [],

        # Puzzle progress
        "bookshelf_clue_found": False,
        "drawer_unlocked": False,
        "painting_clue_found": False,

        # Inventory
        "inventory": [],

        # Security and validation
        "failed_attempts": 0,

        # Final escape status
        "exit_unlocked": False,

    }


def reset_game_state():

    """
    Resets the game to its original state.
    """

    return create_initial_state()


def explore_object(state, object_name):

    """
    Records an object explored by the player.
    """

    if object_name not in state["explored_objects"]:

        state["explored_objects"].append(object_name)

    return state


def add_inventory_item(state, item):

    """
    Adds an item to the player's inventory.
    """

    if item not in state["inventory"]:

        state["inventory"].append(item)

    return state


def has_item(state, item):

    """
    Checks whether the player possesses an item.
    """

    return item in state["inventory"]


def get_game_progress(state):

    """
    Returns the number of completed objectives.
    """

    completed = 0

    if state["bookshelf_clue_found"]:
        completed += 1

    if state["drawer_unlocked"]:
        completed += 1

    if state["painting_clue_found"]:
        completed += 1

    if state["exit_unlocked"]:
        completed += 1

    return completed