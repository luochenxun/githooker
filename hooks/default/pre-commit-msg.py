#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys,subprocess
import os
import pickle
import base64
import re

''' ---------- Hook method ---------- '''
pCommitMessage = ''  # git commit message
pCommitTime = ''     # git commit time


# @param project:
#          {
#            "name":"projectName",  // the name of the project
#            "path":"/xx/xx/xx",    // the path of the project
#            "msgReg":"",           // the regular expression to match the commit message
#            "msgRegTips":"",       // the message to show by the invalid commit message
#          }
def hook(project):
    global pCommitMessage

    regStr = project.get("msgReg")
    if regStr:
        pattern = re.compile(regStr)
        matcher = pattern.match(pCommitMessage)
        if matcher:
            print matcher.group()
        else:
            if project.get("msgRegTips"): print project.get("msgRegTips")
            _failed()
    _pass()


''' ---------- Private methods ---------- '''

# init some global variables of git environment
def _initGitInfo():
    global pCommitMessage
    pCommitMessage = os.popen('git log -1 --pretty=format:"%s"').read()


def _pass():
    os._exit(0)

def _failed():
    os._exit(1)


def loadProject(obj_str):
  return pickle.loads(base64.decodestring(obj_str))

def main():
    _initGitInfo()
    hook(loadProject(sys.argv[1]))

if __name__ == "__main__":
    main()
