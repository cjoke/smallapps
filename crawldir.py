#!/usr/bin/env python
'''
This is a simple script generated by codeium.vim plugin in 
neovim. It crawls a directory and prints out the files in it.
This took about 1 min to generate. 
To run it, type: python crawldir.py path/to/directory
'''

import os
import sys

# create a directorycrawler class
class DirectoryCrawler:
    def __init__(self, directory):
        self.directory = directory

    def crawl(self):
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                print(os.path.join(root, file))


# create an object of the class

directory = DirectoryCrawler(sys.argv[1])

# call the crawl method

if __name__ == "__main__":
    directory.crawl()