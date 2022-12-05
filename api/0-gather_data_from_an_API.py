#!/usr/bin/python3
"""Script to generete request using a given APIs"""
import requests
from sys import argv


if __name__ == '__main__':
    user_request = requests.get(
        'http://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json()
    todos_req = requests.get(
        'http://jsonplaceholder.typicode.com/todos').json()
    usr_todos_list = [x for x in todos_req if x.get(
        'userId') == int(argv[1])]
    user_completed_list = [
        x for x in usr_todos_list if x.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(
              user_request.get('name'),
              len(user_completed_list),
              len(usr_todos_list)))
    for task in user_completed_list:
        print("\t " + task.get('title'))
