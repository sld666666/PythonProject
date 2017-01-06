
import  json
import os
def uploadFile(workspace, fileName):
    command = 'curl -vF myfile=@${0}/app/build/outputs/apk/beta/{1}   ' \
              'http://niuce.sqaproxy.souche.com/upload'.format(workspace, fileName)
    rtn = os.system(command)
    return  rtn

def getMd5(datas):
    input = json.loads(datas)
    print(input)
    return input["data"]["md5"]


if __name__=="__main__":
    datas = uploadFile("abc", "bbb")
    print(datas)
    print(getMd5(datas))


