import os
import shutil
import codecs
import time

class FolderManager :

    def isFolderExist(self, path):
        return os.path.isdir(path)

    def removeFolder(self, path):
        rtn = False
        if(self.isFolderExist(path)):
            shutil.rmtree(path)
            rtn = True

        return  rtn


class Convertor :
    def __init__(self):
        self.folderManager = FolderManager()
        self.template = "+++ \n" + \
                        "title = \"{0}\" \n" + \
                        "Tags = [\"{1}\"]\n" + \
                        "Categories = [\"{2}\"]\n" +\
                        "+++ \n \n"

        #"date = \"{3}\" \n" +\

    def excute(self, sourcePath, targetPath):
        rtn = False
        if not self.folderManager.isFolderExist(sourcePath):
            return False

        self.folderManager.removeFolder(targetPath)
        shutil.copytree(sourcePath, targetPath, ignore=self.ig_f)
        #self.folderManager.removeFolder(os.path.join(targetPath, ".git"))

        for lists in os.listdir(targetPath):
            path = os.path.join(targetPath, lists)

            if os.path.isdir(path):
                self.exuteInFolder(lists, "", path)

        rtn = True
        return  rtn

    def ig_f(self, dir, files):
        return [".git"]

    def exuteInFolder(self, tag, category, targetPath):
        for lists in os.listdir(targetPath):
            path = os.path.join(targetPath, lists)
            if len(category) == 0 :
                category = lists.replace(".md", "")

            if os.path.isdir(path):
                self.exuteInFolder(tag, category, path)
            else:
                self.excuteAsFile(path, tag, category, lists.replace(".md", ""))

    def excuteAsFile(self, filePath, tag, category, fileName):
        f = codecs.open(filePath,'r', 'utf-8')

        timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        prefix = self.template.format(fileName, tag, category)

        i = 0
        for line in f.readlines():
            if 0 == i :
                if line.find("+++") >= 0:
                    f.close()
                    return

            prefix += line
            i +=1

        f.close()

        f = codecs.open(filePath, 'w', 'utf-8')
        f.write(prefix)
        f.close()


