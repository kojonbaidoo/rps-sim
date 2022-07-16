class Game():
    def __init__(self, p1, p2, goal,verbose=True):
        self.p1 = p1
        self.p2 = p2
        self.verbose = verbose

        self.p1.setTitle(True)
        self.p2.setTitle(False)

        self.p1_points = 0
        self.p2_points = 0
        
        # number of points to win the game
        self.goal = goal

        self.plays = {self.p1.getTitle:[], self.p2.getTitle:[]}

        self.english = {1:'rock',2:'paper',3:'scissors'}
        self.outcomeEnglish = {None:'draw',True:'Player 1 wins',False:'Player 2 wins'}

    def play(self):
        p1_plays = []
        p2_plays = []
        
        while self.p1_points < self.goal and self.p2_points < self.goal:
            p1_move = self.p1.play(plays=p2_plays)
            p2_move = self.p2.play(plays=p1_plays)

            # print(p1_move)
            # print(f"{p2_move}\n")

            p1_plays.append(p1_move)
            p2_plays.append(p2_move)

            res = self.check(p1_move,p2_move)
            
            # UPDATE WITH 'match' implementation
            if res == None:
                continue
            elif res == True:
                self.p1_points+=1
            else:
                self.p2_points+=1
        
        self.plays[self.p1.getTitle].extend(p1_plays)
        self.plays[self.p2.getTitle].extend(p2_plays)
        
        return self.result()

    def check(self,p1_move, p2_move):
        # 1 = rock;
        # 2 = paper;
        # 3 = scissors;

        val = p1_move - p2_move
        # Update with 'match' implementation
        if val == 0:
            return None

        elif val == -1 or val == 2:
            return False

        elif val == 1 or val == -2:
            return True        

    def result(self):
        if self.p1_points > self.p2_points:
            if self.verbose: print("Player 1 wins")
            return True
        
        else:
            if self.verbose: print("Player 2 wins")
            return False

    def getPlays(self,player):
        return self.plays[player]
    
    def getP1Points(self):
        return self.p1_points

    def getP2Points(self):
        return self.p2_points

    def playthrough(self):
        print("GAME PLAYTHROUGH")
        for i in range(len(self.plays[self.p1.getTitle])):
            print(f"ROUND {i+1} \n\
                    Player 1:{self.english[self.plays[self.p1.getTitle][i]]} \n\
                    Player 2:{self.english[self.plays[self.p2.getTitle][i]]} \n\
                    Outcome:{self.outcomeEnglish[self.check(self.plays[self.p1.getTitle][i],self.plays[self.p2.getTitle][i])]}")
