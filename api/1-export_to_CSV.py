#!/usr/bin/python3
"""Lists all tasks from a given employee ID in CSV format."""
import requests, sys, csv


if __name__ == "__main__":
    usr_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(usr_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": usr_id}).json()

    completed = [todo for todo in todos if todo.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
                                                          len(completed),
                                                          len(todos)))
    [print("\t {}".format(todo.get("title"))) for todo in completed]
