

import unittest
import logging

from WebCrawler.parser import Parser

class ParserTestor(unittest.TestCase):

    def setUp(self):
        self.parser = Parser.Parser()

    def testParser(self):
        content = '<html><head><title>Page title</title></head> ' \
                  '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.'\
                  '<p id="secondpara" align="blah">This is paragraph <b>two</b>.'\
                  '</html>'
        self.assertTrue(self.parser.parser(content))
