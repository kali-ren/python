import requests
from bs4 import BeautifulSoup, Comment
import argparse

#initial foothold: extraction of comments and links.

def get_comments(soup):
	for comments in soup.find_all(text=lambda text:isinstance(text, Comment)):
		print(comments.extract())

def get_local(soup):
	[print(tag['href']) for tag in soup.find_all(href=True) if tag['href']  != '#']

def get_all(soup):
	[print(a['href']) for a in soup.find_all('a', href=True) if a['href'] != '#']
	

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('target',    	   help='pass the target: https://example.com, http://example.com')
	parser.add_argument('-c', '-comments', help='show comments',  action='store_true')
	parser.add_argument('-a', '-alinks',   help='show all links', action='store_true')
	parser.add_argument('-l', '-llinks',   help='show local links only', action='store_true')
	args = parser.parse_args()
	
	r 	   = requests.get(args.target).text
	soup   = BeautifulSoup(r, 'lxml')

	if args.c:
		print("\n///////////////////////// COMMENTS /////////////////////////\n")		
		get_comments(soup)

	if args.a:
		print("\n///////////////////////// LOCAL LINKS /////////////////////////\n")		
		get_all(soup)

	if args.l:
		print("\n///////////////////////// LINKS /////////////////////////\n")				
		get_local(soup)

main()
