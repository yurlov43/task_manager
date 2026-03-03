from models.task import Task
from repositories.task_repository import TaskRepository


def test_save_and_load(repo):
    tasks = [Task(id=1, description="Тест")]
    
    assert repo.save_all(tasks) is True
    loaded = repo.load_all()
    
    assert len(loaded) == 1
    assert loaded[0].id == 1
    assert loaded[0].description == "Тест"


def test_load_missing_file():
    repo = TaskRepository(file_path="missing.json")
    assert repo.load_all() == []


def test_next_id(repo):
    assert repo.get_next_id([]) == 1
    tasks = [Task(id=5, description="Тест")]
    assert repo.get_next_id(tasks) == 6