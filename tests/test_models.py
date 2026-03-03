import pytest
from models.task import Task


def test_task_creation():
    task = Task(id=1, description="Тест")
    assert task.id == 1
    assert task.description == "Тест"
    assert task.completed is False


def test_empty_description_raises():
    with pytest.raises(ValueError):
        Task(description="")


def test_task_serialization():
    task = Task(id=1, description="Тест", completed=True)
    data = task.model_dump()
    restored = Task.model_validate(data)
    assert restored.id == task.id
    assert restored.description == task.description
    assert restored.completed == task.completed