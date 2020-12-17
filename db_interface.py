import sqlite3

def top_scores():
	# Returns top three highest winners
	conn = sqlite3.connect("highscores.sqlite")
	c = conn.cursor()
	c.execute("SELECT * FROM Scores ORDER BY wins DESC;")
	result_rows = c.fetchmany(3)
        conn.close()
	return result_rows

def insert_score(name, wins):
	# Inserts a name and score
	conn = sqlite3.connect("highscores.sqlite")
	c = conn.cursor()
	record = (name, wins)
	c.execute("INSERT INTO Scores VALUES (?, ?);", (name, wins))
	conn.commit()
	conn.close()	

if __name__ == "__main__":
	for s in top_scores():
		print s


