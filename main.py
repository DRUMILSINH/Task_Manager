import os
from datetime import datetime, date

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.progress import Progress

from task_manager.app import create_app, persist
from task_manager.exceptions import TaskManagerError
from task_manager.exporter import export_to_csv, export_to_json

console = Console()


# ---------- UI HELPERS ----------

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_menu():
    console.print("\n[bold cyan]SMART TASK MANAGER 🚀[/bold cyan]")
    console.print("1. Add task")
    console.print("2. List tasks")
    console.print("3. Mark task completed")
    console.print("4. Delete task")
    console.print("5. Show progress")
    console.print("6. Show overdue tasks")
    console.print("7. Export tasks")
    console.print("0. Exit")


# ---------- ACTION HANDLERS ----------

def add_task_ui(service):
    clear_screen()
    console.print("[bold green]Add New Task[/bold green]\n")

    title = Prompt.ask("Task title")

    priority = IntPrompt.ask(
        "Priority (1 = High, 5 = Low)",
        default=None,
        show_default=False
    )

    due_raw = Prompt.ask(
        "Due date (YYYY-MM-DD, press Enter to skip)",
        default=""
    )

    due_date = (
        datetime.strptime(due_raw, "%Y-%m-%d").date()
        if due_raw else None
    )

    task = service.add_task(title, priority, due_date)
    persist(service)

    console.print(f"\n[green]Added:[/green] {task}\n")


def list_tasks_ui(service):
    clear_screen()
    console.print("[bold cyan]View Tasks[/bold cyan]\n")
    console.print("1. All tasks")
    console.print("2. Pending tasks")
    console.print("3. Completed tasks")
    console.print("4. Sort by priority")
    console.print("5. Sort by due date")

    choice = Prompt.ask(
        "Choose view",
        choices=["1", "2", "3", "4", "5"]
    )

    if choice == "1":
        tasks = service.list_tasks()
    elif choice == "2":
        tasks = service.get_pending_tasks()
    elif choice == "3":
        tasks = service.get_completed_tasks()
    elif choice == "4":
        tasks = service.get_tasks_sorted_by_priority()
    elif choice == "5":
        tasks = service.get_tasks_sorted_by_due_date()

    if not tasks:
        console.print("\n[yellow]No tasks found.[/yellow]\n")
        return

    table = Table(title="Tasks")
    table.add_column("ID", justify="right")
    table.add_column("Title")
    table.add_column("Status")
    table.add_column("Priority")
    table.add_column("Due Date")

    for t in tasks:
        table.add_row(
            str(t.id),
            t.title,
            "✔ Done" if t.completed else "✖ Pending",
            f"P{t.priority}" if t.priority else "-",
            t.due_date.isoformat() if t.due_date else "-"
        )

    console.print()
    console.print(table)
    console.print()


def complete_task_ui(service):
    clear_screen()
    console.print("[bold green]Complete Task[/bold green]\n")

    task_id = IntPrompt.ask("Enter task ID")
    task = service.mark_task_completed(task_id)
    persist(service)

    console.print(f"\n[green]Completed:[/green] {task}\n")


def delete_task_ui(service):
    clear_screen()
    console.print("[bold red]Delete Task[/bold red]\n")

    task_id = IntPrompt.ask("Enter task ID")

    if Confirm.ask("Are you sure you want to delete this task?"):
        service.delete_task(task_id)
        persist(service)
        console.print(f"\n[red]Deleted task {task_id}[/red]\n")
    else:
        console.print("\n[yellow]Deletion cancelled.[/yellow]\n")


def show_progress_ui(service):
    clear_screen()
    console.print("[bold cyan]Progress[/bold cyan]\n")

    progress_value = service.get_progress()
    percent = int(progress_value * 100)

    with Progress() as progress:
        bar = progress.add_task("Completion", total=100)
        progress.update(bar, completed=percent)

    console.print(f"\n{service.get_motivation_message()}\n")


def overdue_tasks_ui(service):
    clear_screen()
    console.print("[bold red]Overdue Tasks[/bold red]\n")

    overdue = service.get_overdue_tasks(date.today())

    if not overdue:
        console.print("[green]No overdue tasks 🎉[/green]\n")
        return

    for task in overdue:
        console.print(task)
    console.print()

def export_tasks_ui(service):
    clear_screen()
    console.print("[bold cyan]Export Tasks[/bold cyan]\n")

    console.print("1. All tasks")
    console.print("2. Pending tasks")
    console.print("3. Completed tasks")
    console.print("4. Sort by priority")
    console.print("5. Sort by due date")

    view = Prompt.ask(
        "Choose tasks to export",
        choices=["1", "2", "3", "4", "5"]
    )

    if view == "1":
        tasks = service.list_tasks()
    elif view == "2":
        tasks = service.get_pending_tasks()
    elif view == "3":
        tasks = service.get_completed_tasks()
    elif view == "4":
        tasks = service.get_tasks_sorted_by_priority()
    elif view == "5":
        tasks = service.get_tasks_sorted_by_due_date()

    if not tasks:
        console.print("[yellow]No tasks to export.[/yellow]\n")
        return

    fmt = Prompt.ask(
        "Export format",
        choices=["csv", "json"]
    )

    filename = Prompt.ask(
        "Enter filename (without extension)",
        default="tasks_export"
    )

    if fmt == "csv":
        export_to_csv(tasks, f"{filename}.csv")
    else:
        export_to_json(tasks, f"{filename}.json")

    console.print(
        f"\n[green]Exported {len(tasks)} tasks to {filename}.{fmt}[/green]\n"
    )


# ---------- MAIN LOOP ----------

def main():
    service = create_app()

    while True:
        try:
            show_menu()
            choice = Prompt.ask(
                "\nChoose option",
                choices=["0", "1", "2", "3", "4", "5", "6", "7"]
            )

            if choice == "1":
                add_task_ui(service)
            elif choice == "2":
                list_tasks_ui(service)
            elif choice == "3":
                complete_task_ui(service)
            elif choice == "4":
                delete_task_ui(service)
            elif choice == "5":
                show_progress_ui(service)
            elif choice == "6":
                overdue_tasks_ui(service)
            elif choice == "7":
                export_tasks_ui(service)
            elif choice == "0":
                console.print("\n[bold cyan]Goodbye 👋[/bold cyan]")
                break

        except TaskManagerError as e:
            console.print(f"\n[red]Error:[/red] {e}\n")
        except KeyboardInterrupt:
            console.print("\n[bold cyan]Exited safely.[/bold cyan]")
            break


if __name__ == "__main__":
    main()
