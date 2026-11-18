from tasks import TaskManager


def show(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet. Add one first!")
    for t in tasks:
        mark = "x" if t["done"] else " "
        print(f"[{mark}] {t['id']}. {t['title']}")


def main():
    manager = TaskManager()
    while True:
        print("\n1.Add  2.Show  3.Complete  4.Delete  5.Exit")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                manager.add_task(input("Title: "))
            elif choice == "2":
                show(manager)
            elif choice == "3":
                manager.complete_task(int(input("Task ID: ")))
            elif choice == "4":
                manager.delete_task(int(input("Task ID: ")))
            elif choice == "5":
                break
            else:
                print("Invalid choice.")
        except (ValueError, KeyError, NotImplementedError) as e:
            print("Error:", e)


if __name__ == "__main__":
    main()