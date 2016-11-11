import logging

import network.IPage as IP


class TagsPage(IP.IPage):

    def analysis(self, soup, nextUrls):
        rtn = []
        subjectItems = soup.find_all('li', {'class' : 'subject-item'})
        if None == subjectItems:
            logging.error("#TagsPage.analysis subject-item not found")
        else:
            for subjectItem in subjectItems:
                a = subjectItem.findAll('a')[1]

                title = self.getTitle(a)
                score = self.getScore(subjectItem)

                if None != title and None != score:
                    tmp = {}
                    tmp['title'] = title
                    tmp['score'] = score
                    rtn.append(tmp)

        nextUrl = self.getNextUrl(soup)
        if None != nextUrl:
            nextUrls.append(nextUrl)
        return  rtn


    def getKeyword(self):
        return "/tag/"

    def getScore(self, subjectItem):
        try:
            score = subjectItem.find('span', {'class' : 'rating_nums'}).contents[0]
            return score
        except:
            return  None

    def getTitle(self, aNode):
        try :
            title = aNode['title']
            return title
        except:
            return  None

    def getNextUrl(self, soup):
        try:
             nextUrl = soup.find('span', {'class' : 'next'}).link['href']
             return nextUrl
        except:
             return None
