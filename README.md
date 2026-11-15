# 🔐 AI Escape Room – The Locked Library

An interactive AI-powered escape room game developed using Python, Streamlit and Google Gemini.

Players explore an abandoned library, discover hidden clues, solve puzzles, collect items and escape through an interactive gaming experience.

## 🎮 Project Overview

The project demonstrates how Generative AI and traditional Python programming can work together to develop an interactive AI application.

The application is developed in two versions.

### Version 1 – AI-Powered Game Master

- Gemini-powered storytelling.
- Interactive library objects.
- Natural-language player interactions.
- AI-generated clues and puzzle progression.
- Conversational game experience.

### Version 2 – Controlled AI Escape Room

- Python-based game-state management.
- Independent puzzle validation.
- Inventory management.
- Controlled game progression.
- Gemini-powered storytelling.
- Validated victory conditions.

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google Gen AI SDK
- Python-dotenv
- Git and GitHub

## 🏛️ Game Story

The player wakes up inside an abandoned library.

Five objects are available for investigation:

1. Desk
2. Bookshelf
3. Painting
4. Locked Drawer
5. Exit Door

The player must discover hidden clues, solve puzzles, collect the brass key and unlock the final exit.

## 🔢 Puzzle Structure

| Puzzle | Challenge | Solution |
|---|---|---|
| Puzzle 1 | Bookshelf combination | 2741 |
| Puzzle 2 | Collect the brass key | Brass Key |
| Puzzle 3 | Painting symbol sequence | 1936 |

## 📂 Project Structure

```text
AI-Escape-Room/
│
├── version_1/
│   ├── app.py
│   └── game_master.py
│
├── version_2/
│   ├── app.py
│   ├── game_engine.py
│   ├── game_state.py
│   ├── validation.py
│   └── test_game.py
│
├── documentation/
├── screenshots/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Karthikkanmanthreddy/AI-Escape-Room.git
```

### 2. Navigate to the project

```bash
cd AI-Escape-Room
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Gemini API

Create a `.env` file in the project root.

Add:

```text
GEMINI_API_KEY=your_api_key
GEMINI_MODEL=your_supported_gemini_model
```

Never upload your actual API key to GitHub.

### 7. Run Version 1

```bash
streamlit run version_1/app.py
```

### 8. Run Version 2

```bash
streamlit run version_2/app.py
```

## 🧪 Testing

Version 2 includes independent Python validation tests covering:

- Preventing premature escape.
- Investigating the bookshelf.
- Validating the drawer combination.
- Investigating the painting.
- Validating the final escape code.

## 🚀 Development Improvements

Version 1 relies heavily on Gemini's conversational context.

Version 2 introduces structured Python game-state management and independent validation to improve reliability and prevent the AI from bypassing game rules.

## 👨‍💻 Author

Karthik

Master's in Data Science  
University of Europe for Applied Sciences, Germany

## 📌 Project Status

- Version 1: Implemented and tested.
- Version 2: Implemented with Python-based
  game-state management, puzzle validation,
  inventory management and AI integration.

## 🖥️ Application Screenshots

### Version 2 – Game Dashboard
![Dashboard](screenshots/version2_dashboard.png)

### Puzzle Challenges
![Puzzle Challenges](screenshots/version2_puzzles.png)

### Player Inventory
![Player Inventory](screenshots/version2_inventory.png)

### Successful Escape
![Successful Escape](screenshots/version2_success.png)
