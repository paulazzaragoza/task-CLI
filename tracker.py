from task import add_task, update_task, delete_task, mark_task, list_all_tasks, list_by_status_tasks
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
    mark_task(id, "in-progress")

#marks a task done by its id
def mark_done(id):
    mark_task(id, "done")

#lists all tasks
def list_all():
    list_all_tasks()

#lists by status the tasks
def list_by_status(status):
    list_by_status_tasks(status)

#main program
def program():
    end = False

    while(not end):
        try:
            command = input(">>> task-cli ")
            lst_command = shlex.split(command)

            if(lst_command[0] == "add"):
                if(len(lst_command) != 2):
                    raise Exception('\tCommandError: use "help" to see de available commands.')
                else:
                    add(lst_command[1])

            elif(lst_command[0] == "update"):
                if(len(lst_command) != 3):
                    raise Exception('\tCommandError: use "help" to see de available commands.')
                else:
                    update(int(lst_command[1]), lst_command[2])

            elif(lst_command[0] == "delete"):
                if(len(lst_command) != 2):
                    raise Exception('\tCommandError: use "help" to see de available commands.')
                else:
                    delete(int(lst_command[1]))

            elif(lst_command[0] == "mark-in-progress"):
                if(len(lst_command) != 2):
                    raise Exception('\tCommandError: use "help" to see de available commands.')
                else:
                    mark_in_progress(int(lst_command[1]))

            elif(lst_command[0] == "mark-done"):
                if(len(lst_command) != 2):
                    raise Exception('\tCommandError: use "help" to see de available commands.')
                else:
                    mark_done(int(lst_command[1]))

            elif(lst_command[0] == "list"):
                if(len(lst_command) == 1):
                    list_all()
                elif(len(lst_command) == 2 and lst_command[1] == "done"):
                    list_by_status("done")
                elif(len(lst_command) == 2 and lst_command[1] == "todo"):
                    list_by_status("todo")
                elif(len(lst_command) == 2 and lst_command[1] == "todo"):
                    list_by_status("in-progress")
                else:
                    raise Exception('\tCommandError: use "help" to see de available commands.')

            elif(lst_command[0] == "help"):
                if(len(lst_command) > 1):
                    raise Exception('\tCommandError: use "help" to see de available commands.')
                else:
                    print('\t> add "[description]" \n\t> update [id] "[description]" \n\t> delete [id] \n\t> ' \
                    'mark in-progress/mark-done [id] \n\t> list *empty*/done/todo/in-progress' \
                    '\n\t> exit\n')

            elif(lst_command[0] == "exit"):
                if(len(lst_command) > 1):
                    raise Exception('\tCommandError: use "help" to see de available commands.')
                else:
                    print("All data has been saved. Bye!")
                    end = True
            else:
                raise Exception('\tCommandError: use "help" to see de available commands.')
        except Exception as e:
            print(e)

if __name__ == "__main__":
    program()