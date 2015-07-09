#!/usr/bin/env python

from bs4 import BeautifulSoup
import random
import requests
import string

BASE_URL = "http://www.imgur.com/"

def get_url_hash():
    counter = 0
    url_hash = ""
    while counter < 5:
        random_letter = random.choice(string.letters)
        url_hash += random_letter
        counter += 1
    return url_hash

def make_web_request(url):
    markup = requests.get(url)
    import ipdb; ipdb.set_trace()

if __name__ == "__main__":
    harsh = get_url_hash()
    make_web_request(BASE_URL + harsh)
