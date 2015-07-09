from bs4 import BeautifulSoup
import random
import requests
import string

def get_url_hash():
    counter = 0
    url_hash = ''
    while counter < 5:
        random_letter = random.choice(string.letters)
        url_hash += random_letter
        counter += 1
    return url_hash
