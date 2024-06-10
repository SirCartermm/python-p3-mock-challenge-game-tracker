class Result:
    def __init__(self, score, player, game):
        self.score = score
        self.player = player
        self.game = game
        # Ensure the objects are of the correct type
        if not isinstance(player, Player):
            raise TypeError("Player must be of type Player")
        if not isinstance(game, Game):
            raise TypeError("Game must be of type Game")

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        if not isinstance(value, Player):
            raise TypeError("Player must be of type Player")
        self._player = value

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, value):
        if not isinstance(value, Game):
            raise TypeError("Game must be of type Game")
        self._game = value