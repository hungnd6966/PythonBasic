from __future__ import print_function
from lxml import html
import requests
import re

# Base URL for formulating a search
url = ".craigslist.org/search/tia?sort=date&query="

def get_posts(event_name, location):
	""" The get_posts function accesses the Craigslist page of search results for the given event and location.
	Returns a list of post information tuples, sorted by price.

	:param event_name: The keyword with which to search for the event. 
	:type event_name: String.
	:param location: The metropolitan area in which to search for the event.
	:type location: String.
	:returns: List of tuples of post information, sorted by ticket price. 
	:raises: None.
	"""
	ev = '+'.join(event_name.split())
	page = requests.get("http://" + str(location.lower()) + url + ev)


	# Create a tree out of the html content of the search results page	
	tree = html.fromstring(page.text)	

	posts_pages = get_pages(tree, location) 

	post_info = get_post_info(posts_pages)
	return sorted(post_info, key=lambda post: int(post[4]))

def get_post_info(posts_pages):
	""" The get_post_info loops through a list of post pages and scrapes the required information.
	It returns a list of tuples, each containing information found in the corresponding post. 

	:param posts_pages: A list of html trees for each of the search results. 
	:type posts_pages: lxml html tree.
	:returns: List of tuples of post information. 
	:raises: None.
	"""
	# Gather date, venue, # of tickets, price, and title
	post_info = []
	# Loop through the list of trees we created for each post
	for post in posts_pages: 
		# Grab the right-hand page attributes: date, venue, #tix
		info = post.xpath("//p[@class='attrgroup']/span//text()")
		# Grab the title which includes the price
                # Updated 3/14	
		title_price = post.xpath("//h2[@class='postingtitle']/span[@class='postingtitletext']/span[@id='titletextonly']/text()")
		try:
			# Try to break up the title into the user submitted title and
			# the price. If this fails, skip the post (it is probably an ad).
			#m = re.search(r"(.+) - \$([\d]+).*", title_price[0].strip('\n  '))
			#title = m.group(1)
			#price = m.group(2)
			price = post.xpath("//h2[@class='postingtitle']/span[@class='postingtitletext']/span[@class='price']/text()")
			price = price[0].strip('$')
			title = title_price[0]
		except Exception as e:
			continue 
		# Grab the date, venue, and number of tickets from info
		date = info[0]
		venue = ''
		tix = 1
		for i in range(len(info)):
			if info[i].startswith('venue'):
				venue = info[i+1]
			elif info[i].startswith('number available: '):
				tix = info[i+1]

		# Now, we have title, price, venue, number of tickets, and date
		# We need to analyze the post body for contextual price info		
		post_body = post.xpath("//section[@id='postingbody']/text()")
		
		# Try to find the phrases like "$50/", "$50 each", "$50 per", "$50 a"
		# which indicate the price per individual ticket.
		m = re.search(r"\$([\d]+)(/| each| per| a)", ''.join(post_body))
		
		# Try to find phrases like "both for $50", "pair for $50", "all for $50"
		# or "all 4 for $50", which indicate that the price is for a set of tickets. 
		m2 = re.search(r"(both|pair|all|all [\d]+) for \$([\d]+)", ''.join(post_body))

		if not m is None:
			# Individual ticket phrase found. 
			# Check to make sure it is less than listed price
			# and replace the price attribute.
			if int(m.group(1)) < int(price):
				price = m.group(1)
		elif not m2 is None:
			# Set ticket phrase found. Check that the price
			# is greater than the listed price and set 
			# the price to be the set price divided by number of tickets
			if int(m2.group(2) > int(price)):
				price = m2.group(2)
				price = str(int(price)/int(tix))		
		elif not price == '1':
			# Default -- divide listed price by listed number of tickets. 
			# The $1 case handles posts which list $1 as they want you to 
			# make an offer. 
			price = str(int(price)/int(tix))

		# Append tuple of post information
		post_info.append((date, venue, tix, title, price))
	# Return list of tuples of post information
	return post_info


def get_pages(root, location):
	# Grabs urls of individual posts from search page and creates an lxml tree out of the page. 
	# Returns a list of lxml trees for each post. 
	post_urls = root.xpath("//p[@class='row']/a[@class='i']/@href")
	trees = []
	for i in range(len(post_urls)):
		# Some URLs are not full URLs, so we need to construct them
		# Updated 3/14
		if not post_urls[i].startswith('http') and not post_urls[i].startswith('//'):
			post_urls[i] = "http://" + str(location) + ".craigslist.org" + post_urls[i]
		elif post_urls[i].startswith('//'):
			post_urls[i] = "http:"+post_urls[i]
		#print("the url formed is ", post_urls[i])
		# Request page, create a tree and append it to the list	
		page = requests.get(post_urls[i])
		tr = html.fromstring(page.text)
		trees.append(tr)
	return trees

if __name__ == "__main__":
	event_name = raw_input("Event to search for: ")
	location = raw_input("Location of event: ")
	results = get_posts(event_name, location)
	for r in results:
		print(r)
