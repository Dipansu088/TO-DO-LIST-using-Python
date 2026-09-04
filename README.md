# 📋 CLI To-Do List Tracker

A lightweight, persistent command-line task manager built with Python. This project demonstrates clean terminal-based control flow, defensive user input validation, and local state management using JSON file serialization.

---

## ✨ Features

- **Full CRUD Support:** Add, view, update completion status, delete individual tasks, or wipe all records.
- **Persistent Storage:** Tasks automatically sync to a local `tasks.json` file across program runs.
- **Defensive Error Handling:** 
  - Prevents program crashes from non-integer inputs (`ValueError` handling).
  - Validates user input against active task indices.
  - Handles missing storage files seamlessly via automated fallback routines.

---

## 🛠️ Tech Stack

- **Language:** Python 3.X
- **Standard Libraries:** `json` (data persistence), `sys` / built-in control flow

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8 or higher installed:

```bash
python --version