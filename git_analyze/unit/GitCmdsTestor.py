import git_analyze.GitCmds as GitCmds


test_path = "/Users/luodongshen/Documents/program/document"

def test_getpipeoutput(cmds, quiet = False):
    return  -1

def test_getlogrange():
    print(GitCmds.getlogrange())


def test_getgitversion():
    print(GitCmds.getgitversion())

if __name__=='__main__':
    GitCmds.getpipeoutput(["cd "+ test_path])
    test_getgitversion()
    test_getlogrange()