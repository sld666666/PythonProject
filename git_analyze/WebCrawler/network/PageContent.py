

class PageContent:

    def __init__(self):
        self.pageContent = {'url': "", 'content': ""}


    def addUrl(self, url):
        self.pageContentp['url'] = url

    def getUrl(self):
        return  self.pageContent['url']


    def addContent(self, content):
        self.pageContent['content'] = content


    def getContent(self):
        return  self.pageContent['content']
