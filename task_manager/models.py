from datetime import datetime, date
from task_manager.exceptions import InvalidTaskError


class Task:
    def __init__(
        self,
        id: int,
        title: str,
        completed: bool = False,
        created_at: datetime | None = None,
        priority: int | None = None,
        due_date: date | None = None,
    ):
        if not isinstance(id, int):
            raise InvalidTaskError("Task id must be an integer")

        if not isinstance(title, str) or not title.strip():
            raise InvalidTaskError("Task title must be a non-empty string")

        if priority is not None and priority not in range(1, 6):
            raise InvalidTaskError("Priority must be between 1 and 5")

        self.id = id
        self.title = title.strip()
        self.completed = completed
        self.created_at = created_at or datetime.now()
        self.priority = priority
        self.due_date = due_date

    def __str__(self) -> str:
        status = "✔ Done" if self.completed else "✖ Pending"
        priority = f"P{self.priority}" if self.priority else "No Priority"
        due = self.due_date.isoformat() if self.due_date else "No Due Date"
        return f"[{status}] {self.id}: {self.title} | {priority} | {due}"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "priority": self.priority,
            "due_date": self.due_date.isoformat() if self.due_date else None,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(
            id=data["id"],
            title=data["title"],
            completed=data.get("completed", False),
            created_at=datetime.fromisoformat(data["created_at"]),
            priority=data.get("priority"),
            due_date=date.fromisoformat(data["due_date"])
            if data.get("due_date")
            else None,
        )
