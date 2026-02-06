import json
import os
from typing import List
from task_manager.models import Task
from task_manager.exceptions import StorageError

DATA_DIR = "data"
DB_FILE = "tasks.json"


def _get_db_path() -> str:
    os.makedirs(DATA_DIR, exist_ok=True)
    return os.path.join(DATA_DIR, DB_FILE)


def load_tasks() -> List[Task]:
    path = _get_db_path()

    if not os.path.exists(path):
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)
            return [Task.from_dict(item) for item in raw]
    except json.JSONDecodeError as e:
        raise StorageError("Corrupted task storage file") from e
    except OSError as e:
        raise StorageError("Failed to read task storage") from e


def save_tasks(tasks: List[Task]) -> None:
    path = _get_db_path()

    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(
                [task.to_dict() for task in tasks],
                f,
                indent=4
            )
    except OSError as e:
        raise StorageError("Failed to write task storage") from e
