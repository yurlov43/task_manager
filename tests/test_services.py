def test_add_task(service, mock_repo):
    task = service.add_task("Тест")
    
    assert task is not None
    assert task.id == 1
    assert task.description == "Тест"
    assert len(service.get_all_tasks()) == 1
    assert mock_repo.save_all.call_count == 1


def test_add_task_invalid(service):
    assert service.add_task("") is None
    assert len(service.get_all_tasks()) == 0


def test_delete_task(service, mock_repo):
    task = service.add_task("Тест")

    assert service.delete_task(task.id) is True
    assert len(service.get_all_tasks()) == 0
    assert mock_repo.save_all.call_count == 2


def test_delete_task_not_found(service):
    service.add_task("Тест")

    assert service.delete_task(999) is False
    assert len(service.get_all_tasks()) == 1


def test_complete_task(service):
    task = service.add_task("Тест")
    
    assert service.complete_task(task.id) is True
    assert task.completed is True


def test_complete_task_not_found(service):
    service.add_task("Тест")

    assert service.complete_task(999) is False


def test_find_task(service):
    task = service.add_task("Тест")

    assert service.find_task_by_id(task.id) is task
    assert service.find_task_by_id(999) is None