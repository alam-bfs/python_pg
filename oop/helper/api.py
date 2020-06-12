import requests


def get_status_code():
    req = requests.get('https://api.github.com/events')
    return req.status_code


def get_resp_data():
    resp = requests.get('https://api.github.com/events')
    return resp.text
