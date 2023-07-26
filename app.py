import sqlite3

conection = sqlite3.connect("tasks.db")
db = conection.cursor()

db.execute("SELECT count(name) FROM sqlite_master WHERE type = 'table' AND name = 'tasks'")

if not db.fetchone()[0]:
    db.execute("""CREATE TABLE tasks(
               id INTEGER PRIMARY KEY,
               objective TEXT NOT NULL,
               expiry TEXT,
               state INTEGER DEFAULT 0)
               """)
    print("Table 'tasks' Created Sucessfully")

print("=TO DO LIST=")
while True:
    print("""1. Add Task
2. Mark task as done
3. Remove Task
4. View Tasks
5. Quit""")
    op = int(input("Option: "))

    match op:
        case 1:
            print("Você inseriu 1.")
        case 2:
            print("Você inseriu 2.")
        case 3:
            print("Você inseriu 3.")
        case 4:
            print("Você inseriu 4.")
        case 5:
            print("Bye! =D")
            break
        case _:
            print("Invalid Option!\n")
