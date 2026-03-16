# Week 4: To-Do List with File Persistence

**Difficulty:** Intermediate

## Learning Goals
- Work with lists and dictionaries
- Read and write JSON files
- Build a menu-driven CLI application
- Handle file I/O errors gracefully

## Project Description
Build a to-do list manager that saves tasks to a JSON file so they persist
between sessions. Users can add, view, complete, and delete tasks.

## Concepts Covered
- `json.load()` / `json.dump()`
- File I/O with `open()` and `with` statements
- List and dict manipulation
- UUID generation for unique task IDs
- Datetime for timestamps
- Structured menu loops

## How to Run
```bash
python main.py
```

## Sample Output
```
=== To-Do List ===
1. Add task
2. View tasks
3. Mark task complete
4. Delete task
5. Quit

Choice: 1
Task description: Buy groceries
Task added! (id: a3f2...)

Choice: 2
[ ] a3f2 – Buy groceries  (added 2024-01-15 09:00)
[x] 8b1c – Read a book    (added 2024-01-14 20:30)
```

## Challenges
1. Add task priorities (low / medium / high) and display them sorted.
2. Add a due date field and highlight overdue tasks.
3. Support multiple named lists (e.g. work, personal).
