import json
import os
from typing import List
from models.task import Task


class TaskRepository:
    """Репозиторий для работы с задачами в JSON-файле."""
    
    def __init__(self, file_path: str = "tasks.json"):
        self.file_path = file_path
    
    def load_all(self) -> List[Task]:
        """Загружает все задачи из файла."""
        if not os.path.exists(self.file_path):
            return []
        
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Task.model_validate(item) for item in data]
        except (json.JSONDecodeError, IOError, OSError) as e:
            print(f"Ошибка при загрузке задач: {e}")
            return []
        except Exception as e:
            print(f"Некорректные данные в файле: {e}")
            return []
    
    def save_all(self, tasks: List[Task]) -> bool:
        """Сохраняет все задачи в файл."""
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                data = [task.model_dump() for task in tasks]
                json.dump(data, f, ensure_ascii=False)
            return True
        except (IOError, OSError) as e:
            print(f"Ошибка при сохранении задач: {e}")
            return False
    
    def get_next_id(self, tasks: List[Task]) -> int:
        """Возвращает следующий свободный ID."""
        if not tasks:
            return 1
        return max(task.id for task in tasks) + 1