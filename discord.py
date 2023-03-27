import requests


def send(msg):

    payload = {
        'content' : msg
    }

    header = {
        'authorization' : 'COLOCAR AUTHORIZATION'
    }

    r = requests.post("COLOCAR O LINK DA API", data = payload, headers = header)