#!/usr/bin/env python

from bs4 import BeautifulSoup
import os.path
import random
import requests
import shutil
import string
from urlparse import urlparse

BASE_URL = "http://www.imgur.com/"

def get_url_hash():
    counter = 0
    url_hash = ""
    while counter < 5:
        random_letter = random.choice(string.letters)
        url_hash += random_letter
        counter += 1
    return url_hash

def get_file_name_from_url(url):
    parsed_url = urlparse(url)
    from os.path import splitext, basename
    filename, ext = splitext(basename(parsed_url.path))
    return filename, ext

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

def download_images_to_disk(urls):
    for i, url in enumerate(urls):
        # All the urls in the array have '//' prepended. Rolling with it.
        response = requests.get('http:' + url, stream=True)
        filename, ext = get_file_name_from_url(url)
        local_filepath = './images/{}{}'.format(filename, ext)
        if not os.path.exists(os.path.dirname(local_filepath)):
            os.makedirs(os.path.dirname(local_filepath))
        with open(local_filepath, 'wb') as f:
            for chunk in response:
                f.write(chunk)


if __name__ == "__main__":
    import argparse
    help_description = "Download random images from Imgur."
    arg_parser = argparse.ArgumentParser(description=help_description)
    arg_parser.add_argument("-n",
                            dest="number_of_files",
                            action="store",
                            type=int)

    args = arg_parser.parse_args()
    if not args.number_of_files:
        print "ERROR: Specify a number of files to download."
        print "Pass -h for help."
        import sys
        sys.exit()

    random_urls = get_n_random_image_urls(args.number_of_files)
    download_images_to_disk(random_urls)
