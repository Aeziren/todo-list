import sqlite3

def view_tasks():
    db.execute("SELECT * FROM tasks")
    tasks = db.fetchall()

    if not tasks:
        print("To tasks found.")
    else:
        print(f"N. {'Description':<24} Priority")
        for n, task in enumerate(tasks):
            print(f"{n+1}. {task[0]:<24} {task[1]:^8}")
    input("Press to return to menu.")


def add_task():
    while True:
        task = str(input("Task Description: ").strip())
        if task:
            break
    while True:
        priority = input("Priority (1-3): ")
        if priority and int(priority) in range(1, 4):
            break

    db.execute("INSERT INTO tasks (objective, priority) VALUES (?, ?)", (task, priority))
    connection.commit()
    print(f"Added {task} to tasks!")


connection = sqlite3.connect("tasks.db")
db = connection.cursor()

db.execute("SELECT count(name) FROM sqlite_master WHERE type = 'table' AND name = 'tasks'")

if not db.fetchone()[0]:
    db.execute("""CREATE TABLE tasks(
               objective TEXT NOT NULL,
               priority INTEGER NOT NULL,
               state INTEGER DEFAULT 0)
               """)
    print("Table 'tasks' Created Sucessfully")

print("=TO DO LIST=")
while True:
    print("""1. View Tasks
2. Add task
3. Mark task as done
4. Remove task
5. Quit""")
    op = int(input("Option: "))

    match op:
        case 1:
            view_tasks()
        case 2:
            add_task()
        case 3:
            print("Você inseriu 3.")
        case 4:
            print("Você inseriu 4.")
        case 5:
            print("Bye! =D")
            connection.close()
            break
        case _:
            print("Invalid Option!\n")
