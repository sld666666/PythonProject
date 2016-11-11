
import  unittest
#import network.imp.HttpUrlContentFetcher
from network import HttpUrlContentFetcher


class HttpUrlContentFetcherTestor(unittest.TestCase):

    def setUp(self):
        self.contentFetcher = HttpUrlContentFetcher.HttpUrlContentFetcher()


    def testFetcher(self):
        print(str(self.contentFetcher.fetcher("https://www.douban.com/")))