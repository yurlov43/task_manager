from typing import List, Optional
from models.task import Task
from repositories.task_repository import TaskRepository


class TaskService:
    """Сервис для бизнес-логики работы с задачами."""
    
    def __init__(self, repository: TaskRepository):
        self.repository = repository
        self.tasks: List[Task] = []
        self._load_tasks()
    
    def _load_tasks(self) -> None:
        """Загружает задачи из репозитория."""
        self.tasks = self.repository.load_all()
    
    def _save_tasks(self) -> bool:
        """Сохраняет задачи в репозиторий."""
        return self.repository.save_all(self.tasks)
    
    def get_all_tasks(self) -> List[Task]:
        """Возвращает все задачи."""
        return self.tasks.copy()
    
    def add_task(self, description: str) -> Optional[Task]:
        """
        Добавляет новую задачу.
        Возвращает созданную задачу или None в случае ошибки.
        """
        try:
            if not description or not description.strip():
                raise ValueError("Описание задачи не может быть пустым")
            
            task = Task(
                id=self.repository.get_next_id(self.tasks),
                description=description.strip()
            )
            
            self.tasks.append(task)
            
            if self._save_tasks():
                return task
            else:
                self.tasks.remove(task)
                return None
                
        except ValueError as e:
            print(f"Ошибка валидации: {e}")
            return None
    
    def delete_task(self, task_id: int) -> bool:
        """
        Удаляет задачу по ID.
        Возвращает True при успешном удалении.
        """
        for i, task in enumerate(self.tasks):
            if task.id == task_id:

                deleted_task = self.tasks.pop(i)
                
                if self._save_tasks():
                    return True
                
                self.tasks.insert(i, deleted_task)
                return False
        
        return False
    
    def complete_task(self, task_id: int) -> bool:
        """
        Отмечает задачу как выполненную.
        Возвращает True при успешном обновлении.
        """
        task = self.find_task_by_id(task_id)
        if not task:
            return False
    
        if task.completed:
            return True
    
        task.completed = True
        if self._save_tasks():
            return True
    
        task.completed = False
        return False
    
    def find_task_by_id(self, task_id: int) -> Optional[Task]:
        """Находит задачу по ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None