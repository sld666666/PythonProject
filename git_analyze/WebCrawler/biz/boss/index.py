
import logging
import WebCrawler.network.HttpUrlContentFetcher as  hcf

charPageUrl = r"https://www.zhipin.com/chat/im?mu=chat"

def initLog():
    logging.basicConfig(
        filename='boss.log',
        level=logging.DEBUG
    )


def paserCharPage() :
    hcf.HttpUrlContentFetcher().fetcher(charPageUrl)


if __name__ == "main":
    initLog()