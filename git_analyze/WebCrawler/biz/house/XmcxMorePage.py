import network.IPage as IP

class XmcxMorePage(IP.IPage):

    def __init__(self):
        pass

    def analysis(self, soup, nextPages):
        allTrs = soup.find('div', {'class' : 'policy01'}).findAll('tr')
        values = list()
        if None != allTrs:
            for tr in allTrs:
                tds = tr.findAll('td')
                if len(tds) == 4:
                    nextPages.append(self._getNextPages(tds))
                else:
                    values.append(self._getDict(tds))

        return  values

    def getKeyword(self):
        return 'xmcx_more'

    def _getDict(self, tds):
        rtn = {}
        for i in range(len(tds)):
            text = tds[i].text
            if 0==i:
                rtn["house_name"] = text
            elif 1 == i:
                rtn["ara"] = text
            elif 2 == i:
                rtn["developers"] = text
            elif 3 == i:
                rtn["sale_counts"] = text
            elif 4 == i:
                rtn["sale_size"] = text
            elif 5 == i:
                rtn["pre_price"] = text

        return rtn

    def _getNextPages(self, tds):
        hrefs = tds[2].findAll('a')
        for href in hrefs:
            if '后页' == href.text:
                return href['href']

        return None