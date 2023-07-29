import sqlite3

def view_tasks(op = 0):
    db.execute("SELECT * FROM tasks")
    tasks = db.fetchall()

    if not tasks:
        print("To tasks found.")
    else:
        print(f"{'TASKS':=^70}")
        print(f"""{color_text(f'ID.  {"Description":<44} {"Priority":<10} State', 34)}""")
        for task in tasks:
            if task[3] == 0:
                print(f"{task[0]:<4} {task[1]:<47} {task[2]:<9} {task[3]}")
            else:
                print(f"{task[0]:<4} {color_text(f'{task[1]:<47}', 9)} {task[2]:<9} {task[3]}")
    if not op:
        input(f"{color_text('Press Enter to return to menu.', 33)}")
    if op == 1:
        return input(f"{color_text('Choice: ', 33)}")


def add_task():
    while True:
        task = str(input("Task Description: ").strip())
        if task:
            break
    while True:
        priority = input("Priority (1-3): ")
        if priority and int(priority) in range(1, 4):
            break

    db.execute("""INSERT INTO tasks (objective, priority)
               VALUES (?, ?);""", (task, priority))
    connection.commit()
    print(f"{color_text(f'Added {task} to tasks!', 32)}")


def mark_task():
    op = view_tasks(1)
    db.execute("""UPDATE tasks
               SET state = 1
               WHERE id = ?;""", op)
    connection.commit()
    print(f"{color_text('Success!', 32)}")


def remove_task():
    op = view_tasks(1)
    db.execute("""DELETE FROM tasks
               WHERE id = ?""", op)
    connection.commit()
    print(f"{color_text('Success!', 32)}")


def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"


connection = sqlite3.connect("tasks.db")
db = connection.cursor()

db.execute("""SELECT count(name)
           FROM sqlite_master
           WHERE type = 'table' AND name = 'tasks';""")

if not db.fetchone()[0]:
    db.execute("""CREATE TABLE tasks(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               objective TEXT NOT NULL,
               priority INTEGER NOT NULL,
               state INTEGER DEFAULT 0;)
               """)

    print(f"{color_text('Table created successfully!', 32)}")

while True:
    print(f"{'TO DO LIST':=^70}")
    print(f"""{color_text('1.', 33)} View Tasks
{color_text('2.', 33)} Add task
{color_text('3.', 33)} Mark task as done
{color_text('4.', 33)} Remove task
{color_text('5.', 33)} Quit""")
    op = int(input(f"{color_text('Option: ', 33)}"))

    match op:
        case 1:
            view_tasks()
        case 2:
            add_task()
        case 3:
            mark_task()
        case 4:
            remove_task()
        case 5:
            print("Bye! =D")
            connection.close()
            break
        case _:
            print(f"{color_text('Invalid Option!', 31)}")
