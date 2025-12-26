# Construction Management MicroSaaS

A simple construction management system developed as my **CS50 Final Project**.
This project represents my first complete backend application using Flask and SQLite.

---

## 🚧 Project Overview

This MicroSaaS was designed to help **small and medium construction companies** manage their daily operations without complex accounting systems.

The focus is on **practical workflow**, clarity, and simplicity.

---

## ✨ Features

- Create, edit and delete construction works (CRUD)
- Dashboard with all registered works
- Flash messages for user feedback
- SQLite database for persistence
- Clean and simple UI

---

## 🧠 Technical Stack

- **Backend:** Python + Flask
- **Database:** SQLite
- **Templates:** Jinja2
- **Frontend:** HTML + CSS

---

## 🧩 System Flow (Simplified)
```text
User Action → Flask Route → Database (SQLite)
             → Flash Message → Redirect → Dashboard
```
---

## 🗂️ Project Structure
```text
project/
├── app.py              # Main Flask application
├── database.db         # SQLite database
├── requirements.txt    # Project dependencies
├── templates/          # HTML templates (Jinja2)
│   ├── layout.html
│   ├── dashboard.html
│   ├── create_work.html
│   └── edit_work.html
├── static/             # Static files
│   └── style.css
```
---

## ▶️ How to Run the Project

```bash
pip install -r requirements.txt
flask run

