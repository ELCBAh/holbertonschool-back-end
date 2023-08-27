#!/usr/bin/python3
"""Lists all tasks from a given employee ID in CSV format."""
import csv
import requests
import sys


if __name__ == "__main__":
    usr_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(usr_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": usr_id}).json()

    with open("{}.csv".format(usr_id), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([usr_id, username, task.get("completed"),
                             task.get("title")])
