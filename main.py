from gameplay import DiamondsGame
from ui import UI

# Create a DiamondsGame instance with the desired number of players
num_players = 2  # You can change this according to your preference
game = DiamondsGame(num_players)

# Create a UI instance and pass the game instance to it
ui = UI(game)

# Run the game
ui.run()