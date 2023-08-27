import random


class RPS():

    win = {"rock":"scissors", "scissors":"paper", "paper":"rock"}
    play = ("rock", "paper", "scissors")
    
    def __init__(self):
        self.score = {"win":0, "lose":0}
        self.input = "help"


    def pcaction(self):
        self.pc = random.choice(RPS.play)
        print(f"PC chose: {self.pc}")
        
    
    def action(self):
        self.input = input(f"Your move: ").lower()
        if self.input in RPS.play:
            self.pcaction()
            self.whowon()
        elif self.input == "quit":
            return
        else:
            print("Welcome to Rock, Paper, Sciccors! To quit the game type quit, or make a play with rock, paper or scissors")



    def scorereset(self):
        self.score = {"win":0, "lose":0}
    
    
    def conditioncheck(self):
        if self.score["win"] == 3:
            print("You won, well done and the game is now reset")
            self.scorereset()
    
        elif self.score["lose"] == 3:
            print("You lost, boohoo game reset")
            self.scorereset()


    def whowon(self):
        if RPS.win[self.input] == self.pc:
            self.score["win"] += 1
            print("you won the round")
        elif RPS.win[self.pc] == self.input:
            self.score["lose"] +=1
            print("you lost the round")
        else:
            print("draw")
        print(f"Score is {self.score}")
        self.conditioncheck()


        

#


game = RPS()


while game.input != "quit":
    
    game.action()
    


