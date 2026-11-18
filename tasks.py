class TaskManager:
    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add_task(self, title):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title cannot be empty")
        if len(title.strip()) > 100:
            raise ValueError("Task title too long (max 100 chars)")
        task = {"id": self._next_id, "title": title.strip(), "done": False}
        self.tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self):
        return list(self.tasks)

    def complete_task(self, task_id):
        raise NotImplementedError("Complete task not implemented yet")


    def delete_task(self, task_id):
        raise NotImplementedError("Delete task not implemented yet")