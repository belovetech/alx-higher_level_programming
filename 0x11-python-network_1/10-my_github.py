#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import sys
import requests

if __name__ == '__main__':
    # username = sys.argv[1]
    # password = sys.argv[2]
    # auth = requests.auth.HTTPBasicAuth(username, password)
    # url = 'https://api.github.com/user'

    # res = requests.post(url, auth=auth)
    # res_json = res.json()
    # print(res_json.get('id'))

    url = "https://api.github.com/user"
    response = requests.get(
        url, auth=requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    res_dict = response.json()
    print(res_dict.get('id'))
