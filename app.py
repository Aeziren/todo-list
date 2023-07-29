# Imports
import sqlite3

# Functions:
# Function to view tasks, ask the user for input if triggered
def view_tasks(op = 0):
    # Search on database
    db.execute("SELECT * FROM tasks")
    tasks = db.fetchall()

    if not tasks:
        print("To tasks found.")
    else:
        # Show tasks on CLI
        print(f"{'TASKS':=^70}")
        print(f"""{color_text(f'ID.  {"Description":<44} {"Priority":<10}', 34)}""")
        for task in tasks:
            if task[3] == 0:
                print(f"{task[0]:<4} {task[1]:<47} {task[2]:<9}")
            else:
                print(f"{task[0]:<4} {color_text(f'{task[1]:<47}', 9)} {task[2]:<9}")
    if not op:
        input(f"{color_text('Press Enter to return to menu.', 33)}")
    if op == 1:
        choice = input(f"{color_text('Choice: ', 33)}")
        print(choice)
        return choice


# Function to add tasks
def add_task():
    # Ask user for input of description and priority
    while True:
        task = str(input("Task Description: ").strip())
        if task:
            break
    while True:
        priority = input("Priority (1-3): ")
        if priority and int(priority) in range(1, 4):
            break

    # Create query
    query = """INSERT INTO tasks (objective, priority)
    VALUES (?, ?);"""

    # Insert task into database and commit changes.
    db.execute(query, (task, priority))
    connection.commit()

    # Feedback
    print(f"{color_text(f'Added {task} to tasks!', 32)}")


# Function to mark a task a done
def mark_task():
    # Make a call to the function of viewing tasks, triggering input part of it
    op = view_tasks(1)

    # Create query
    query = """UPDATE tasks
    SET state = 1 WHERE id = (?)"""

    # Insert value into database and commit changes.
    db.execute(query, (op,))
    connection.commit()

    # Feedback
    print(f"{color_text('Success!', 32)}")


# Function to remove task from database, works simmilary as mark task as done.
def remove_task():
    # Make a call to the function of viewing tasks, triggering input part of it
    op = view_tasks(1)

    # Create query
    query = """DELETE FROM tasks
    WHERE id = ?"""

    # Insert value into database and commit changes.
    db.execute(query, (op, ))
    connection.commit()

    # Feedback
    print(f"{color_text('Success!', 32)}")


# Function used in all code to color the CLI, simply return a f-string
def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

# End of function section

# Initialize database
connection = sqlite3.connect("tasks.db")
db = connection.cursor()

# Query used for verification of database existence
verify_query = """SELECT count(name)
FROM sqlite_master
WHERE type = 'table' AND name = 'tasks';"""

# Query used to create database
creation_query = ("""CREATE TABLE tasks(
id INTEGER PRIMARY KEY AUTOINCREMENT
objective TEXT NOT NULL
priority INTEGER NOT NULL
state INTEGER DEFAULT 0;)""")

# Verify for the existence of database, if it does not exist, create a new one.
db.execute(verify_query)

if not db.fetchone()[0]:
    db.execute(creation_query)

    # Feedback user about creating of database
    print(f"{color_text('Table created successfully!', 32)}")

# Menu
while True:
    print(f"{'TO DO LIST':=^70}")
    print(f"""{color_text('1.', 33)} View Tasks
{color_text('2.', 33)} Add task
{color_text('3.', 33)} Mark task as done
{color_text('4.', 33)} Remove task
{color_text('5.', 33)} Quit""")
    op = int(input(f"{color_text('Option: ', 33)}"))

    # Switch
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
            # Close connection to database
            connection.close()
            break
        case _:
            print(f"{color_text('Invalid Option!', 31)}")
