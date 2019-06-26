
import shutil
import  json
import  os
import sys
import filecmp


def isDiff(src, dst, commonFile):
    common = []
    common.append(commonFile)
    diff = filecmp.cmpfiles(src, dst, common)
    print(diff)
    return (diff[0] != commonFile)

def copyIfDif(src, dst):
    print("do copy#" + src)
    shutil.copy2(src, dst)

def copytree2(src, dst, symlinks=False, ignore=None, copy_function=copyIfDif,
              ignore_dangling_symlinks=False):
    names = os.listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()

    if not os.path.isdir(dst):
        os.makedirs(dst)

    errors = []
    for name in names:
        if name in ignored_names:
            continue

        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if os.path.islink(srcname):
                linkto = os.readlink(srcname)
                if symlinks:
                    # We can't just leave it to `copy_function` because legacy
                    # code with a custom `copy_function` may rely on copytree
                    # doing the right thing.
                    os.symlink(linkto, dstname)
                    shutil.copystat(srcname, dstname, follow_symlinks=not symlinks)
                else:
                    # ignore dangling symlink if the flag is on
                    if not os.path.exists(linkto) and ignore_dangling_symlinks:
                        continue
                    # otherwise let the copy occurs. copy2 will raise an error
                    if os.path.isdir(srcname):
                        copytree2(srcname, dstname, symlinks, ignore,
                                  copy_function)
                    else:
                        copy_function(srcname, dstname)
            elif os.path.isdir(srcname):
                copytree2(srcname, dstname, symlinks, ignore, copy_function)
            else:
                if not isDiff(src, dst, name):
                    continue
                # Will raise a SpecialFileError for unsupported file types
                copy_function(srcname, dstname)
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except shutil.Error as err:
            errors.extend(err.args[0])
        except OSError as why:
            errors.append((srcname, dstname, str(why)))
    try:
        shutil.copystat(src, dst)
    except OSError as why:
        # Copying file access times may fail on Windows
        if getattr(why, 'winerror', None) is None:
            errors.append((src, dst, str(why)))
    if errors:
        raise shutil.Error(errors)
    return dst

class CopyConfig:
    def __init__(self, name, source, target, ingores):
        self.name = name
        self.source = source
        self.target = target
        self.ingores = ingores

class BatchCopy:

    def __init__(self):
        self.ingores=[""]

    def copy (self, name) :
        copyConfig = self.getConfig(name)
        self.ingores = copyConfig.ingores
        copytree2(copyConfig.source, copyConfig.target, ignore = self.ignore)

    def ignore(self, src, name):
        return  self.ingores

    def getConfig(self, name):
        filepath = os.path.abspath('CopyConfig.json')
        file = open(filepath, "r")
        items = json.load(file)
        for item in  items:
            if item["name"] == name:
                file.close()
                print("get config#" + str(item))
                return  CopyConfig(name, item["source"], item["target"], item["ignores"])

        file.close()

        return CopyConfig(name, "", "", "")



if __name__=='__main__':
    name = "xplan"
    if  len(sys.argv)>1:
        name = sys.argv[1]
    print(name)
    batchCopy = BatchCopy()
    batchCopy.copy(name)
    print("success!")