#!/usr/bin/pythON3
""" Export data to csv format """
import requests
import sys
import csv

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("name")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        [writer.writerow(
                [user_id, username, t.get("completed"), t.get("title")])
         for t in todos]
