import AoCparse

class flipflop:
    state = False
    def flip(self, input):
        if not input:
            return not state
class conjunction:
    previousinputs = []
    def __init__(self, connections):
        previousinputs = [False for i in connections]
    def conjunction(self, input, prevstate = False):
        if prevstate and input:
            return (input,False)
        else: 
            return (input,True)
    