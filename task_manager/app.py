from task_manager.service import TaskService
from task_manager.storage import load_tasks, save_tasks


def create_app() -> TaskService:
    tasks = load_tasks()
    return TaskService(tasks)


def persist(service: TaskService) -> None:
    save_tasks(service.get_all_tasks())
