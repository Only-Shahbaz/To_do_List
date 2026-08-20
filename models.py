

class Task:
    def __init__(self, task_id: int, title:str, description:str, start_date: str, end_date: str):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.is_Completed = False

    def __str__(self):
        status = "Completed" if self.is_Completed else "pending"
        return f"Task ID: {self.task_id}\nTitle: {self.title}\nDescription: {self.description}\nStart Date: {self.start_date}\nEnd Date: {self.end_date}\nStatus: {status}"