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

def get_n_random_image_urls(n):
    urls = []
    for i in range(n):
        response = requests.get(BASE_URL + get_url_hash())
        while response.status_code != 200:
            response = requests.get(BASE_URL + get_url_hash())
        soup = BeautifulSoup(response.text, "html.parser")
        # image_box is a reference to a div that houses the image on the page
        image_box = soup.find("div", {"class" : "image textbox"})
        image_element = image_box.find("img")
        if image_element:
            urls.append(image_element.attrs["src"])
        else:
            # it's a video/moving image
            source_elements = image_box.findAll("source")
            webm_element = source_elements[0]
            urls.append(webm_element.attrs["src"])
    return urls

if __name__ == "__main__":
    print get_n_random_image_urls(10)
