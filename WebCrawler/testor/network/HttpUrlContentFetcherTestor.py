
import  unittest
#import network.imp.HttpUrlContentFetcher
from network import HttpUrlContentFetcher


class HttpUrlContentFetcherTestor(unittest.TestCase):

    def setUp(self):
        self.contentFetcher = HttpUrlContentFetcher.HttpUrlContentFetcher()
        self.contentFetcher.setCodec('GBK')


    def testFetcher(self):
        print(str(self.contentFetcher.fetcher("http://www.hzfc.gov.cn/scxx/xmcx_more.php?page=4&cqid=&key=&select_type=")))