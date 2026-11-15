import streamlit as st
import os

from dotenv import load_dotenv
from google import genai

from game_state import create_initial_state, get_game_progress
from game_engine import process_action, submit_puzzle


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

load_dotenv()

st.set_page_config(
    page_title="The Locked Library | Version 2",
    page_icon="🔐",
    layout="wide"
)

API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

MODEL_NAME = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.8-flash"
)


# --------------------------------------------------
# GAME DESIGN
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #101522;
    color: #ffffff;
}

h1, h2, h3 {
    color: #e6c27a;
}

div.stButton > button {
    background-color: #26344c;
    color: white;
    border: 1px solid #c49b55;
    border-radius: 12px;
    height: 65px;
    width: 100%;
    font-size: 16px;
}

div.stButton > button:hover {
    background-color: #405575;
    color: white;
}

.success-box {
    background-color: #173d32;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #38a169;
}

.game-box {
    background-color: #1c2638;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #c49b55;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# INITIALIZE GAME
# --------------------------------------------------

if "game_state" not in st.session_state:

    st.session_state.game_state = create_initial_state()

if "game_messages" not in st.session_state:

    st.session_state.game_messages = [
        {
            "role": "assistant",
            "content": (
                "Welcome, explorer! You are trapped inside "
                "the Locked Library. Investigate your "
                "surroundings and find a way to escape."
            )
        }
    ]


state = st.session_state.game_state


# --------------------------------------------------
# AI STORYTELLER
# --------------------------------------------------

def ai_storyteller(event):

    """
    Gemini provides storytelling only.
    Python remains responsible for game validation.
    """

    if not API_KEY:

        return event

    try:

        client = genai.Client(api_key=API_KEY)

        prompt = f"""
        You are the storyteller of an escape room game.

        Describe the following validated game event
        in an immersive adventure style.

        IMPORTANT:
        - Do not change the game outcome.
        - Do not invent collected items.
        - Do not invent puzzle solutions.
        - Do not claim the player escaped unless
          the event explicitly confirms escape.
        - Keep the response under 120 words.

        VALIDATED GAME EVENT:
        {event}
        """

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return response.text or event

    except Exception:

        return event


# --------------------------------------------------
# GAME ACTION
# --------------------------------------------------

def handle_object(object_name):

    result = process_action(
        state,
        object_name
    )

    st.session_state.game_messages.append({
        "role": "assistant",
        "content": ai_storyteller(result)
    })


def handle_puzzle(puzzle, answer):

    success, message = submit_puzzle(
        state,
        puzzle,
        answer
    )

    st.session_state.game_messages.append({
        "role": "assistant",
        "content": ai_storyteller(message)
    })


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🔐 THE LOCKED LIBRARY")

st.subheader(
    "Version 2 — Intelligent AI Escape Room"
)

st.markdown("""
You awaken inside an ancient library.

The entrance is locked. Hidden clues are scattered
throughout the room.

Investigate objects, solve puzzles, collect items
and escape before you are trapped forever.
""")

st.divider()


# --------------------------------------------------
# GAME PROGRESS
# --------------------------------------------------

progress = get_game_progress(state)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Puzzles Completed", f"{progress}/4")

with col2:
    st.metric(
        "Objects Explored",
        len(state["explored_objects"])
    )

with col3:
    st.metric(
        "Items Collected",
        len(state["inventory"])
    )

with col4:
    st.metric(
        "Game Status",
        "Completed" if state["game_completed"]
        else "In Progress"
    )

st.progress(progress / 4)

st.divider()


# --------------------------------------------------
# ENVIRONMENT
# --------------------------------------------------

st.header("🏛️ Explore Your Environment")

objects = [
    ("🪑 Desk", "desk"),
    ("📚 Bookshelf", "bookshelf"),
    ("🖼️ Painting", "painting"),
    ("🗄️ Locked Drawer", "drawer"),
    ("🚪 Exit Door", "door")
]

columns = st.columns(5)

for index, (label, object_name) in enumerate(objects):

    with columns[index]:

        if st.button(
            label,
            key=f"object_{object_name}",
            disabled=state["game_completed"]
        ):

            handle_object(object_name)

            st.rerun()


st.divider()


# --------------------------------------------------
# PUZZLE 1 – DRAWER
# --------------------------------------------------

st.header("🔢 Puzzle Challenges")

if "bookshelf" in state["explored_objects"]:

    if not state["drawer_unlocked"]:

        st.subheader("Puzzle 1: The Locked Drawer")

        st.write(
            "Enter the four-digit combination "
            "discovered on the bookshelf."
        )

        with st.form("drawer_form"):

            drawer_code = st.text_input(
                "Drawer Combination",
                max_chars=4,
                placeholder="Enter four digits"
            )

            submit_drawer = st.form_submit_button(
                "🔓 Unlock Drawer"
            )

            if submit_drawer:

                if drawer_code:

                    handle_puzzle(
                        "drawer",
                        drawer_code
                    )

                    st.rerun()

                else:

                    st.warning("Enter a combination first.")

    else:

        st.success(
            "✅ Puzzle 1 completed! Drawer unlocked."
        )


# --------------------------------------------------
# PUZZLE 2 – PAINTING
# --------------------------------------------------

if state["drawer_unlocked"]:

    st.subheader("Puzzle 2: The Mysterious Painting")

    if not state["painting_clue_found"]:

        st.info(
            "Investigate the painting to discover "
            "the hidden symbols."
        )

    else:

        st.success(
            "✅ Painting investigated. "
            "Final sequence discovered: 1936."
        )


# --------------------------------------------------
# PUZZLE 3 – EXIT
# --------------------------------------------------

if state["painting_clue_found"]:

    st.subheader("Puzzle 3: Escape the Library")

    st.write(
        "Enter the final four-digit code and use "
        "the brass key to unlock the exit."
    )

    with st.form("exit_form"):

        exit_code = st.text_input(
            "Final Exit Code",
            max_chars=4,
            placeholder="Enter final code"
        )

        submit_exit = st.form_submit_button(
            "🚪 Escape the Library"
        )

        if submit_exit:

            if exit_code:

                handle_puzzle(
                    "exit",
                    exit_code
                )

                st.rerun()

            else:

                st.warning("Enter the exit code.")


st.divider()


# --------------------------------------------------
# INVENTORY
# --------------------------------------------------

st.header("🎒 Player Inventory")

if state["inventory"]:

    for item in state["inventory"]:

        st.success(f"🗝️ {item}")

else:

    st.info("Your inventory is currently empty.")


st.divider()


# --------------------------------------------------
# AI GAME MASTER
# --------------------------------------------------

st.header("🤖 AI Game Master")

for message in st.session_state.game_messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# --------------------------------------------------
# VICTORY SCREEN
# --------------------------------------------------

if state["game_completed"]:

    st.balloons()

    st.markdown("""
    <div class="success-box">

    <h1 style="text-align:center;">
    🏆 YOU ESCAPED!
    </h1>

    <h3 style="text-align:center;">
    Congratulations, Explorer!
    </h3>

    <p style="text-align:center;">
    You solved the puzzles, collected the brass key
    and successfully escaped The Locked Library.
    </p>

    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# RESTART
# --------------------------------------------------

st.sidebar.title("📜 Mission Instructions")

st.sidebar.write("""
1. Investigate the desk.
2. Explore the bookshelf.
3. Discover the drawer combination.
4. Collect the brass key.
5. Investigate the painting.
6. Discover the final code.
7. Escape the library.
""")

st.sidebar.divider()

if st.sidebar.button("🔄 Restart Game"):

    st.session_state.game_state = create_initial_state()

    st.session_state.game_messages = [
        {
            "role": "assistant",
            "content": "A new adventure begins. Good luck, explorer!"
        }
    ]

    st.rerun()