from card import *
import db_interface as db

class BlackjackGame:
    """ The Blackjack Game class defines an instance of a session
	with a user connected to the Blackjack server. Each instance
	may involve multiple games, with stats being recorded. 

	:param c: The socket object through which we communicate with 
                  the player. 
	:type c: socket obj. 

    """
    def __init__(self, c):
        self.sock = c
        self.win_count = 0
        self.game_count = 0

        self.sock.send("\nWelcome to the Blackjack server!\n\n")
        self.sock.send("What's your name? ")
        self.name = self.sock.recv(30).strip()

    def play(self):
	""" Allow the user to play multiple games in a row, tracking the game number and 
            displaying the number of games played each time. User may continue to play 
            by selecting "y" at the end of a game, or quit by selecting "n". 
 	"""
        while(1):
            self.sock.send("\n\n******* Game {} *******\n".format(str(self.game_count + 1)))
            self.init_game()
            self.play_game()
            self.game_count += 1
            self.sock.send("Play again? [y] or [n]: ")
            if self.sock.recv(5).strip() == "n":
                self.sock.send("Would you like to see a scoreboard? [y] or [n]: ")
                db.insert_score(self.name, self.win_count)
                if self.sock.recv(4)[0] == 'n':
                    self.sock.send("Goodbye!\n")
                else:
                    self.sock.send("The top 3 scorers:\n")
                    for s in db.top_scores():
                        self.sock.send("{}   {}\n".format(s[0], s[1]))
                    self.sock.send("Goodbye!\n")
                break
        self.sock.close()

    def init_game(self):
        self.deck = Deck()   # initialize deck of cards
        self.deck.shuffle()  # shuffle deck
        self.sock.send("You've played {} games and won {} games. \n".format(str(self.game_count), str(self.win_count)))
	# Create two hand objects for the player and the dealer, initially dealing 2 to the dealer and 1 to the player.  
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.deck.move_cards(self.player_hand, 1)
        self.deck.move_cards(self.dealer_hand, 2)

    def play_game(self):
        entry = "h"
        while entry == "h":
            self.deck.move_cards(self.player_hand, 1)
            self.sock.send("Dealer hand: <hidden>{}\n".format(self.dealer_hand.__str__(1)))
            self.sock.send("Player hand:{}\n".format(self.player_hand.__str__()))
            if self.check_end():
                return
            self.sock.send("Enter h to hit or s to stay: ")
            entry = self.sock.recv(5).strip()
	self.end_game()

    def check_end(self):
        d_values = self.dealer_hand.values()
        p_values = self.player_hand.values()

        if(d_values[0] == 21 or p_values[0] > 21):
            self.sock.send("Dealer wins!\n")
        elif(d_values[0]>21 or p_values[0] == 21):
            self.sock.send("You win!\n")
            self.win_count += 1
        else:
            return False
        return True
                        
    def end_game(self):
        d_hand_value = self.dealer_hand.values()
        while d_hand_value[-1] < 17:
            self.deck.move_cards(self.dealer_hand, 1)
            d_hand_value = self.dealer_hand.values()

        self.sock.send("Dealer hand:{}\n".format(self.dealer_hand.__str__()))
        self.sock.send("Player hand:{}\n".format(self.player_hand.__str__()))


        if self.check_end():
            return
	else:
            self.check_winner()

    def check_winner(self):
        dealer_max_val = 0
        player_max_val = 0
        for v in self.dealer_hand.values():
            if v > dealer_max_val and v <= 21:
                dealer_max_val = v
        for v in self.player_hand.values():
            if v > player_max_val and v <= 21:
                player_max_val = v
        if dealer_max_val > player_max_val:
            self.sock.send("Dealer wins!\n")
        elif player_max_val > dealer_max_val:
            self.sock.send("You win!\n")
            self.win_count += 1
        else:
            self.sock.send("Draw!\n")
