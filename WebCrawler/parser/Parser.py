
import bs4
import logging

class Parser :

    def parser(self, content):
        soup = bs4.BeautifulSoup(content, from_encoding="utf-8")
        return  soup

