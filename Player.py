from random import randrange

class Player():
    def __init__(self,strat=1) -> None:
        self.strat = strat
        self.prev_play = []

    def setTitle(self,title):
        self.title = title

    def getTitle(self):
        return self.title

    def play(self,plays=[]):
        # Update with 'match' implementation
        if self.strat == 1:
            my_play = self.strat1()
        
        elif self.strat == 2:
            my_play = self.strat2(plays)
        
        elif self.strat == 3:
            my_play = self.strat3()
        
        elif self.strat == 4:
            my_play = self.strat4()

        else:
            my_play = self.strat1()

        self.prev_play.append(my_play)
        return my_play

    # Random
    def strat1(self):
        return randrange(1,4)

    # Playing the move that beats your opponents previous move
    def strat2(self,plays):
        if len(plays) == 0:
            return self.strat1()
        
        else:
            # Update with 'match' implementation
            if plays[-1] == 1: return 2
            elif plays[-1] == 2: return 3
            elif plays[-1] == 3: return 1
    
    def strat3(self):
        return 1

    # Play the move that beats your previous move
    def strat4(self):
        return self.strat2(self.prev_play)