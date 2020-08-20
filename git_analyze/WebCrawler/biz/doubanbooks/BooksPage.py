
import network.IPage as IP

BaseTagUrl = 'https://book.douban.com/tag/'

class BooksPage(IP.IPage):

    def analysis(self, soup, nextUrls):

        tds = soup.findAll('td')
        tags = []
        for td in tds :
            content = td.find('a').text
            if None != content :
                tags.append(content)
                nextUrls.append(BaseTagUrl+content)

        return tags

    def getKeyword(self):
        return 'index-sorttags-all'