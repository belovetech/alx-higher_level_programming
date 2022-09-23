#!/usr/bin/python3
"""Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response."""
import sys
import requests

if __name__ == '__main__':
    data = {'email': sys.argv2}
    bodyRes = requests.post(sys.argv[1], data=data)
    print(bodyRes.text)
