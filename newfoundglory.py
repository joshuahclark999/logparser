#!/usr/bin/python3
import sys
import re
import os
import glob
import time
from collections import Counter


# Print all of the logs related to the IP address that appears most commonly between all the logs

def compareLogs(ip, file):
    filename = file.name.split("/")
    filename = filename[-1]
    lines = file.readlines()
    for line in lines:
        if ip in str(line):
            # if type(ip) == "NoneType":
            #     pass
            return(filename)

def ipCounter(f):
    ipList = []
    ipDict ={}
    ip = ""
    regex = r"[A-Z]*=([1-9]\d?\d?(\.\d{1,3}){2}\.\d{1,3},?)+|([1-9]\d?\d?(\.\d{1,3}){2}\.\d{1,3},?)+"
    for line in f:
        line = str(line)
        match = re.findall(regex, line)
        if match != None:
            for x in match:
                for y in x:
                    if len(y) > 7:
                        ipList.append(y)
    ipDict = Counter(ipList)
    ipDict = dict(sorted(ipDict.items(), key=lambda item: item[1]))
    return(ipDict)

def parseList(nameList):
    res = []
    for x in nameList:
        if x != None:
            print(x)

def main():
    path = sys.argv[1]
    ipList = {}
    nameList = []
    for f in glob.glob(path +"/**", recursive=True):
        if os.path.isdir(f):
            continue
        with open(f, 'rb') as file:
            # ipCounter(file)
            ipList = ipCounter(file)
    lastIp = list(ipList.keys())[-1]
    print("IP Found in the logs the most: " + lastIp)
    for f in glob.glob(path +"/**", recursive=True):
        if os.path.isdir(f):
            continue
        with open(f,'rb') as file:
            # nameList.append(compareLogs(lastIp, file))
            nameList.append(compareLogs(lastIp,file))
    parseList(nameList)
    
if __name__ == "__main__":
    main()