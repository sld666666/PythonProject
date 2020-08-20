import  git_analyze.config as gcfg
import  git_analyze.DataCollector as dc
import  git_analyze.HTMLReportCreator as hrc
import  os

class AnalyzeManager :

    def __init__(self):
        self.gitDataCollerctor = dc.GitDataCollector()
        self.HTMLReportCreator = hrc.HTMLReportCreator()
        pass

    def excute(self, startTime, endTime):
        self.startTime = startTime
        self.endTime = endTime

        binarypath = os.path.dirname(os.path.abspath(__file__))
        binarypath += "/projects/"
        items =  gcfg.gitConfig["projects"]
        contents = []
        for item in items:
            content = {}
            content["content"] = self.doExcute(binarypath, item)
            content["name"] = item["name"]
            content["group"] = item["group"]
            contents.append(content)

        self.HTMLReportCreator.generate(self.startTime, self.endTime, contents)

    def doExcute(self, binarypath, item):
        gourpPath = binarypath +  item["group"]
        if not os.path.exists(gourpPath):
            os.mkdir(gourpPath)

        itemPath = gourpPath + "/" + item["name"]
        if not os.path.exists(itemPath):
            print("do clone {} : ".format(item["name"]) + self.gitDataCollerctor.create(gourpPath, item["git_path"]))

        return self.doCollect(itemPath)

    def doCollect(self, itemPath):
        content = self.gitDataCollerctor.collect(itemPath, self.startTime, self.endTime)
        return content