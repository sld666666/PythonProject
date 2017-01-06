

import network.IPage as IP
import logging

class IndexPage(IP.IPage):

    def __init__(self):
        pass

    def analysis(self, soup, nextPages):
        rtn = []
        try:
            posts = soup.find_all("div", {'class' : 'postTitle'})
            for post in posts:
                try :
                    postTitle = post.find('a').text
                    rtn.append(postTitle)
                    nextPages.append(post.find('a')['href'])
                except:
                    pass
        except Exception as e:
            logging.error(str(e))

        nextUrl = self.getBlogNextPageUrl(soup)
        if None != nextUrl:
            nextPages.append(nextUrl)
        return  rtn
    def getKeyword(self):
        return 'default.html'

    def getBlogNextPageUrl(self, soup):
        nextUrl = ''
        pager = soup.find('div', {'id':'nav_next_page'})
        if None == pager:
            pager = soup.find('div', {'class' : 'pager'})
        for item in pager:
            try:
                title = item.text
                if '下一页'== title:
                    nextUrl = item['href']
            except Exception as e:
                pass

        return nextUrl