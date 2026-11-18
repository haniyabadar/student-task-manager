class TaskManager:
    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add_task(self, title):
        task = {"id": self._next_id, "title": title, "done": False}
        self.tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self):
        return list(self.tasks)

    def complete_task(self, task_id):
        raise NotImplementedError("Complete task not implemented yet")


    def delete_task(self, task_id):
        if not isinstance(task_id, int):
            raise ValueError("Task ID must be a number")
        for t in self.tasks:
            if t["id"] == task_id:
                self.tasks.remove(t)
                return t
        raise KeyError(f"Task {task_id} not found")