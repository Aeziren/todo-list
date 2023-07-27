import sqlite3

def add_task():
    while True:
        task = input("Task Description: ").strip()
        if task:
            break

    exp = input("Expiry date (optional): ").strip()

    db.execute("INSERT INTO tasks (objective, expiry) VALUES (?, ?)", (task, exp))
    connection.commit()
    print(f"Added {task} to tasks!")


connection = sqlite3.connect("tasks.db")
db = connection.cursor()

db.execute("SELECT count(name) FROM sqlite_master WHERE type = 'table' AND name = 'tasks'")

if not db.fetchone()[0]:
    db.execute("""CREATE TABLE tasks(
               objective TEXT NOT NULL,
               expiry TEXT,
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
            print("Op1")
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
