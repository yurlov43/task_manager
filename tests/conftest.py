import pytest
import tempfile
import os
from unittest.mock import Mock
from repositories.task_repository import TaskRepository
from services.task_service import TaskService


@pytest.fixture
def temp_file():
    """Временный файл."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write('[]')
        path = f.name
    yield path
    if os.path.exists(path):
        os.unlink(path)


@pytest.fixture
def repo(temp_file):
    """Репозиторий."""
    return TaskRepository(file_path=temp_file)


@pytest.fixture
def mock_repo():
    """Мок репозитория."""
    repo = Mock()
    repo.load_all.return_value = []
    repo.get_next_id.return_value = 1
    repo.save_all.return_value = True
    return repo


@pytest.fixture
def service(mock_repo):
    """Сервис с моком."""
    return TaskService(mock_repo)