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

    def excute(self, summaryPath, targetPath):
        rtn = False
        if not self.folderManager.isFolderExist(targetPath):
            return False


        content = ""
        for item in os.listdir(targetPath):
            path = os.path.join(targetPath, item)

            if os.path.isdir(path):
                if self.isIngore(item):
                    continue

                content = content +  "* " + "[{}]({}/README.MD)".format(item, item)
                self.createReadMeFile(path)
                content += self.exuteInFolder(item, path, 0, "")
                content += "\n"

        self.writeSummary(summaryPath, content)
        rtn = True
        return  rtn

    def writeSummary(self, summaryPath, content):
        header = "# Summary \n \n* [Introduction](README.MD) \n"
        content = header +  content
        f = codecs.open(summaryPath, 'w', 'utf-8')
        f.write(content)
        f.close()

    def createReadMeFile(self, path):
        readMePath = path+"/README.MD"
        if os.path.exists(readMePath):
            return

        f = codecs.open(readMePath, 'w', 'utf-8')
        f.write("readMe")
        f.close()

    def isIngore(self, folderName):
        return folderName in [".git",  "node_modules", "_book", "README.MD"]

    def exuteInFolder(self, parentName, targetPath, depth, content):
        depth += 1

        for item in os.listdir(targetPath):
            if self.isIngore(item):
                continue

            path = os.path.join(targetPath, item)
            if os.path.isdir(path):
                content += "\n"
                path = os.path.join(targetPath, item)
                content = content + " "*depth + "* " + "[{}]({}/README.MD)".format(item, parentName + "/" + item)
                self.createReadMeFile(path)
                content = self.exuteInFolder(parentName + "/" + item, path, depth, content)
            else:
                if item.endswith('.md'):
                    content += "\n"
                    content = content + " "* (depth+1) + "* " + "[{}]({}/{})".format(item.replace(".md", ""), parentName,item)
        return content

if __name__=='__main__':
    convert =  Convertor()
    root = "/Users/luodongshen/Documents/program/document"
    summaryPath = root+"/SUMMARY.MD"
    convert.excute(summaryPath, root)
    print("done")