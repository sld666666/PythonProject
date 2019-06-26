
import os
import shutil
def bacthDelete(targetPath, schema, func):
    for lists in os.listdir(targetPath):
        path = os.path.join(targetPath, lists)
        func(schema, lists, path, bacthDelete)


def deleteByName(schema,inputName, path, callback):
    if os.path.isdir(path):
        if schema == inputName:
            shutil.rmtree(path)
            print("delete" + path)
        else:
            callback(path, schema, deleteByName)
    else:
        if schema == inputName:
            os.remove(path)
            print("delete" + path)

def removeFolder(self, path):
    rtn = False
    if (self.isFolderExist(path)):
        shutil.rmtree(path)
        rtn = True

    return rtn

def deleteBySize(maxSize,inputName, path, callback):
    if os.path.isdir(path):
        if inputName == ".git":
            return

        callback(path, maxSize, deleteBySize)
    else:
        size = os.path.getsize(path)
        if size > maxSize:
            os.remove(path)
            print("delete" + path + ":" + str(size/1024))

if __name__=='__main__':
    bacthDelete('/Users/luodongshen/Documents/program/backups/big-client', '.git', deleteByName)
    bacthDelete('/Users/luodongshen/Documents/program/backups/big-client', 1024*1024, deleteBySize)