import AoCparse
from itertools import groupby

seedsnmappings = AoCparse.getinput(5)

def extractmappings(l):
    mapped = {}
    for i in range(1, len(l)):
        split = l[i].split(" ")
        source = int(split[1])
        destination= int(split[0])
        step = int(split[2])
        mapped.update({(source, step):destination})
    return mapped.copy()

def mapseeds(seedrng, d):
    result = int(seedrng[0])
    seeds = d.keys()
    for s in seeds:
        if result in range(s[0], s[0]+s[1]):
            result = d.get(s) + (seed - s[0])
            return result
    return result
    
#def addin(base, nbr):
def turndicttolist(dic):
    l = []
    for d in dic.keys():
        l.append((d, d + dic.get(d)))
    # remove duplicates [seedss.append(item) for item in seeds if item not in seedss]
    sorted(l)
    return l.copy()


seedranges =seedsnmappings[0].split(":")[1].strip().split(" ")
seeds = []
mappings = [list(g) for k, g in groupby(seedsnmappings, key=bool) if k]
seedtosoil = extractmappings(mappings[1])
# dict with key = start value value = the range
seedrangedict={}
for i in range(0, len(seedranges),2):
    print(i)
    start=int(seedranges[i])
    end = start+int(seedranges[i+1])
    seedrangedict.update({start:int(seedranges[i+1])})

seeds = turndicttolist(seedrangedict)     

print(seeds)

seedtosoil = mappings[1]= extractmappings(mappings[1])
soiltofert = mappings[2]=extractmappings(mappings[2])
fertilizertowater= mappings[3]= extractmappings(mappings[3])
watertolight = mappings[4]= extractmappings(mappings[4])
lighttotemperature= mappings[5] = extractmappings(mappings[5])
temperaturetohumidity = mappings[6]= extractmappings(mappings[6])
humiditytolocation = mappings[7] = extractmappings(mappings[7])

# # d1 is the destination, d2 is the source 
# def mergedicts(d1, d2):
#     keys1 = d1.keys()
#     keys2 = d2.keys()
#     for key in keys2:
#         print()
    

# mergedicts(humiditytolocation,temperaturetohumidity)

# for i in range(1,len(seedsnmappings)):
location = 111111111111111111111111111111111111111111
for s in seeds:
    tmp = mapseeds(mapseeds(mapseeds(mapseeds(mapseeds(mapseeds(mapseeds(s, seedtosoil), soiltofert), fertilizertowater), watertolight), lighttotemperature), temperaturetohumidity), humiditytolocation)
    location = min(tmp, location)

print(seedtosoil)
print(soiltofert)
print(location)