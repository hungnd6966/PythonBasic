""" This module defines the parse_file function
    for analyzing a file of soccer team statistics. """


from __future__ import print_function
import sys

def parse_file(filename):
	"""The parse_file function opens football.csv in the local
	directory, parses the file and returns the name of the soccer
	team who has the minimum difference in goals scored and goals
	allowed.
	:returns: Team name (string), Minimum goal difference (integer)
	:raises: None.
        """
	# Open file and read attribute names
	f = open(filename, 'r')
	attr_names = f.readline().split(',')

	# Grab indeces of interesting attributes
	try:
		team_index = attr_names.index("Team")
		g_index = attr_names.index("Goals")
		g_a_index = attr_names.index("Goals Allowed")
	except Exception as e:
		print("Error: ", e)
		return "N/A", "N/A"	

	# Calculate goal diffs and map to team name
	goal_diffs = {}
	for line in f:
		line = line.split(',')
		goal_diffs[line[team_index]] = abs(int(line[g_index]) - int(line[g_a_index]))

	# Find min goal diff and corresponding team
	min_goal_diff = 1000
	for key, value in goal_diffs.iteritems():
		if value < min_goal_diff:
			team_name = key
			min_goal_diff = value
	
	return team_name, min_goal_diff

if __name__ == "__main__":
	team, goal_diff = parse_file(sys.argv[1])
	print(team + " has a minimum goal difference of", goal_diff)
