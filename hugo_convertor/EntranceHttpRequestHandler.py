import http.server
import Convertor
import os
import _thread

TargetPath = "/root/root/site/content/post/blog"
GitSrcPath = "/root/root/site/blog"
HugeSitePath = "/root/root/site/"
HugeStatCommond = r'hugo server --buildDrafts -p 80 --bind 115.28.83.94 -b http://115.28.83.94/'
class EntranceHttpRequestHandler(http.server.CGIHTTPRequestHandler):

    def do_POST(self):
        print('begin')

        self.gitpull(GitSrcPath)

        self.stopHugo()

        convert = Convertor.Convertor()
        convert.excute(GitSrcPath,TargetPath)
        self.startHugo()
        print("finished")
        self.wfile.write(b"msg finished")


    def gitpull(self,  filePath):
        os.chdir(filePath)
        command = "git pull "
        os.system(command)

    def startHugo(self):
        _thread.start_new_thread(self.doStartHugo, ())

    def doStartHugo(self):
        os.chdir(HugeSitePath)
        output = os.system(HugeStatCommond)
        print(output)
        print('sartHugo finished')

    def stopHugo(self):
        command = 'kill -9 $(pidof hugo)'
        os.system(command)
        print('stopHugo finished')
