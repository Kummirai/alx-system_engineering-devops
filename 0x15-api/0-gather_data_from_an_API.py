#!/usr/bin/python3
"""
Gathering information from an API
"""
import requests
from sys import argv


if __name__ == "__main__":
    Base_url = 'https://jsonplaceholder.typicode.com'
    """REST API url"""

    user = requests.get('{}/users/{}'.format(Base_url, argv[1])).json()
    todos = requests.get('\
            {}/todos'.format(Base_url), params={'userId': argv[1]}).json()

    total_tasks = len(todos)
    completed = 0
    completed_tasks = []

    for todo in todos:
        if todo['completed']:
            completed += 1
            completed_tasks.append(todo["title"])
    output = 'Employee {} is done with tasks \
            ({}/{}): '.format(user["name"], completed, total_tasks)

    print(output)
    for task in completed_tasks:
        print('\t {}'.format(task))
