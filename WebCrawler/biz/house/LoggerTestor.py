
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

    pass

if __name__=='__main__':
    init.initLog()
    logging.debug("test done")