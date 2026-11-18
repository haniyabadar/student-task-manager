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
        for t in self.tasks:
            if t["id"] == task_id:
                t["done"] = True
                return t
        raise KeyError(f"Task {task_id} not found")


    def delete_task(self, task_id):
        raise NotImplementedError("Delete task not implemented yet")