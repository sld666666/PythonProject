import git_analyze.GitCmds as GitCmds
import git_analyze.HTMLReportCreator as HRC
import git_analyze.AnalyzeManager as AM

test_path = "/Users/luodongshen/Documents/program/document"

hrc = HRC.HTMLReportCreator()
am = AM.AnalyzeManager()

def test_generate():
    rtn = hrc.generate()
    print(rtn)

def test_excute():
    am.excute('8-1-2019','8-14-2019')


if __name__=='__main__':
    test_excute()
