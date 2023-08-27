#!/usr/bin/python3
"""Lists all tasks from a given employee ID."""
import requests
import sys
import json
import urllib


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    user_id = int(sys.argv[1])
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    user_response = requests.get(user_url)
    user_data = user_response.json()
    completed_tasks = 0
    total_tasks = 0
    count_tasks = 0
    employee_name = user_data.get("name")
    for todo in todos_data:
        if todo["userId"] == user_id:
            count_tasks += 1
            if todo["completed"] is True:
                completed_tasks += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, completed_tasks, count_tasks))
    for todo in todos_data:
        if todo["userId"] == user_id and todo["completed"] is True:
            print("\t {}".format(todo["title"]))
