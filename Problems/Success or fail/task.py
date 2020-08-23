"""Define a function check_success(url) that, given a URL, sends out a GET request and returns "Success" if it
succeeds and "Fail" otherwise.

"""
import requests


def check_success(url):
    resp = requests.get(url)
    if 200 <= resp.status_code < 400:  # check the value of status code
        return 'Success'
    else:
        return 'Fail'
