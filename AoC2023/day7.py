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
    result = sorted(list(l.items()),key=lambda x: x[1], reverse=True) 
    return result

def setkind(hand):
    handtype = highcard
    card = parseHand(hand[0])
    print(card)
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

def sorthand(x,y):
    x = x[0]
    y = y[0]
    print(x)
    print(y)
    if x == y:
        return 0
    elif x.isdigit() and y.isdigit():
        return int(x) - int(y)
    else: 
        for n in range(len(x)):
            if x[n]== "A":
                if y[n] == "A":
                    pass
                else:
                    return 1
            elif x[n]=="K":
                if y[n] == "A":
                    return -1
                elif y[n] == "K":
                    pass
                else: 
                    return 1                    
            elif x[n]== "Q":
                if y[n] == "A":
                    return -1
                elif y[n] == "K":
                    return -1
                elif y[n] == "Q":
                    pass 
                elif y[n] == "J":
                    return 1
                elif y[n] == "T":
                    return 1
                else: 
                    return 1
            elif x[n]== "J":
                if y[n] == "A":
                    return -1
                elif y[n] == "K":
                    return -1
                elif y[n] == "Q":
                    return -1
                elif y[n] == "J":
                    pass
                elif y[n] == "T":
                    return 1
                else: 
                    return 1
            elif x[n]== "T":
                if y[n] == "A":
                    return -1
                elif y[n] == "K":
                    return -1
                elif y[n] == "Q":
                    return -1 
                elif y[n] == "J":
                    return -1
                elif y[n] == "T":
                    pass
                else: 
                    return 1
            else: 
                if x[n].isdigit() and not y[n].isdigit():
                    return -1
                elif not x[n].isdigit() and y[n].isdigit():
                    return 1
                elif(int(x[n]) != int(y[n])):
                    return int(x[n]) - int(y[n])
                else: 
                    pass
            
    return 0

inp = AoCparse.getinput(7)
# list of touples the style of (cards, hand type, wager)
handwager = []

for i in inp:
    hands = i.split(" ")[0]
    wager = i.split(" ")[1]
    handwager.append((hands, "", (int(wager))))

print(handwager)
processedpt2 = []
for i in handwager:
    processedpt2.append(setkind(i))

processedpt2 =  sorted(processedpt2, key=functools.cmp_to_key(sorthand))
processedpt2 = sorted(processedpt2, key= lambda x:x[1], reverse=True)
r = 1
result = 0
for b in processedpt2:
    result += b[2]*r
    print(f"{r}, {b}, {b[2]*r}, {result}")
    r += 1
print(result)