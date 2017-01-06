import network.IPage as IP
import utils.html2text
import os
import codecs

class OnePagePage(IP.IPage):

    def __init__(self):
        pass

    def analysis(self, soup, nextPages):
        content = soup.find('div', {'class' : 'post'})
        category = self.getCategory(soup)
        date = self.getPostDate(soup)
        title = self.getTitle(soup)

        html2Text = utils.html2text.HTML2Text()
        result = html2Text.handle(str(content))

        result += "##备注 \n @post in:" + date
        self._write(result, title)
    def getKeyword(self):
        return ['/p/','/archive/']

    def _reverser(self, title):
        title = title.strip()
        title = title.replace(':', '')
        title = title.replace('/', '')
        title = title.replace('>', '')
        return title

    def _write(self, content, title):
        folderName = os.path.relpath(".","..")
        if folderName != 'sld_blogs':
            os.chdir('sld_blogs')

        file = codecs.open(self._reverser(title)+".md", 'w', 'utf-8')
        file.write(content)
        file.close()
        print('do write')

    def getTitle(self, soup):
        content = soup.find('h1', {'class' : 'postTitle'})
        return content.text

    def getCategory(self, soup):
        try:
            category = soup.find('div', {'id' : 'BlogPostCategory'})['href'].text
            return category
        except:
            return  None
    def getPostDate(self, soup):
        try:
            date =soup.find('span', {'id': 'post-date'}).text
            return  date
        except:
            return None