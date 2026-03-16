"""Tests for Week 4 – To-Do List with File Persistence."""

import json
import pytest
from week_04_todo_list.main import (
    add_task,
    complete_task,
    create_task,
    delete_task,
    get_task_by_id,
    load_tasks,
    save_tasks,
)


def test_create_task_fields():
    task = create_task("Buy milk")
    assert task["description"] == "Buy milk"
    assert task["done"] is False
    assert "id" in task
    assert "created_at" in task


def test_add_task():
    tasks = []
    task = add_task(tasks, "Test task")
    assert len(tasks) == 1
    assert tasks[0] is task


def test_get_task_by_id():
    tasks = []
    task = add_task(tasks, "Find me")
    found = get_task_by_id(tasks, task["id"])
    assert found is task


def test_get_task_by_id_not_found():
    tasks = []
    add_task(tasks, "Something")
    assert get_task_by_id(tasks, "xxxxxxxx") is None


def test_complete_task():
    tasks = []
    task = add_task(tasks, "Finish project")
    result = complete_task(tasks, task["id"])
    assert result is True
    assert task["done"] is True


def test_complete_task_not_found():
    tasks = []
    assert complete_task(tasks, "nonexistent") is False


def test_delete_task():
    tasks = []
    task = add_task(tasks, "Delete me")
    result = delete_task(tasks, task["id"])
    assert result is True
    assert len(tasks) == 0


def test_delete_task_not_found():
    tasks = []
    assert delete_task(tasks, "nonexistent") is False


def test_save_and_load_tasks(tmp_path, monkeypatch):
    import week_04_todo_list.main as m

    data_file = tmp_path / "tasks.json"
    monkeypatch.setattr(m, "DATA_FILE", data_file)

    tasks = [create_task("Persist me")]
    save_tasks(tasks)
    loaded = load_tasks()
    assert len(loaded) == 1
    assert loaded[0]["description"] == "Persist me"


def test_load_tasks_missing_file(tmp_path, monkeypatch):
    import week_04_todo_list.main as m

    monkeypatch.setattr(m, "DATA_FILE", tmp_path / "nonexistent.json")
    assert load_tasks() == []
