import git_analyze.GitCmds as GitCmds
import git_analyze.DataCollector as GDC

test_path = "/Users/luodongshen/Documents/program/document"

dc = GDC.GitDataCollector()

def test_collect():
    rtn = dc.collect(test_path, '7-1-2019', '8-7-2019')
    print(rtn)




if __name__=='__main__':
    test_collect()
