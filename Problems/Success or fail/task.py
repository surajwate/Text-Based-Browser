import requests


def check_success(url):
    resp = requests.get(url)
    if 200 <= resp.status_code < 400:
        return 'Success'
    else:
        return 'Fail'
