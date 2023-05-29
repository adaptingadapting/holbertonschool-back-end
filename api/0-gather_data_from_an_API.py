#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
from requests import get
from sys import argv

if __name__ == "__main__":
    e_id = argv[-1]

    user_info = get(f"https://jsonplaceholder.typicode.com/users/{e_id}"
                    ).json()

    e_name = user_info["name"]

    tasks_in = get(f"https://jsonplaceholder.typicode.com/todos?userId={e_id}"
                   ).json()

    completed = 0
    not_completed = 0
    list_of_c_tasks = []

    for task in tasks_in:
        if task["completed"] is True:
            completed += 1
            list_of_c_tasks.append(task["title"])
        else:
            not_completed += 1
    total_tasks = completed + not_completed

    print("Employee {} is done with tasks({}/{}):"
          .format(e_name, completed, total_tasks))
    for element in list_of_c_tasks:
        print(f"\t {element}")
