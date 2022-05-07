"""
game
"""


class Game:
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("Help info of the game")

    @classmethod
    def show_top_score(cls):
        print(cls.top_score)

    def start_game(self, score):
        print(f"{self.player_name}'s game has started")
        if score > Game.top_score:
            Game.top_score = score


# main
Game.show_help()
Game.show_top_score()

# player 1 : John
game1 = Game("John")
game1.start_game(5)
Game.show_top_score()
game1.start_game(10)
Game.show_top_score()

# player 2 : Peter
game2 = Game("Peter")
game2.start_game(10)
Game.show_top_score()
game2.start_game(15)
Game.show_top_score()

