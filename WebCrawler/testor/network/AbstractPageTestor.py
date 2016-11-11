

import unittest
import WebCrawler.network.imp.AbstractPage as AP

class HttpUrlContentFetcher(unittest.TestCase) :

    def setUp(self):
        pass

    def testExcute(self):
        contentFetcher = AP.AbstractPage("https://book.douban.com/")
        self.assertTrue(contentFetcher.excute())