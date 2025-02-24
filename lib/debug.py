# lib/testing/debug.py
#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # You can add test instances here, e.g.:
    # author = Author("Carry Bradshaw")
    # magazine = Magazine("Vogue", "Fashion")
    # article = author.add_article(magazine, "How to wear a tutu with style")

    # don't remove this line, it's for debugging!
    ipdb.set_trace()