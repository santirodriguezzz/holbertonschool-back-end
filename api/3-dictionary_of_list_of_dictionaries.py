#!/usr/bin/python3
"""Python script to export data in the JSON format"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    user_request = requests.get(
        'http://jsonplaceholder.typicode.com/users/').json()
    todos_req = requests.get(
        'http://jsonplaceholder.typicode.com/todos').json()
    dic = {}
    for u in user_request:
        uid = u.get('id')
        name = u.get('username')
        dic[uid] = []
        for i in todos_req:
            aux = {}
            if i.get('userId') == int(uid):
                aux['task'] = i.get('title')
                aux['completed'] = i.get('completed')
                aux['username'] = name
                dic[uid].append(aux)

    with open("todo_all_employees.json", "w", encoding='utf-8') as f:
        json.dump(dic, f)
