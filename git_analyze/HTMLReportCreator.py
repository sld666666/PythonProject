import os
import datetime
import  git_analyze.config as cg

one_table_template = "    <dt>Group name</dt>\
                            <dd>{}</dd>\
                            <dt>Project name</dt>\
                            <dd>{}</dd>\
                            <table border=\"1\">\
                              {}\
                            </table>    \n"
table_one_head = "<tr>\
                <th>author</th>\
                <th>fileChanges</th>\
                <th>insertions</th>\
                <th>deletions</th>\
              </tr> \n"

table_one_line_template = "<tr>\
                            <th>{}</th>\
                            <th>{}</th>\
                            <th>{}</th>\
                            <th>{}</th>\
                          </tr> \n"

class HTMLReportCreator :

    def generate(self, startTime, endTime,  contents):
        print(contents)
        binarypath = os.path.dirname(os.path.abspath(__file__))
        f = open(binarypath + "/index_template.html", 'r')
        rtn = f.read()

        info = ""
        for content in contents:
            name = content["name"]
            group = content["group"]
            tableInfo = ""
            if  "content" in content:
                table = table_one_head
                for item in content["content"]:
                    table += self.generateOneItem(item)
                tableInfo = one_table_template.format(group,name, table)
            else:
                tableInfo = "zore updated"

            info += tableInfo

        result = rtn.format(startTime, endTime, datetime.datetime.now(), info)
        fo = open(binarypath + "/result.html", 'w', encoding = 'utf-8')
        fo.write(result)
        return  ""


    def generateOneItem(self, content):
        if cg.key_author_format not in content:
            return ""

        if cg.key_file_changesformat not in content:
            return  ""

        author = content[cg.key_author_format]
        fileChanges = content[cg.key_file_changesformat]
        insertions = 0
        if cg.key_insertions_format in content:
            insertions = content[cg.key_insertions_format]

        deletions = 0
        if cg.key_deletions_format in content:
            deletions = content[cg.key_deletions_format]

        return table_one_line_template.format(author, fileChanges, insertions, deletions)