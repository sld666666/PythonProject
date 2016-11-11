

class IPage:
    def analysis(self, soup, nextPageContent):
        raise NotImplementedError( "Should have implemented this" )

    def getKeyword(self):
        raise NotImplementedError( "Should have implemented this" )