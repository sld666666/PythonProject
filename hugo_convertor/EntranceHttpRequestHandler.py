import http.server
import Convertor
import os

class EntranceHttpRequestHandler(http.server.CGIHTTPRequestHandler):

    def do_POST(self):
        gitPath = "/root/root/site/blog"
        self.gitpull(gitPath)

        self.stopHugo()

        convert = Convertor.Convertor()
        convert.excute(gitPath,
                        "/root/root/site/content/post/blog")
        self.startHugo()
        print("finished")
        self.wfile.write(b"aabbcc")


    def gitpull(self,  filePath):
        os.chdir(filePath)

        #gitPath = "\"C:\\Program Files (x86)\\Git\\bin\\git.exe\""
        command = "git pull "
        os.system(command)

    def startHugo(self):
        os.chdir("E:\green\hugo\hub_site")
        os.popen(r'hugo server --buildDrafts -p 80 --bind 115.28.83.94 -b http://115.28.83.94/')

    def stopHugo(self):
        command = 'kill -9 $(pidof hugo)'
        os.system(command)
