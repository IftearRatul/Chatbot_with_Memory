# Chatbot_with_Memory 🤖🧠

A simple Python-based chatbot that maintains conversational memory across sessions using a JSON-based storage system. The bot remembers previous interactions and uses that information to provide context-aware replies.

---

## 🚀 Features

- **Persistent Memory**  
  Stores all conversations in `memory.json`, allowing the chatbot to remember previous sessions.

- **Lightweight Architecture**  
  Core logic is handled inside `architecture.py` with minimal dependencies.

- **Configurable**  
  Includes a `config/` folder for easy modification and extension.

- **Easy to Extend**  
  Add new logic or integrate with APIs, GUIs, or other models.

---

## 📂 Project Structure

Chatbot_with_Memory/
├── app/ # Optional application logic (if used)
├── config/ # Configuration files
├── architecture.py # Main chatbot + memory logic
├── memory.json # Conversation memory storage
├── requirements.txt # Required Python packages
├── .gitignore # Git ignore rules
├── LICENSE # MIT license
└── README.md # Project documentation

##**Create and activate a virtual environment**

python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
