from services.task_service import TaskService


def test_workflow(repo):
    """Тест интеграционного поведения сервиса."""
    
    service = TaskService(repo)
    
    task1 = service.add_task("A")
    task2 = service.add_task("B")
    assert len(service.get_all_tasks()) == 2
    
    service.complete_task(task1.id)
    service.delete_task(task2.id)
    
    tasks = service.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0].id == task1.id
    assert tasks[0].completed is True
    
    service2 = TaskService(repo)
    assert len(service2.get_all_tasks()) == 1