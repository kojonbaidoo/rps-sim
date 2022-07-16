from Game import Game
from Player import Player

def main():
#    single_run(p1_strat=3,p2_strat=2)
    sim(100,p1_strat=4,p2_strat=1)

def single_run(p1_strat=1,p2_strat=1,verbose=True):
    kojo = Player(p1_strat)
    rohan = Player(p2_strat)
    deathBattle = Game(p1=kojo,p2=rohan,goal=5,verbose=verbose)

    res = deathBattle.play()
    # deathBattle.playthrough()

    return res

def sim(games,p1_strat=1,p2_strat=1):
    print(f"PARAMS:\n\
    Player 1 Strategy: {p1_strat}\n\
    Player 2 Strategy: {p2_strat}\n")
    p1_wins = 0
    p2_wins = 0

    for i in range(games):
        res = single_run(p1_strat=p1_strat,p2_strat=p2_strat,verbose=False)
        if res == True:
            p1_wins+=1
        else: p2_wins+=1
    
    p1_percent = (p1_wins/games)*100
    p2_percent = (p2_wins/games)*100

    print(f"Player 1 wins: {p1_percent}%\nPlayer 2 wins: {p2_percent}%")

if __name__=='__main__':
    main()