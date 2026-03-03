from services.task_service import TaskService


class ConsoleApp:
    """Консольный интерфейс для управления задачами."""
    
    def __init__(self, task_service: TaskService):
        self.service = task_service
    
    def _print_menu(self) -> None:
        """Отображает главное меню."""
        print("\n------------ МЕНЮ ------------")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Отметить задачу выполненной")
        print("4. Показать все задачи")
        print("5. Выйти")
        print("-" * 30)

    def _add_task(self) -> None:
        """Обрабатывает добавление задачи."""
        description = input("Введите описание задачи: ").strip()
        
        if not description:
            print("Ошибка: описание не может быть пустым")
            return

        task = self.service.add_task(description)
        if task:
            print(f"Задача добавлена (ID: {task.id})")
        else:
            print("Не удалось добавить задачу")
    
    def _get_task_id(self, action_name: str) -> tuple[bool, int | None]:
        """Запрашивает ID и проверяет его корректность."""
        try:
            task_id = int(input(f"Введите ID задачи для {action_name}: ").strip())

            if not self.service.find_task_by_id(task_id):
                print(f"Задача с ID {task_id} не найдена")
                return False, None
        
            return True, task_id
        except ValueError:
            print("Ошибка: ID должен быть числом")
            return False, None

    def _delete_task(self) -> None:
        """Обрабатывает удаление задачи."""
        success, task_id = self._get_task_id("удаления")
        if not success:
            return
    
        confirm = input(f"Удалить задачу с ID {task_id}? (д/н): ").strip().lower()
        if confirm in ['д', 'да', 'y', 'yes']:
            if self.service.delete_task(task_id):
                print(f"Задача {task_id} удалена")
            else:
                print(f"Не удалось удалить задачу {task_id}")
    
    def _complete_task(self) -> None:
        """Обрабатывает отметку задачи как выполненной."""
        success, task_id = self._get_task_id("отметки как выполненной")
        if not success:
            return
    
        if self.service.complete_task(task_id):
            print(f"Задача отмечена как выполненная")
        else:
            print(f"Не удалось отметить задачу")
    
    def _list_tasks(self) -> None:
        """Показывает все задачи."""
        tasks = self.service.get_all_tasks()
    
        if not tasks:
            print("\nСписок задач пуст")
            return
    
        print("\n---------- ВСЕ ЗАДАЧИ ----------")
    
        for task in tasks:
            status = "[V]" if task.completed else "[ ]"
            print(f"{status} ID: {task.id:3} | {task.description}")
    
        print("-" * 32) 
    
    def run(self) -> None:
        """Запускает главный цикл приложения."""
        print("\nДобро пожаловать в менеджер задач!")
        
        while True:
            self._print_menu()
            choice = input("Выберите действие (1-5): ").strip()
            
            if choice == "1":
                self._add_task()
            elif choice == "2":
                self._delete_task()
            elif choice == "3":
                self._complete_task()
            elif choice == "4":
                self._list_tasks()
            elif choice == "5":
                print("\nДо свидания!")
                break
            else:
                print("Неверный ввод. Пожалуйста, выберите 1-5")