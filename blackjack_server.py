from socket import *
from blackjack_db import BlackjackGame
import threading

def serve_game(c):
        BlackjackGame(c).play()

        
if __name__ == "__main__":
	# Create IPv4 TCP socket
	s = socket(AF_INET, SOCK_STREAM)
        # Make socket re-usable before natural release
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) 
	# Bind to localhost:9000
	s.bind(("",9000))
	s.listen(5)
	while True:
		c,a = s.accept()
		# Handle client connection in a new thread. 
		t = threading.Thread(target=serve_game, args=(c,))
		t.start()
