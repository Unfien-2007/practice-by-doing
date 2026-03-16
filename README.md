# Practice by Doing – Weekly Python Projects

A structured series of Python projects that grow in complexity week by week,
taking you from complete beginner to confident intermediate/advanced developer.

---

## Curriculum Overview

| Week | Project | Difficulty | Key Concepts |
|------|---------|------------|--------------|
| [01](week_01_hello_world/) | Hello World & Basic I/O | 🟢 Beginner | `print`, `input`, f-strings, type conversion |
| [02](week_02_calculator/) | Simple Calculator | 🟢 Beginner | Functions, loops, `if/elif/else`, exceptions |
| [03](week_03_guessing_game/) | Number Guessing Game | 🟡 Beginner → Intermediate | `random`, game loops, scoring, state |
| [04](week_04_todo_list/) | To-Do List with File Persistence | 🟡 Intermediate | JSON I/O, dicts, menu-driven CLI, UUIDs |
| [05](week_05_web_scraper/) | Web Scraper | 🟠 Intermediate | `requests`, `BeautifulSoup`, CSV output |
| [06](week_06_data_analysis/) | CSV Data Analysis | 🟠 Intermediate → Advanced | `pandas`, `groupby`, statistics, reporting |
| [07](week_07_rest_api/) | REST API with Flask | 🔴 Advanced | Flask, CRUD endpoints, HTTP status codes |
| [08](week_08_database_app/) | Database-Backed CLI App | 🔴 Advanced | SQLAlchemy ORM, SQLite, repository pattern |

---

## Getting Started

### Prerequisites
- Python 3.11 or higher
- `pip` (comes with Python)

### Running a Weekly Project
Each week lives in its own folder.  Navigate there and follow its `README.md`:

```bash
cd week_01_hello_world
python main.py
```

### Installing Project Dependencies
Projects that need third-party libraries include a `requirements.txt`:

```bash
cd week_05_web_scraper
pip install -r requirements.txt
python main.py
```

### Running the Tests
All weeks include unit/integration tests powered by **pytest**.

```bash
# Install test dependencies
pip install pytest pandas flask sqlalchemy requests beautifulsoup4

# Run all tests
pytest

# Run tests for a specific week
pytest week_03_guessing_game/
```

---

## Project Descriptions

### Week 1 – Hello World & Basic I/O 🟢
Build a simple greeting program that asks for the user's name and age, then
prints personalised facts such as birth year and months lived.  The perfect
first Python programme.

### Week 2 – Simple Calculator 🟢
An interactive CLI calculator supporting `+`, `-`, `*`, and `/`.  Handles
division-by-zero errors gracefully and loops until the user quits.

### Week 3 – Number Guessing Game 🟡
The computer picks a secret number; the player races to guess it within a
limited number of attempts.  A score is awarded based on how few guesses were
needed.

### Week 4 – To-Do List with File Persistence 🟡
A menu-driven task manager that reads and writes tasks to a `tasks.json` file,
so your list survives between sessions.

### Week 5 – Web Scraper 🟠
Scrape the Hacker News front page using `requests` and `BeautifulSoup`, then
export the results (title, URL, score, author) to a CSV file.

### Week 6 – CSV Data Analysis 🟠
Load a bundled sales dataset with `pandas`, compute revenue totals, identify
the best-selling product, and produce a monthly trend report.

### Week 7 – REST API with Flask 🔴
A fully-functional Book Library API with five RESTful endpoints (list, get,
create, update, delete).  Uses Flask's application-factory pattern so it's
easy to test.

### Week 8 – Database-Backed CLI App 🔴
A Contact Book powered by SQLite and the SQLAlchemy ORM.  Demonstrates the
repository pattern, `argparse`-based CLI commands, and integration testing
with an in-memory database.

---

## Learning Path

```
Week 1 ──► Week 2 ──► Week 3 ──► Week 4
                                    │
                               Week 5 ──► Week 6
                                              │
                                         Week 7 ──► Week 8
```

Feel free to attempt the **Challenges** listed in each week's `README.md` to
deepen your understanding before moving on.

Happy coding! 🐍
