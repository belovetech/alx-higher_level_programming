#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import sys
import requests

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    auth = requests.auth.HTTPBasicAuth(username, password)
    url = 'https://api.github.com/user'

    res = requests.post(url, auth=auth)
    res = res.json()
    print(res.get('id'))
