"""
Week 4 – To-Do List with File Persistence
-------------------------------------------
A menu-driven CLI to-do list that saves tasks to a JSON file so
they survive between program runs.
"""

import json
import uuid
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).parent / "tasks.json"
DATE_FMT = "%Y-%m-%d %H:%M"


# ---------------------------------------------------------------------------
# Persistence helpers
# ---------------------------------------------------------------------------

def load_tasks() -> list[dict]:
    """Load tasks from the JSON file. Return an empty list if the file
    does not exist or is malformed."""
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks: list[dict]) -> None:
    """Persist the task list to the JSON file."""
    with DATA_FILE.open("w", encoding="utf-8") as fh:
        json.dump(tasks, fh, indent=2)


# ---------------------------------------------------------------------------
# Task operations
# ---------------------------------------------------------------------------

def create_task(description: str) -> dict:
    """Return a new task dict."""
    return {
        "id": str(uuid.uuid4())[:8],
        "description": description,
        "done": False,
        "created_at": datetime.now().strftime(DATE_FMT),
    }


def add_task(tasks: list[dict], description: str) -> dict:
    """Create a task, append it to *tasks*, and return the new task."""
    task = create_task(description)
    tasks.append(task)
    return task


def get_task_by_id(tasks: list[dict], task_id: str) -> dict | None:
    """Return the task whose id starts with *task_id*, or None."""
    for task in tasks:
        if task["id"].startswith(task_id):
            return task
    return None


def complete_task(tasks: list[dict], task_id: str) -> bool:
    """Mark the task as done. Return True on success, False if not found."""
    task = get_task_by_id(tasks, task_id)
    if task is None:
        return False
    task["done"] = True
    return True


def delete_task(tasks: list[dict], task_id: str) -> bool:
    """Remove the task from the list. Return True on success, False if not found."""
    task = get_task_by_id(tasks, task_id)
    if task is None:
        return False
    tasks.remove(task)
    return True


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

def display_tasks(tasks: list[dict]) -> None:
    if not tasks:
        print("  (no tasks yet)")
        return
    for task in tasks:
        status = "x" if task["done"] else " "
        print(f"  [{status}] {task['id']} – {task['description']}"
              f"  (added {task['created_at']})")


# ---------------------------------------------------------------------------
# Menu
# ---------------------------------------------------------------------------

MENU = """
=== To-Do List ===
1. Add task
2. View tasks
3. Mark task complete
4. Delete task
5. Quit
"""


def main() -> None:
    tasks = load_tasks()

    while True:
        print(MENU)
        choice = input("Choice: ").strip()

        if choice == "1":
            desc = input("Task description: ").strip()
            if desc:
                task = add_task(tasks, desc)
                save_tasks(tasks)
                print(f"Task added! (id: {task['id']})")
            else:
                print("Description cannot be empty.")

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            display_tasks(tasks)
            task_id = input("Enter task id to mark complete: ").strip()
            if complete_task(tasks, task_id):
                save_tasks(tasks)
                print("Task marked as complete.")
            else:
                print("Task not found.")

        elif choice == "4":
            display_tasks(tasks)
            task_id = input("Enter task id to delete: ").strip()
            if delete_task(tasks, task_id):
                save_tasks(tasks)
                print("Task deleted.")
            else:
                print("Task not found.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
