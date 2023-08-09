#!/usr/bin/python3
"""
This script returns information about an employee's TODO list progress.
"""

import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = requests.get(url)
    todos = response.json()
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user_response = requests.get(user_url)
    user = user_response.json()
    done_tasks = [task for task in todos if task['completed']]
    print('Employee {} is done with tasks({}/{}):'.format(user['name'], len(done_tasks), len(todos)))
    for task in done_tasks:
        print('\t {}'.format(task['title']))

