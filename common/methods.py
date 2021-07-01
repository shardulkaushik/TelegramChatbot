import requests
import json


def hit_link(link):
    request = requests.get(link)
    return json.loads(request.content)


def build_url(link, **kwargs):
    return link + '?' + '&'.join([str(key) + '=' + str(kwargs[key]) for key in kwargs])