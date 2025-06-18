from task import add_task, update_task, delete_task, mark_in_progress_task
import shlex

#adds a task
def add(description):
    add_task(description)

#updates a task
def update(id, description):
    update_task(id, description)

#deletes a task
def delete(id):
    delete_task(id)

#marks a task in progress by its id
def mark_in_progress(id):
    mark_in_progress_task(id)

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
                if(len(lst_command) != 3):
                    raise Exception('CommandError: use "help" to see de available commands.')
                else:
                    update(int(lst_command[1]), lst_command[2])

            elif(lst_command[0] == "delete"):
                if(len(lst_command) != 2):
                    raise Exception('CommandError: use "help" to see de available commands.')
                else:
                    delete(int(lst_command[1]))

            elif(lst_command[0] == "mark-in-progress"):
                if(len(lst_command) != 2):
                    raise Exception('CommandError: use "help" to see de available commands.')
                else:
                    mark_in_progress(int(lst_command[1]))

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