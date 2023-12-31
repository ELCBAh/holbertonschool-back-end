#!/usr/bin/python3
"""Lists all tasks from a given employee ID."""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    completed = [todo for todo in todos if todo.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
                                                          len(completed),
                                                          len(todos)))
    print("\n".join(["\t {}".format(todo.get("title")) for todo in completed]))
