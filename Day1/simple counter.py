count = 0
stop_program = False
while not stop_program:
    choice = input("Provide command: ")
    if choice == "add":
    # Add command here
        count=count+1
        print(count)

    elif choice == "minus":
        count=count-1
        print(count)
    # Add command here
    elif choice == "exit":

        stop_program = True