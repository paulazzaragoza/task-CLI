from task import add_task
import shlex

#adds a task
def add(description):
    add_task(description)

#main program
def program():
    end = False

    while(not end):
        try:
            command = input(">>> task-cli ")
            lst_command = shlex.split(command)

            if(lst_command[0] == "add"):
                if(len(lst_command) != 2):
                    raise Exception('CommandError: use /"help/" to see de available commands.')
                else:
                    add(lst_command[1])

            elif(lst_command[0] == "help"):
                if(len(lst_command) > 1):
                    raise Exception('CommandError: use /"help/" to see de available commands.')
                else:
                    print("\t> add [task] \n\t> update [id] [task] \n\t> delete [id] \n\t> " \
                    "mark in-progress/mark-done [id] \n\t> list *empty*/done/todo/in-progress" \
                    "\n\t> exit\n")

            elif(lst_command[0] == "exit"):
                if(len(lst_command) > 1):
                    raise Exception('CommandError: use /"help/" to see de available commands.')
                else:
                    print("Bye bye!")
                    end = True

        except Exception as e:
            print(e)

if __name__ == "__main__":
    program()