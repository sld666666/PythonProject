

class IPage:
    def analysis(self, soup, nextPages):
        raise NotImplementedError( "Should have implemented this" )

    def getKeyword(self):
        raise NotImplementedError( "Should have implemented this" )