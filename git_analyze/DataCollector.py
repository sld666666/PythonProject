
import time
import os
import datetime
import pickle
import zlib
import re

import git_analyze.config as GC
import git_analyze.GitCmds as GCmd
import git_analyze.config as config

insertion_format = "insertion(+)"
insertions_format = "insertions(+)"
deletion_fromat = "deletion(-)"
deletions_fromat = "deletions(-)"
file_changed_fromat = " file changed"
files_changed_fromat = " files changed"



log_stat_template = 'git log {} --shortstat --after \'{}\' --before \'{}\''
class GitDataCollector:

    def create(self, dir, repository):
        rtn = GCmd.getpipeoutput(["git clone " + repository], dir)
        return rtn

    def collect(self, dir, start, end):
        # first update
        rtn = GCmd.getpipeoutput(["git pull"], dir)
        print(rtn)

        # then collector
        infos = self.getUpdateInfo(start, end, dir).split("commit ")

        contents = []
        for info in infos:
            contents.append(self.parserOneItem(info))

        print(contents)
        print(len(contents))
        contents =  self.generate(contents)
        print(len(contents))
        print(contents)
        return contents
    def getUpdateInfo(self, start, end, dir):
        rtn = ""
        branchs = GCmd.getpipeoutput(["git branch -r "], dir).split("\n")
        for branch in branchs :
            cmd = log_stat_template.format(branch, start, end)
            rtn +=   GCmd.getpipeoutput([cmd], dir)

        return rtn

    def generate(self, contents):
        rtns = []
        for content in contents:
            rtn = self.findByAuthor(rtns, content.get(config.key_author_format))
            if rtn is not None:
                if config.key_deletions_format in content:
                    if config.key_deletions_format in rtn :
                        deletions = rtn[config.key_deletions_format] + content[config.key_deletions_format]
                    else :
                        deletions =  content[config.key_deletions_format]
                    rtn[config.key_deletions_format] = deletions

                if config.key_file_changesformat in content:
                    if config.key_file_changesformat in rtn :
                        fileChangeds = rtn[config.key_file_changesformat] + content[config.key_file_changesformat]
                    else :
                        fileChangeds = content[config.key_file_changesformat]

                    rtn[config.key_file_changesformat] = fileChangeds

                if config.key_insertions_format in content:
                    if config.key_insertions_format in rtn:
                        insertions = rtn[config.key_insertions_format] + content[config.key_insertions_format]
                    else :
                        insertions = content[config.key_insertions_format]

                    rtn[config.key_insertions_format] = insertions
            else :
                rtns.append(content)

        return rtns

    def findByAuthor(self, items, author):
        for item in items :
            if  config.key_author_format in item and  author == item[config.key_author_format]:
                return item

        return None

    def parserOneItem(self, item):
        rtn = {}
        items = item.split("\n")
        if (len(item) < 3):
            return rtn

        commit = items[0]
        authorItem = self.getAuthor(items)
        if None == authorItem:
            return rtn

        author = authorItem.lstrip("Author : ")
        rtn = self.parserItemDetail(self.getDetailItem(items))
        rtn[config.key_commit_format] = commit
        rtn[config.key_author_format] = author
        return rtn
    def getAuthor(self, items):
        for item in items :
            if item.find("Author: ") >= 0:
                return item


    def getDetailItem(self, items):
        for item in items :
            if item.find(file_changed_fromat) > 0 or item.find(files_changed_fromat) > 0:
                return item

        return ""
    def parserItemDetail(self, item):
        if len(item) <= 0:
            return {}

        items = item.split(", ")
        if len(items) < 2:
            print("parserItemDetail error:" + item)
            return {}
        else:
            fileChanges = 0
            insertions = 0
            deletions = 0
            for i in range(0, len(items)):
                if items[i].find(insertion_format) > 0:
                    insertions = int(items[i].rstrip(insertion_format))
                elif items[i].find(insertions_format) > 0:
                    insertions = int(items[i].rstrip(insertions_format))
                elif items[i].find(deletion_fromat) > 0:
                    deletions = int(items[i].rstrip(deletion_fromat))
                elif items[i].find(deletions_fromat) > 0:
                    deletions = int(items[i].rstrip(deletions_fromat))
                elif items[i].find(file_changed_fromat) > 0:
                    fileChanges = int(items[i].rstrip(file_changed_fromat))
                elif items[i].find(files_changed_fromat) > 0:
                    fileChanges = int(items[i].rstrip(files_changed_fromat))
                else:
                    print("parserItemDetail not support type : "+ items[i])
            return {config.key_insertions_format:insertions,
                    config.key_deletions_format:deletions,
                    config.key_file_changesformat:fileChanges}
