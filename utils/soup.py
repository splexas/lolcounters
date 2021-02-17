from bs4 import BeautifulSoup
import requests


def soup_request(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    return soup