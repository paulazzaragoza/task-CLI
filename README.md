# task-CLI
This project is a task tracker to track and manage your task. You can track what you need to do, what you have done, and what you are currently working on. This project is based on CLI, and the programming lenguage is Python.

The url this project is based on is: [roadmap backend projects - task tracker CLI](https://roadmap.sh/projects/task-tracker).

## requirements
The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to: 
* add, update, and delete tasks.
* mark a task as in progress or done.
* list all tasks.
* list all tasks that are done.
* list all tasks that are not done.
* list all tasks that are in progress.

> ⚠️ **Warning:** the JSON file should be created if it does not exist.

## command examples
**adding a new task**  
task-cli add "Buy groceries"  
Output: Task added successfully (ID: 1)  

**updating and deleting tasks**  
task-cli update 1 "Buy groceries and cook dinner"  
task-cli delete 1  

**marking a task as in progress or done**  
task-cli mark-in-progress 1  
task-cli mark-done 1  

**listing all tasks**  
task-cli list  

**listing tasks by status**  
task-cli list done  
task-cli list todo  
task-cli list in-progress  

## task properties
Each task should have the following properties: 
* id: a unique identifier for the task.  
* description: a short description of the task.  
* status: the status of the task.  
* createdAt: the date and time when the task was created.  
* updatedAt: the date and time when the task was last updated.  
