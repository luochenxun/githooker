#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys,subprocess
import os
import pickle
import base64
import re
import collections
import json

''' ---------- Hook method ---------- '''
pCommitTime = ''     # git commit time


# @param project:
#          {
#            "name":"projectName",  // the name of the project
#            "path":"/xx/xx/xx",    // the path of the project
#            "msgReg":"",           // the regular expression to match the commit message
#            "msgRegTips":"",       // the message to show by the invalid commit message
#          }
def hook(project):
    None

''' ---------- Private methods ---------- '''

# init some global variables of git environment
def _initGitInfo():
    None

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
