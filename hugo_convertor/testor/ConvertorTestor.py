
import unittest
import Convertor

class ConvertorTestor(unittest.TestCase):
    #def __init__(self):

    def setUp(self):
        self.convert = Convertor.Convertor()

    def testExcute(self):
         self.convert.excute("E:\green\hugo\hub_site\content\documents", "E:\green\hugo\hub_site\content\post\documents")