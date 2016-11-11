
import WebCrawler.network.interface.IPage as IP

class SubjectPage(IP.IPage):

    def analysis(self, soup, nextUrls):
        h1 = soup.findAll('h1')
        title = h1[0].text


    def getKeyword(self):
        return "/subject/"