from pathlib import Path
from datetime import datetime
import json

#saves de id counter for all tasks
id = None

#dict for the different status for a task
status_dict = {"todo": 1, "in-progress": 2, "done": 3}

#checks if the json file exists, if not it is created
def check_file():
    path = Path(".tasks.json")
    if not path.exists():
        path.touch()

#returns the lists of tasks     
def get_tasks():
    try:
        with open(".tasks.json", "r") as json_tasks:
            tasks = json.load(json_tasks)

    except json.JSONDecodeError:
            tasks = []

    return tasks

#get the last id number
def get_last_id():
    global id
    lst = get_tasks()
    if(len(lst) != 0):
        last_task = lst[len(lst) - 1]
        id = last_task["id"] + 1
    else:
        id = 1



#checks if a task already exists
def exists_task(lst, description_task):
    for actual in lst:
        for key in actual.keys():
            if(key == "description" and actual["description"].lower() == description_task.lower()):
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
    check_file()
    get_last_id()
    my_tasks = get_tasks()

    if(not exists_task(my_tasks, description)):
        new_task = create_task(description)
        my_tasks.append(new_task)

        with open (".tasks.json", "w") as json_tasks:
            json.dump(my_tasks, json_tasks, indent=4)

        print(f"The task \"{description}\" was succesfully added! (ID:{id-1})")
    else:
        print(f"The task \"{description}\" already exists!")



if __name__ == "__main__":
    add_task("Buy groceries")
    add_task("help Marina")

    add_task("Clean up my room")
    add_task("This one does not exist")