import AoCparse

cards = AoCparse.getinput(4)

for card in cards:

    numberlists = card.split(":")[1].strip()
    winning = numberlists.split("|")[0].strip().split(" ")
    own =  numberlists.split("|")[1].strip().split(" ")
    print(winning)
    print(own)
