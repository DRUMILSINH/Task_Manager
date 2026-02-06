# 🧠 Smart CLI Task Manager (Python)

A **production-style, interactive CLI task manager** built in Python with clean architecture, persistent storage, rich terminal UI, and full unit test coverage.

This project focuses on **software design, separation of concerns, and real-world usability**, not just scripting.

---

## ✨ Features

* ✅ Add, list, complete, and delete tasks
* 🎯 Task priorities (1 = High → 5 = Low)
* 📅 Optional due dates with overdue detection
* 📊 Progress tracking with motivation messages
* 🧭 Sorting & filtering:

  * Pending / Completed
  * By priority
  * By due date
* 📤 Export tasks to **CSV** or **JSON**
* 🎨 Interactive terminal UI using **Rich**
* 💾 Persistent storage (JSON-based)
* 🧪 Unit tested (models, service, storage)

---

## 🏗️ Architecture Overview

This project follows **clean architecture principles**.

```
task_manager/
│
├── models.py       # Domain model (Task)
├── service.py      # Business logic (TaskService)
├── storage.py      # Persistence layer (JSON)
├── app.py          # Application bootstrap
├── exporter.py     # CSV / JSON export logic
├── exceptions.py   # Custom domain exceptions
│
├── data/
│   └── tasks.json  # Persistent storage
│
├── tests/          # Unit tests
│   ├── test_models.py
│   ├── test_service.py
│   └── test_storage.py
│
└── main.py         # Interactive Rich-based CLI
```

### Design Principles Used

* **Separation of concerns**
* **Single Responsibility Principle**
* **Domain-driven design (lightweight)**
* **Replaceable interfaces** (CLI can be swapped for GUI/API)
* **Testability-first architecture**

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/cli-task-manager.git
cd cli-task-manager
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # macOS/Linux
```

### 3️⃣ Install dependencies

```bash
pip install rich
```

### 4️⃣ Run the app

```bash
python main.py
```

No command memorization required — everything is **menu-driven**.

---

## 🖥️ Sample CLI Flow

```
SMART TASK MANAGER 🚀
1. Add task
2. List tasks
3. Mark task completed
4. Delete task
5. Show progress
6. Show overdue tasks
7. Export tasks
0. Exit
```

---

## 📤 Exporting Tasks

You can export:

* All tasks
* Pending tasks
* Completed tasks
* Sorted views

Formats supported:

* **CSV** (Excel-friendly)
* **JSON** (API/backup-friendly)

---

## 🧪 Running Tests

All core logic is unit tested.

```bash
python -m unittest discover tests
```

Tests cover:

* Task validation
* Business rules
* Progress calculation
* Persistence safety

---

## 🧠 What This Project Demonstrates

* Writing **maintainable Python**, not scripts
* Designing **testable business logic**
* Handling persistence cleanly
* Building **user-friendly CLI tools**
* Applying backend engineering principles in small projects

---

## 📌 Resume Bullet (You Can Use This)

```
• Built a production-style Python CLI Task Manager with clean architecture,
  interactive Rich-based UI, persistent storage, export functionality, and
  full unit test coverage using unittest.
```

---

## 🔮 Future Improvements

* SQLite backend (drop-in replacement for JSON)
* Tag-based task grouping
* Recurring tasks
* GUI or REST API interface

---

## 🏁 Project Status

**✔ Complete

