from repositories.task_repository import TaskRepository
from services.task_service import TaskService
from presentation.console_app import ConsoleApp


def main():
    repository = TaskRepository("tasks.json")
    service = TaskService(repository)
    app = ConsoleApp(service)
    app.run()


if __name__ == "__main__":
    main()
