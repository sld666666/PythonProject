
import  unittest
#import WebCrawler.network.imp.HttpUrlContentFetcher
from WebCrawler.network.imp import HttpUrlContentFetcher

class HttpUrlContentFetcherTestor(unittest.TestCase):

    def setUp(self):
        self.contentFetcher = HttpUrlContentFetcher.HttpUrlContentFetcher()


    def testFetcher(self):
        print(str(self.contentFetcher.fetcher("https://www.douban.com/")))