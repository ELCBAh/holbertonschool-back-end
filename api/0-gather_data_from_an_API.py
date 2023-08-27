#!/usr/bin/python3
"""Lists all tasks from a given employee ID."""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos = "https://jsonplaceholder.typicode.com/todos/?userId={}".format(
        user_id)
    user_info = requests.get(user).json()
    user_name = user_info.get("username")
    todo_list = requests.get(todos).json()
    completed = [todo for todo in todo_list if todo.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(user_name,
                                                          len(completed),
                                                          len(todo_list)))
    for todo in completed:
        print("\t {}".format(todo.get("title")))
