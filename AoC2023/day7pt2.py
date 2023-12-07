import AoCparse
import functools
fivekind = 0
fourkind = 1
fullhouse = 2
threekind = 3
twopair = 4
onepair= 5
highcard = 6

def parseHand(cards):
    card =""
    l = {}
    for c in cards: 
        amount = l.get(c, 0) +1
        l.update({c: amount})
        card = c
    j = l.get("J",0)
    l.update({"J":0})
    result = sorted(list(l.items()),key=lambda x: x[1], reverse=True)
    
    if j == 5:
        l.update({"J":5})
        result = list(l.items())
        return result
    elif j >=result[0][1] and result[0][0] == "J":
        j =  result[1][1] + j
    else: 
        j = result[0][1]+j
    result[0] = (result[0][0],j)
    return result

def setkind(hand):
    handtype = highcard
    card = parseHand(hand[0])
    if (card[0][1] == 5 ):
        handtype = fivekind
    elif (card[0][1] == 4):
        handtype = fourkind
    elif(card[0][1] == 3 and card[1][1]==2):
        handtype = fullhouse
    elif(card[0][1]== 3):
        handtype = threekind
    elif(card[0][1]==2 and card[1][1]==2):
        handtype = twopair
    elif(card[0][1]==2):
        handtype = onepair
    else:
        handtype = highcard 
    return (hand[0], handtype, hand[2])

def lookup(s):
    if s.isdigit():
        return int(s)
    else: 
        if s == 'A':
            return 14
        elif s == 'K':
            return 13
        elif s == 'Q':
            return 12
        elif s == 'J':
            return 1
        elif s == 'T':
            return 10

def sorthand(t1,t2):
    x = t1[0]
    y = t2[0]
    for n in range(len(x)):
        if x[n].isdigit() and y[n].isdigit():
            if x[n] == y[n]:
                continue
            else:
                return int(x[n]) - int(y[n])
        else:
            a = lookup(x[n])
            b = lookup(y[n])
            if (a == b):
                continue
            else:
                return a - b       
    return 0

inp = AoCparse.getinput(7)
# list of touples the style of (cards, hand type, wager)
handwager = []

for i in inp:
    hands = i.split(" ")[0]
    wager = i.split(" ")[1]
    handwager.append((hands, "", (int(wager))))

processedpt2 = []
for i in handwager:
    processedpt2.append(setkind(i))

processedpt2 =  sorted(processedpt2, key=functools.cmp_to_key(sorthand))
processedpt2 = sorted(processedpt2, key= lambda x:x[1], reverse=True)
r = 1
result = 0
for b in processedpt2:
    result += b[2]*r
    r += 1
print(result)
print("the result should be 250757288")