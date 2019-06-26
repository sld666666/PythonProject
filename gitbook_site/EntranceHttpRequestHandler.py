import http.server
import gitbook_site.Convertor as CT
import os
import _thread

TargetPath = "/Users/luodongshen/Documents/program/document"
GitSrcPath = "/Users/luodongshen/Documents/program/document"
HugeStatCommond = r'gitbook serve'
class EntranceHttpRequestHandler(http.server.CGIHTTPRequestHandler):

    def do_POST(self):
        print('begin')

        self.gitpull(GitSrcPath)

        self.stopGitbook()

        convert = CT.Convertor()
        convert.excute(TargetPath+"/SUMMARY.MD",TargetPath)
        self.startGitbook()
        print("finished")
        self.wfile.write(b"msg finished")


    def gitpull(self,  filePath):
        os.chdir(filePath)
        command = "git pull "
        os.system(command)

    def startGitbook(self):
        _thread.start_new_thread(self.doStartGitbook, ())

    def doStartGitbook(self):
        os.chdir(TargetPath)
        output = os.system(HugeStatCommond)
        print(output)
        print('sartHugo finished')

    def stopGitbook(self):
        command = 'kill -9 $(pidof gitbook)'
        os.system(command)
        print('stopHugo finished')
