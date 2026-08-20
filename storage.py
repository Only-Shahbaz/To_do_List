from models import Task


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title:str, description:str, start_date: str, end_date: str) -> Task:
        task = Task(self.next_id, title, description, start_date, end_date)
        self.tasks.append(task)
        self.next_id += 1
        return task