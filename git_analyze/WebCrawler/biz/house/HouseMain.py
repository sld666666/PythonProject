
import os
import  sys
import datetime

parent = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
parent = os.path.abspath(os.path.join(parent, os.pardir))
sys.path.append(parent)
print(sys.path)

import biz.initialization as init
import biz.house.XmcxMorePage as XP
import logging


def begin(indexUrl, baseUrl):
    dbManager = init.getDbmanager('house')
    dbManager.setBaseUrl(baseUrl)

    dbManager.register(XP.XmcxMorePage())
    dbManager.init(indexUrl, str(datetime.date.today()))

    dbManager.excute(indexUrl, None)
    pass

if __name__=='__main__':
    init.initSys()
    init.initLog()
    logging.debug("begin")
    begin('http://www.hzfc.gov.cn/scxx/xmcx_more.php', 'http://www.hzfc.gov.cn')
    logging.debug("finished")