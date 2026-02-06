from datetime import date
from typing import List
from task_manager.models import Task
from task_manager.exceptions import TaskNotFoundError


class TaskService:
    def __init__(self, tasks: List[Task] | None = None):
        self._tasks: List[Task] = tasks or []

    def get_all_tasks(self) -> List[Task]:
        return list(self._tasks)

    def add_task(self, title, priority=None, due_date=None) -> Task:
        new_id = max((t.id for t in self._tasks), default=0) + 1
        task = Task(
            id=new_id,
            title=title,
            priority=priority,
            due_date=due_date,
        )
        self._tasks.append(task)
        return task

    def list_tasks(self) -> List[Task]:
        return list(self._tasks)

    def delete_task(self, task_id: int) -> None:
        for task in self._tasks:
            if task.id == task_id:
                self._tasks.remove(task)
                return
        raise TaskNotFoundError(f"Task {task_id} not found")

    def mark_task_completed(self, task_id: int) -> Task:
        for task in self._tasks:
            if task.id == task_id:
                task.completed = True
                return task
        raise TaskNotFoundError(f"Task {task_id} not found")

    def get_progress(self) -> float:
        if not self._tasks:
            return 0.0
        completed = sum(1 for t in self._tasks if t.completed)
        return completed / len(self._tasks)

    def get_pending_tasks(self) -> List[Task]:
        return [t for t in self._tasks if not t.completed]

    def get_overdue_tasks(self, today: date) -> List[Task]:
        return [
            t for t in self._tasks
            if t.due_date and not t.completed and t.due_date < today
        ]

    def get_motivation_message(self) -> str:
        progress = self.get_progress()
        if progress == 0:
            return "Start small. One task is enough."
        if progress < 0.5:
            return "Momentum building. Keep going."
        if progress < 1.0:
            return "Almost there. Finish strong."
        return "All tasks completed. System clear."
    
    def get_tasks_sorted_by_priority(self):
        """
        High priority first (1 → 5), tasks without priority go last
        """
        return sorted(
            self._tasks,
            key=lambda t: (t.priority is None, t.priority)
        )

    def get_tasks_sorted_by_due_date(self):
        """
        Earliest due date first, tasks without due date go last
        """
        return sorted(
            self._tasks,
            key=lambda t: (t.due_date is None, t.due_date)
        )

    def get_completed_tasks(self):
        return [t for t in self._tasks if t.completed]

    def get_pending_tasks(self):
        return [t for t in self._tasks if not t.completed]

