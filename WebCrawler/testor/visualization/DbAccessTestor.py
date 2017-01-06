import unittest
import  sys
import os

parent = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
parent = os.path.abspath(os.path.join(parent, os.pardir))
sys.path.append(parent)
print(sys.path)

from WebCrawler.visualization.DbAccess import DbAccess

class DbAccessTestor(unittest.TestCase):

    def setUp(self):
        self.dbAccess = DbAccess()


    def testGetUrlTree(self):
        rtn = self.dbAccess.getUrlTree()

        self.assertFalse(None == rtn)