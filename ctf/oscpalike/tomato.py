import requests, sys, getopt
from bs4 import BeautifulSoup, Comment

def usage():
	print("TMT extract tool")

	print("insert ascii art\n")

	print("Usage: tomato.py -c -l <url>")
	print("-c --comments\t- extract all comments")
	print("-l --links\t- extract all links")
	print("-u --url\t- mandatory url target")
	print()
	
	print("Examples: ")
	print("tomato.py -c -l 192.168.1.10")
	print("tomato.py -c 192.168.1.10")
	print("tomato.py -l 192.168.1.10")

	sys.exit(0)

def get_comments(sopa):
	print("\n///////////////////////// COMMENTS /////////////////////////\n")
	for comments in sopa.find_all(text=lambda text:isinstance(text, Comment)):
		print(comments.extract())		

def get_links(sopa):
	print("\n///////////////////////// LINKS /////////////////////////\n")
	for tag in sopa.find_all(href=True):
		print(tag['href'])

def main():
	links = False
	comments = False
	target = ''
	
	try:
		opts, args = getopt.getopt(sys.argv[1:],"clhu:",["comments","links","help","url"])
	except getopt.GetoptError as err:
		print(str(err))
		usage()

	for o,a in opts:
		if o in ("-h","--help"):
			usage()

		elif o in ("-l","--links"):
			links = True

		elif o in("-c","--comments"):
			comments = True
		
		elif o in("-u","--url"):
			target  = a
		
		else:
			print("Invalid Option")
			usage()
	
	if target:
		try:
			r = requests.get(target).text
			sopa = BeautifulSoup(r,'lxml')
			
			if links:
				get_links(sopa)
	
			if comments:
				get_comments(sopa)
			
		except Exception as e:
			print("[-]erro: " + str(e))
			sys.exit(0)
	else:
		usage()			


main()