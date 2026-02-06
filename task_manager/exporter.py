import csv
import json
from typing import List
from task_manager.models import Task


def export_to_csv(tasks: List[Task], filename: str) -> None:
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["id", "title", "completed", "created_at", "priority", "due_date"]
        )
        for task in tasks:
            writer.writerow([
                task.id,
                task.title,
                task.completed,
                task.created_at.isoformat(),
                task.priority,
                task.due_date.isoformat() if task.due_date else None
            ])


def export_to_json(tasks: List[Task], filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(
            [task.to_dict() for task in tasks],
            f,
            indent=4
        )
