'''
This program implements the Pocket Beast game. The game is played by two players.
'''


import random

class Player():
    def __init__(self, index, health, beast):
        self.index = index
        self.beast = beast
        self.health = health
        self.rival = None
        self.action = None
        self.power = 0

    def print_health_info(self):
        print(f"{self.beast}'s health: {self.health}")

    def choose_action(self):
        self.action = "defence" if input(f"Player {self.index}, do you want to defend? (y/n): ") == "y" else "attack"

    def act(self):
        if self.action == "defence":
            self.defence()
        else:
            self.attack(6, 2)

    def defence(self):
        self.power = 0
        print("Defending!") 
        
    def attack(self, dice_type, dice_number):
        '''
        This function simulates an attack by rolling the dice and returning the total 
        unless the beast is defending then it does nothing
        '''
        self.power = 0
        for _ in range(dice_number):
            self.power += random.randint(1, dice_type)
        self.rival.health -= self.power  

    def print_attack_message(self):
        '''
        This function prints the attack message for the provided player
        '''
        print(f"{self.beast} attacks {self.rival.beast} for {self.power} damage")

class GameData():
    def __init__(self, player1, player2):
        self.players = [player1 , player2]
        player1.rival = player2
        player2.rival = player1

    def __iter__(self):
        return iter(self.players)
    
    def find_winner(self):
        winner = None
        for players in self:
            if players.health < 0:
                winner = players.rival
        return winner

    def has_no_winner(self):
        state = True
        if self.find_winner() is not None:
            state = False
        return state

def create_beasts():
    '''
    This function creates the beasts for the players.
    '''

    player_one_beast = input("Player 1, choose your beast: ")
    player_two_beast = input("Player 2, choose your beast: ")

    print("Player 1's beast is a " + player_one_beast)
    print("Player 2's beast is a " + player_two_beast)

    return GameData(Player(1, 50, player_one_beast), Player(2, 50, player_two_beast))

def play_game(gamedata):

    while gamedata.has_no_winner():
        [player.print_health_info() for player in gamedata]
        [player.choose_action() for player in gamedata]
        [player.act() for player in gamedata]
        [player.print_attack_message() for player in gamedata]

    return gamedata.find_winner()

def print_winner(winner):
    '''
    This function prints the winner of the game
    '''
    print(f"{winner.beast} wins!")


if __name__ == "__main__":
    print_winner(play_game(create_beasts()))