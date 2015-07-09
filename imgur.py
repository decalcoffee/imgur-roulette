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

def get_n_random_images(n):
    for i in range(n):
        response = requests.get(BASE_URL + get_url_hash())
        while response.status_code != 200:
            response = requests.get(BASE_URL + get_url_hash())
        print response

if __name__ == "__main__":
    get_n_random_images(10)
