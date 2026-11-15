import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

MODEL_NAME = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.8-flash"
)

SYSTEM_PROMPT = """
You are the Game Master of an interactive escape room.

GAME TITLE: The Locked Library.

STORY:
The player wakes up inside a locked library.

The room contains:
1. A desk
2. A bookshelf
3. A painting
4. A locked drawer
5. An exit door

GAME OBJECTIVES:
- Investigate objects.
- Discover clues.
- Solve three puzzles.
- Collect useful items.
- Unlock the exit.

PUZZLE DESIGN:

Puzzle 1:
The bookshelf contains four marked books.
Their numbers, in the correct order, are 2, 7, 4, 1.
The drawer code is 2741.

Puzzle 2:
Opening the drawer reveals a brass key.

Puzzle 3:
The painting reveals four symbols:
Moon = 1
Sun = 9
Star = 3
Key = 6

The final door code is 1936.

RULES:
- Respond like an engaging adventure game.
- Describe the environment dramatically.
- Respond to the player's actions.
- Give hints when the player is struggling.
- Do not immediately reveal puzzle solutions.
- Keep track of the conversation.
- Do not invent new rooms or objects.
- Do not claim the player has escaped unless the
  required puzzles have been completed.

IMPORTANT:
This is Version 1. Python-based action validation
will be introduced in Version 2.
"""


import time


def generate_response(history, action):

    if not API_KEY:
        return "Gemini API key is missing. Check your .env file."

    client = genai.Client(api_key=API_KEY)

    conversation = SYSTEM_PROMPT + "\n\n"

    for message in history:
        conversation += (
            f"{message['role'].upper()}: "
            f"{message['content']}\n"
        )

    conversation += f"PLAYER: {action}\n"
    conversation += "GAME MASTER:"

    # Retry temporarily unavailable requests
    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=conversation
            )

            if response.text:
                return response.text

            return "The Game Master is thinking. Try again."

        except Exception as error:

            error_message = str(error)

            if attempt < 2 and (
                "503" in error_message
                or "429" in error_message
                or "UNAVAILABLE" in error_message
            ):

                time.sleep(2 ** attempt)
                continue

            return f"Game Master error: {error_message}"

    return "The Game Master is temporarily unavailable."