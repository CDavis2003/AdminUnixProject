import requests

URL = 'http://127.0.0.1:8080'

def get_data():
    url = URL + '/get_data'
    response = requests.get(url)
    return response.json()


def get_initial():
    url = URL + '/get_initial'

    response = requests.get(url)
    return response.json()