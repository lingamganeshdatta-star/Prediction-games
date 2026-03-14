import random
import sys
class TruthOrDareGame:
    def  __init__(self,players):
        self.players=players
        self.truth_questions=["what is your biggest fear?",
                             "Have you never lied to your best friend?",
                             "what is a scret you have never told to anyone?",
                             "who was your first crush?",
                             "what is your biggest regret?"
            ]
        self.dare_questions=["do 10 pushups.",
                            "singa song loudly.",
                            "send a funny message to your friend.",
                            "dance for 30 secs.",
                            "speak in a funny accent for the next 2 rounds."
            ]
        self.current_player_index=0
    def get_truth(self):
            return random.choice(self.truth_questions)
    def get_dare(self):
            return random.choice(self.dare_questions)
    def play_turn(self):
        player=self.players[self.current_player_index]
        print(f"\n it's {player}'s turn")
        choice=input("choose truth or dare(or exit to quit);").strip().lower()
        if choice=="truth":
            print(f"\n truth for {player}: {self.get_truth()}")
        elif choice=="dare":
            print(f"\n dare for {player}: {self.get_dare()}")
        elif choice=="exit":
            print("\n thanks for playing good bye")
            sys.exit()
        else:
            print("\n invalid choice.Try again.")
        self.current_player_index=(self.current_player_index+1)%len(self.players)
    def start_game(self):
         print("\n welcome to the truth or dare game!")
         print("----------------------------")
         while True:
            self.play_turn()
def get_players():
    players=[]
    print("enter the player names and type done when finished:")
    while True:
        name=input("player name:").strip()
        if name.lower()=="done":
            break
        if name:
            players.append(name)
    if len(players)<2:
        print("At least 2 players are required to play teh truth or dare game.")
        return get_players()
    return players
if __name__=="__main__":
    player_list=get_players()
    game=TruthOrDareGame(player_list)
    game.start_game()
    
        
            






































            
