import AoCparse
from itertools import groupby
import re

def getdecision(s):
    d ={}
    print(s)
    possibles = s[0].split(",")
    for p in possibles:
        if "}" in p:
            p = p[:-1]
        if ":" in p:
            condacont = p.split(":")
            d.update({condacont[0]: condacont[1]})
        else:
            d.update({None:p})
    return d.copy()

def getparts(ps):
    d = {}
    p = ps.split(",")
    for i in p:
        var = re.findall(r"[xmas]",i)
        amount = re.findall(r"\d+",i)
        print(f"v{var[0]}, a {amount[0]}m {i}")
        d.update({var[0]: int(amount[0])})
    return d.copy()

def process(workflow, part):
    print(workflow)
    conditions = workflow.keys()
    result = None
    for i in conditions:
        if i == None:
            return workflow.get(None)
        else:
            number = int(re.findall("\d+",i)[0])  
            if "<" in i:
                if "x" in i:
                    if part.get("x",0) < number:
                        return workflow.get(i)
                if "m" in i:
                    if part.get("m",0) < number:
                        return workflow.get(i)
                if "a" in i:
                    if part.get("a",0) < number:
                        return workflow.get(i)
                if "s" in i:
                    if part.get("s",0) < number:
                        return workflow.get(i)
            elif ">" in i:
                if "x" in i:
                    if part.get("x",0) > number:
                        return workflow.get(i)
                if "m" in i:
                    if part.get("m",0) > number:
                        return workflow.get(i)
                if "a" in i:
                    if part.get("a",0) > number:
                        return workflow.get(i)
                if "s" in i:
                    if part.get("s",0) > number:
                        return workflow.get(i)
    return None

input = AoCparse.getinput(19)
# read in the input and set everything up
mapping = [list(g) for k, g in groupby(input, key=bool) if k]
workflowsstrings = mapping[0]
partsstr = mapping[1]
parts = []
for part in partsstr:
    parts.append(getparts(part))
workflows ={}
for w in workflowsstrings:
    key = re.findall("^[a-z]+", w)
    value = getdecision(re.findall("{.+}", w))
    if key and value:
        workflows.update({key[0]:value})
accepted = []
rejected = []
nextw = "in"
result = 0
# start the processing 
for p in parts:
    while nextw != "A" and nextw != "R":
        nextw = process(workflows.get(nextw), p)
        if nextw == "A":
            accepted.append(p)
        if nextw == "R":
            rejected.append(p)
    print(f" part {p}")
    nextw ="in"

print(accepted)     
for a in accepted:
    result += sum(a.values())
print(result)