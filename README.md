# To_do_List_APP
# Modular To-Do List Application

A lightweight, clean, and modular Command Line Interface (CLI) To-Do List application written in core Python. This project demonstrates software design best practices using a **three-tier modular architecture** separating data modeling, business logic/storage, and user interface layers.

---

## 🛠️ Project Structure

The project is organized into clear, independent modules:

```text
todo_project/
│── models.py      # Data Layer: Task entity & date comparison logic
│── storage.py     # Business Logic / Data Layer: In-memory task management
└── main.py        # Presentation Layer: CLI interaction and user flow