This is a script to download random images from imgur.com.

## Installation
1. `git clone git@github.com:violetlight/imgur-roulette.git && cd imgur-roulette`
2. `pip install -r requirements.txt`

## Usage
`./imgur.py -n <number_of_files> [-d <directory>]`

**-n** - Number of random images to download from Imgur.  
**-d (optional)** - Directory to save the images to. This is always treated as a relative path at the moment. If the specified
directory does not exist, it will be created. Defaults to `./images/`.
