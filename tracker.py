from task import add_task, update_task
import shlex

#adds a task
def add(description):
    add_task(description)

def update(id, description):
    update_task(id, description)

#main program
def program():
    end = False

    while(not end):
        try:
            command = input(">>> task-cli ")
            lst_command = shlex.split(command)

            if(lst_command[0] == "add"):
                if(len(lst_command) != 2):
                    raise Exception('CommandError: use "help" to see de available commands.')
                else:
                    add(lst_command[1])

            elif(lst_command[0] == "update"):
                update(int(lst_command[1]), lst_command[2])

            elif(lst_command[0] == "help"):
                if(len(lst_command) > 1):
                    raise Exception('CommandError: use "help" to see de available commands.')
                else:
                    print('\t> add "[description]" \n\t> update [id] "[description]" \n\t> delete [id] \n\t> ' \
                    'mark in-progress/mark-done [id] \n\t> list *empty*/done/todo/in-progress' \
                    '\n\t> exit\n')

            elif(lst_command[0] == "exit"):
                if(len(lst_command) > 1):
                    raise Exception('CommandError: use "help" to see de available commands.')
                else:
                    print("All data has been saved. Bye!")
                    end = True
            else:
                raise Exception('CommandError: use "help" to see de available commands.')
        except Exception as e:
            print(e)

if __name__ == "__main__":
    program()