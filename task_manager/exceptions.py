class TaskManagerError(Exception):
    """Base exception for the Task Manager application."""
    pass


class TaskNotFoundError(TaskManagerError):
    """Raised when a task with a given ID does not exist."""
    pass


class InvalidTaskError(TaskManagerError):
    """Raised when task data is invalid."""
    pass


class StorageError(TaskManagerError):
    """Raised when task persistence fails."""
    pass
