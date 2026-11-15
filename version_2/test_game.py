from game_state import create_initial_state
from validation import (
    investigate_object,
    solve_drawer_puzzle,
    inspect_painting,
    unlock_exit
)


state = create_initial_state()

print("\n--- AI ESCAPE ROOM TEST ---\n")


# Test 1: Try escaping immediately

success, message = unlock_exit(state, "1936")

print("Test 1:", message)


# Test 2: Investigate bookshelf

success, message = investigate_object(
    state, "bookshelf"
)

print("\nTest 2:", message)


# Test 3: Unlock drawer

success, message = solve_drawer_puzzle(
    state, "2741"
)

print("\nTest 3:", message)


# Test 4: Investigate painting

success, message = inspect_painting(state)

print("\nTest 4:", message)


# Test 5: Escape

success, message = unlock_exit(
    state, "1936"
)

print("\nTest 5:", message)


print("\nFinal Game State:")
print(state)