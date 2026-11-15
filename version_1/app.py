import streamlit as st
from game_master import generate_response

st.set_page_config(
    page_title="The Locked Library",
    page_icon="🔐",
    layout="wide"
)

# Game styling
st.markdown("""
<style>
.stApp {
    background-color: #101522;
    color: white;
}

h1, h2, h3 {
    color: #e6c27a;
}

div.stButton > button {
    background-color: #26344c;
    color: white;
    border: 1px solid #c49b55;
    border-radius: 10px;
    height: 65px;
    width: 100%;
}

div.stButton > button:hover {
    background-color: #405575;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# Initialize game
if "messages" not in st.session_state:
    st.session_state.messages = []

if "explored" not in st.session_state:
    st.session_state.explored = []

if "inventory" not in st.session_state:
    st.session_state.inventory = []


# Game Master function
def ask_game_master(action):

    response = generate_response(
        st.session_state.messages,
        action
    )

    st.session_state.messages.append({
        "role": "user",
        "content": action
    })

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })


# Header
st.title("🔐 THE LOCKED LIBRARY")

st.markdown(
    "### An AI-Powered Escape Room Adventure"
)

st.markdown("""
You wake up inside an abandoned library.

The entrance is locked. Five mysterious objects surround you.

Your mission is to investigate the library, discover hidden clues,
solve puzzles and escape.
""")

st.divider()


# Game status
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Objects Explored", len(st.session_state.explored))

with col2:
    st.metric("Items Collected", len(st.session_state.inventory))

with col3:
    st.metric("Mission", "Escape the Library")


st.divider()


# Library environment
st.subheader("🏛️ Explore Your Environment")

objects = [
    ("🪑 Desk", "desk"),
    ("📚 Bookshelf", "bookshelf"),
    ("🖼️ Painting", "painting"),
    ("🗄️ Locked Drawer", "drawer"),
    ("🚪 Exit Door", "door")
]

columns = st.columns(5)

for index, (label, obj) in enumerate(objects):

    with columns[index]:

        if st.button(label, key=obj):

            if obj not in st.session_state.explored:
                st.session_state.explored.append(obj)

            ask_game_master(
                f"I want to investigate the {obj}."
            )

            st.rerun()


st.divider()


# Player inventory
st.subheader("🎒 Player Inventory")

if st.session_state.inventory:
    st.write(st.session_state.inventory)
else:
    st.info("Your inventory is currently empty.")


# Game conversation
st.subheader("🤖 AI Game Master")

if not st.session_state.messages:

    st.info(
        "Welcome, explorer! Choose an object above "
        "or describe what you want to investigate."
    )

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# Natural language interaction
player_action = st.chat_input(
    "What would you like to do next?"
)

if player_action:

    ask_game_master(player_action)

    st.rerun()


# Restart
if st.sidebar.button("🔄 Restart Game"):

    st.session_state.messages = []
    st.session_state.explored = []
    st.session_state.inventory = []

    st.rerun()


st.sidebar.title("📜 Mission Instructions")

st.sidebar.write("""
1. Explore the five objects.
2. Investigate hidden clues.
3. Solve the puzzles.
4. Collect useful items.
5. Unlock the exit door.
6. Escape the library!

Good luck, explorer!
""")