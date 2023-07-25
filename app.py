print("=TO DO LIST=")
while True:
    print("""1. Add Task
2. Mark task as done
3. Remove Task
4. Quit""")
    op = int(input("Option: "))

    match op:
        case 1:
            print("Você inseriu 1.")
        case 2:
            print("Você inseriu 2.")
        case 3:
            print("Você inseriu 3.")
        case 4:
            print("Bye! =D")
            break
        case _:
            print("Invalid Option!\n")
