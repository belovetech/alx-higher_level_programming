#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests

if __name__ == '__main__':

    try:
        data = {}
        if sys.argv[1]:
            data['q'] = sys.argv[1]
        else:
            data['q'] = ''
    except IndexError as err:
        pass

    res = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        resJSON = res.json()
        if not resJSON:
            print('No result')
        else:
            print('{[]} {}'.format(resJSON.get('id'), resJSON.get('name')))
    except requests.exceptions.JSONDecodeError as err:
        print('Not a valid JSON')
