


class Player: # create a plyaer object 
  def __init__(self):#initialization the ovbects 
      self.name = ""
      self.symbol = ""

  def choose_name(self):
      while True:
          name = input("Enter your name (letters only): ")
          if name.isalpha():#check if the input is char of not 
              self.name = name
              break
          print("Invalid name. Please use letters only.")

  def choose_symbol(self):
      while True:
          symbol = input(f"{self.name}, choose your symbol (a single letter): ")
          if symbol.isalpha() and len(symbol) == 1: #check if the symbol is char and the lengh is one 
              self.symbol = symbol.upper() #transformation the char to the upper case 
              break
          print("Invalid symbol. Please choose a single letter.")

class Menu:#the minue for user 
  def display_main_menu(self):
      print("Welcome to my X-O game!")
      print("1. Start Game")
      print("2. Quit Game")
      choice = input("Enter your choice (1 or 2): ")
      return choice

  def display_endgame_menu(self):#ASK THE USER  TO RESTART THE GAME OR QUIT THE GAME 
      menu_text = """
Game Over!
1. Restart Game
2. Quit Game
Enter your choice (1 or 2): """
      choice = input(menu_text)
      return choice

class Board:
  def __init__(self):
      self.board = [str(i) for i in range(1, 10)]# Create a list from 1 to 9 

  def display_board(self): #create the board 
      for i in range(0, 9, 3):
          print("|".join(self.board[i:i+3]))
          if i < 6:
              print("-" * 5)

  def update_board(self, choice, symbol):#put the sympol thet player choose it in the right location  
      if self.is_valid_move(choice):
          self.board[choice - 1] = symbol
          return True
      return False

  def is_valid_move(self, choice):#check if the location is valid or not 
      return self.board[choice - 1].isdigit()

  def reset_board(self):#تعيد تعين اللوحة الى حالتها الرئيسة 
      self.board = [str(i) for i in range(1, 10)]

  def check_win(self, symbol):#chesk if the plyer win 
      win_conditions = [
          [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
          [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
          [0, 4, 8], [2, 4, 6]              # Diagonals
      ]
      for condition in win_conditions:
          if all(self.board[i] == symbol for i in condition):
              return True
      return False

  def is_draw(self):#التاكد من ان النتيجة تعادل ام لا 
      return all(not cell.isdigit() for cell in self.board)

class Game:
  def __init__(self):
      self.players = [Player(), Player()]
      self.board = Board()
      self.menu = Menu()
      self.current_player_index = 0

  def start_game(self):#show the main minue and ask the user to start a game or quit 
      choice = self.menu.display_main_menu()
      if choice == "1":
          self.setup_players()
          self.play_game()
      else:
          self.quit_game()

  def setup_players(self):#ask the player to add his name and sympol
      for number, player in enumerate(self.players, start=1):
          print(f"Player {number}, enter your details:")
          player.choose_name()
          player.choose_symbol()
          print("-" * 20)

  def play_game(self):#manage the game and ask the user to choose location in the boord  and also chesk if the player win or draw 
      self.board.reset_board()
      game_over = False

      while not game_over:
          self.board.display_board()
          current_player = self.players[self.current_player_index]
          move = int(input(f"{current_player.name}'s turn ({current_player.symbol}). Choose a position (1-9): "))
          if self.board.update_board(move, current_player.symbol):
              if self.board.check_win(current_player.symbol):
                  self.board.display_board()
                  print(f"Congratulations, {current_player.name}! You win!")
                  game_over = True
              elif self.board.is_draw():
                  self.board.display_board()
                  print("It's a draw!")
                  game_over = True
              else:
                  self.current_player_index = 1 - self.current_player_index
          else:
              print("Invalid move. Try again.")

      end_choice = self.menu.display_endgame_menu()
      if end_choice == '1':
          self.play_game()
      else:
          self.quit_game()

  def quit_game(self):
      print("Thanks for playing!")

if __name__ == "__main__":#يستخدم هذا الجزء لتشيغل اللعبة وعندما يتم تشغيل الملف ينشئ كائن "game ويبدا اللعب "
  game = Game()
  game.start_game()
