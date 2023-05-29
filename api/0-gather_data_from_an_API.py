#!/usr/bin/python3
""" module for api """

from requests import get
from sys import argv


e_id = argv[-1]

user_info = get(f"https://jsonplaceholder.typicode.com/users/{e_id}").json()

e_name = user_info["name"]

tasks_info = get(f"https://jsonplaceholder.typicode.com/todos?userId={e_id}"
                 ).json()

completed = 0
not_completed = 0
list_of_c_tasks = []

for task in tasks_info:
    if task["completed"] == True:
        completed += 1
        list_of_c_tasks.append(task["title"])
    else:
        not_completed += 1

total_tasks = completed + not_completed

print(f"Employee {e_name} is done with tasks({completed}/{total_tasks}):")

for element in list_of_c_tasks:
    print(f"\t {element}")
