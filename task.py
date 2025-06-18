from pathlib import Path
from datetime import datetime
import json

#saves the id counter for all tasks
id = None

#dict that saves if the file or the id has been checked before
checked_dict = {"file": False, "id": False}


#checks if the json file exists, if not it is created
def check_file():
    path = Path(".tasks.json")
    if not path.exists():
        path.touch()

    checked_dict["file"] = True

#returns the lists of tasks     
def get_tasks():
    try:
        with open(".tasks.json", "r") as json_tasks:
            tasks = json.load(json_tasks)

    except json.JSONDecodeError:
            tasks = []

    return tasks

#returns the position of the id coincidence
def get_coincidence(lst, id):
    if(len(lst) == 0): return -1

    pos = 0
    for dct in lst:
        if(dct["id"] == id):
            return pos
        
        pos += 1

    return -1

#get the last id number
def get_last_id():
    global id
    lst = get_tasks()
    if(len(lst) != 0):
        last_task = lst[len(lst) - 1]
        id = last_task["id"] + 1
    else:
        id = 1

    checked_dict["id"] = True

#checks if a task already exists
def exists_task(lst, description_task):
    if(len(lst) == 0): return False

    for dct in lst:
        if(dct["description"].lower() == description_task.lower()):
            return True
            
    return False

#creates a task and returns it
def create_task(description):
    global id
    new_task = {
        "id" : id,
        "description" : description,
        "status" : "todo",
        "createdAt" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    id += 1

    return new_task

#adds a task
def add_task(description):
    if(not checked_dict["file"]): check_file()
    if(not checked_dict["id"]): get_last_id()

    my_tasks = get_tasks()
    if(not exists_task(my_tasks, description)):
        new_task = create_task(description)
        my_tasks.append(new_task)

        with open (".tasks.json", "w") as json_tasks:
            json.dump(my_tasks, json_tasks, indent=4)

        print(f"\tThe task \"{description}\" was succesfully added! (ID:{id-1})")
    else:
        print(f"\tThe task \"{description}\" already exists!")

#update the description of a task by its id number
def update_task(id, description):
    if(not checked_dict["file"]): check_file()

    my_tasks = get_tasks()
    pos = get_coincidence(my_tasks, id)

    if(pos != -1): 
        my_tasks[pos]["description"] = description
        my_tasks[pos]["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open (".tasks.json", "w") as json_tasks:
            json.dump(my_tasks, json_tasks, indent=4)

        print(f"\tThe task with id \"{id}\" was succesfully updated!")
    else:
        print(f"\tThe task with id \"{id}\" does not exist!")

#updates the rest of the ids already assigned
def update_ids(lst, pos):
    global id 
    id -= 1

    if(len(lst) > 0):
        for i in range(pos, len(lst)):
            lst[i]["id"] = lst[i]["id"] - 1

#deletes a task by its id number
def delete_task(id):
    if(not checked_dict["file"]): check_file()
    if(not checked_dict["id"]): get_last_id()

    my_tasks = get_tasks()
    pos = get_coincidence(my_tasks, id)

    if(pos != -1): 
        del my_tasks[pos]
        update_ids(my_tasks, pos)

        with open (".tasks.json", "w") as json_tasks:
            json.dump(my_tasks, json_tasks, indent=4)

        print(f"\tThe task with id \"{id}\" was succesfully removed!")
    else:
        print(f"\tThe task with id \"{id}\" does not exist!")

#marks a task in progress by its id
def mark_in_progress_task(id):
    if(not checked_dict["file"]): check_file()

    my_tasks = get_tasks()
    pos = get_coincidence(my_tasks, id)

    if(pos != -1): 
        my_tasks[pos]["status"] = "in-progress"
        my_tasks[pos]["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open (".tasks.json", "w") as json_tasks:
            json.dump(my_tasks, json_tasks, indent=4)

        print(f"\tThe task with id \"{id}\" was succesfully marked in progress!")
    else:
        print(f"\tThe task with id \"{id}\" does not exist!")

#marks a task done by its id
def mark_done_task(id):
    if(not checked_dict["file"]): check_file()

    my_tasks = get_tasks()
    pos = get_coincidence(my_tasks, id)

    if(pos != -1): 
        my_tasks[pos]["status"] = "done"
        my_tasks[pos]["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open (".tasks.json", "w") as json_tasks:
            json.dump(my_tasks, json_tasks, indent=4)

        print(f"\tThe task with id \"{id}\" was succesfully marked done!")
    else:
        print(f"\tThe task with id \"{id}\" does not exist!")

#lists all tasks
def list_all_tasks():
    if(not checked_dict["file"]): check_file()

    my_tasks = get_tasks()

    if(len(my_tasks) == 0):
        print(f'\tThere are no tasks added yet.')

    else:
        for dct in my_tasks:
            print(f'\tThe task "{dct['description']}" has id "{dct['id']}" and its status is "{dct['status']}".')

#lists by status the tasks
def list_by_status_tasks(status):
    if(not checked_dict["file"]): check_file()

    my_tasks = get_tasks()
    exist_tasks = False

    if(len(my_tasks) == 0):
        print(f'\tThere are no tasks added yet.')
    
    else:
        for dct in my_tasks:
            if(dct['status'] == status):
                if(not exist_tasks): exist_tasks = True
                print(f'\tThe task "{dct['description']}" has id "{dct['id']}".')

        if(not exist_tasks):
            print(f'\tThere are no tasks marked as {status}.')

if __name__ == "__main__":
    add_task("Buy groceries")
    add_task("help Marina")

    add_task("Clean up my room")
    add_task("This one does not exist")

    delete_task(1)