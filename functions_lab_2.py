tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]


# As a user, to manage my task list I would like a program that allows me to:


#print a list of uncompleted tasks

def uncompleted_tasks(list):
    uncompleted_list = []
    for task in list:
        if task["completed"] == False:
            uncompleted_list.append(task)

    return uncompleted_list

print(uncompleted_tasks(tasks))


#print a list of completed tasks

def completed_tasks(list):
    completed_list = []
    for task in list:
        if task["completed"]==True:
            completed_list.append(task)

    return completed_list

print(completed_tasks(tasks))


#print a list of all task descriptions

def task_descriptions(list):
    description_list = []
    for task in list:
        description_list.append(task["description"])

    return description_list

print(task_descriptions(tasks))
      

#print a list of tasks where time_taken is at least a given time

def tasks_longer_than(list, time):
    task_list = []
    for task in list:
        if task ["time_taken"] >= time:
            task_list.append(task)

    return task_list

time = 30
print(tasks_longer_than(tasks, time))


# Print any task with a given description

def task_by_description (list, description):
    for task in list:
        if task["description"] == description:
            return task
        
    return "Not found"

print(task_by_description(tasks,"Feed Cat"))


# Given a description update that task to mark it as complete.

def mark_completed (list, description):
    for task in list:
        if task["description"] == description:
            task["completed"] = True

mark_completed(tasks, "Clean Windows")
print(tasks)

# Add a task to the list

def add_task (list, task_details):
    list.append(task_details)

add_task(tasks, {"description": "Take a Break", "completed": False, "time_taken": 50})
print(tasks)