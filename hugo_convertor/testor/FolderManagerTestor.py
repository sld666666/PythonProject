
import unittest
import Convertor
import  os

class FolderManagerTestor(unittest.TestCase):
    #def __init__(self):

    def setUp(self):
        self.folderManager = Convertor.FolderManager()

    def testIsFolderExist(self):
        targetPath= r"E:\green\hugo\hub_site\content\post\aaabbcc"
        rtn = self.folderManager.isFolderExist(targetPath)
        assert rtn == False

        targetPath= r"E:\green\hugo\hub_site\content\post\tmp"
        rtn = self.folderManager.isFolderExist(targetPath)
        self.assertTrue(rtn)

    def testRemoveFolder(self):
        targetPath= r"E:\green\hugo\hub_site\content\post\tmp1"
        os.mkdir(targetPath)
        rtn = self.folderManager.removeFolder(targetPath)
        assert rtn == True

