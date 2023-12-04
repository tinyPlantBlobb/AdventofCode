import AoCparse
cards = AoCparse.getinput(4)
result = 0
mapping= {}
for i in range(len(cards)):
    mapping[i] = 1


def gettotal(own, winning):
    total = 0
    for n in winning:
        if (n in own):
            total += 1
    return total


def pt1(total):
    if(total>0):
        return 2**(total-1)
    return 0
        
def pt2(cards):
    cardcount = 0
    for card in range(len(cards)):
        cardcount += mapping[card]
    return cardcount

def addnewcard(cardnr, total):
    print(f"card nrb: {cardnr}, cards won from this one: {total}, current amount of this card: {mapping.get(cardnr)}\n")
    if total > 1:
        
        for i in range(1,total+1): 
            
            newcrd = cardnr+i
            newval =  mapping.get(newcrd) + mapping.get(cardnr)
            mapping[newcrd] = newval
            print(f"added {mapping.get(cardnr)} cards to card {newcrd} from card {cardnr}")

    elif total == 1:
        newval =  mapping.get(cardnr+1) + mapping.get(cardnr)
        mapping[cardnr+1] = newval



# dict= {card number: (times this card exists, total winnings from this card)}
for card in enumerate(cards):
    numberlists = cards[card[0]].split(":")[1].strip()
    winning = list(filter(None, numberlists.split("|")[0].strip().split(" ")))
    own =  numberlists.split("|")[1].strip().split(" ")

    total = gettotal(own, winning)


    print(f"key: {card[0]}, value: {mapping[card[0]]}")

    
    addnewcard(card[0], total)
    result += pt1(total)
    print(mapping)


print(f"pt1 = {result}")
print(f"pt2 = {pt2(cards)}")

