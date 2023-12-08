import AoCparse
import re
from itertools import groupby
import math
def pt1(input):
    currentnode = "NBA"
    treedict = {}
    counter = 0

    instructions = input[0]
    tree = input[2:]

    for i in tree:
        s = i.split('=')
        touple = s[1].split(", ")
        a = touple[0].split("(")[1]
        b = touple[1].split(")")[0]
        treedict.update({s[0].strip(): (a,b)})
        
    while not re.match("..Z", currentnode):
        for i in instructions:
            t = treedict.get(currentnode)
            counter += 1
            if i == "L":
                currentnode = t[0]
            else:
                currentnode = t[1]
                
    print(f"pt1: {counter}")
    
def pt2helper(instructions, treedict, start):
    currentnode = start
    counter = 0
        
    while not re.match("..Z", currentnode):
        for i in instructions:
            t = treedict.get(currentnode)
            counter += 1
            if i == "L":
                currentnode = t[0]
            else:
                currentnode = t[1]
    return counter
    
    
def pt2(inp):
    instructions = input[0]
    treedict = {}
    tree = input[2:]
    for i in tree:
        s = i.split('=')
        touple = s[1].split(", ")
        a = touple[0].split("(")[1]
        b = touple[1].split(")")[0]
        treedict.update({s[0].strip(): (a,b)})
        
    starts = treedict.keys()
    currentnode = [re.findall("..A *", start) for start in starts]
    currentnodes = list(filter(None, currentnode))
    doneparts = []
    result = 1
    for i in currentnodes:
        res = pt2helper(instructions, treedict, i[0])
        doneparts.append(res)
    result = math.lcm(*doneparts)
    print(f"pt2: {result}")

    
    
input = AoCparse.getinput(8)
pt1(input)
pt2(input)