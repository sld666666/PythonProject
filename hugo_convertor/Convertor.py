import os
import shutil
import codecs
import time

TargetPath = "/Users/luodongshen/Documents/program/hugo-site/content/post"
GitSrcPath = "/Users/luodongshen/Documents/program/document"

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

            tmpCategory = category
            if os.path.isdir(path):
                if len(tmpCategory) == 0:
                    tmpCategory = lists
                self.exuteInFolder(tag, tmpCategory, path)
            else:
                if len(tmpCategory) == 0 :
                    tmpCategory = tag
                if lists.endswith('.md'):
                    self.excuteAsFile(path, tag, tmpCategory, lists.replace(".md", ""))

    def excuteAsFile(self, filePath, tag, category, fileName):
        print(filePath)
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

if __name__ == '__main__':
        convertor =  Convertor()
        convertor.excute(GitSrcPath, TargetPath)