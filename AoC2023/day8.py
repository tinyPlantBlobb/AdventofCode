import AoCparse
import re
from itertools import groupby
def pt1(input):
    currentnode = "AAA"
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
        
    while currentnode != "ZZZ":
        for i in instructions:
            t = treedict.get(currentnode)
            counter += 1
            if i == "L":
                currentnode = t[0]
            else:
                currentnode = t[1]
                
    print(counter)
    
    
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
    print(currentnodes)
    counter = 0
    done = False
    
    # print(input)
    # print(instructions)
    # print(tree)
    
    # print(treedict)
        
    while not done:
        for i in instructions:
            counter += 1
            for j in currentnodes:
                n = j[0]
                t = treedict.get(n)
                if i == "L":
                    n = t[0]
                    j = list(n)
                else:
                    n = t[1]
                    j = list(n)
        for i in currentnode:
            if not re.match("..Z", i):
                continue
            else:
                done = True
    print(counter)
    
input = AoCparse.getinput(8)
pt1(input)
pt2(input)