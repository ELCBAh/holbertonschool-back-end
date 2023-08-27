#!/usr/bin/python3
"""Lists all tasks from a given employee ID JSON format dictionary."""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    with open("todo_all_employees.json", "w") as f:
        for user in users:
            todo = requests.get(url + "todos", params={"userId": user["id"]}).json()
            user["todos"] = todo
            f.write(json.dumps(user))
            f.write("\n")
