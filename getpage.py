#!/usr/bin/python
# -*- coding: utf-8 -*-

# Here are imports, do not worry about them
#import setpath
import urllib
import urlparse
from bs4 import BeautifulSoup
from json import loads
from urllib import urlopen, urlencode, unquote
from urlparse import urldefrag

# optional helper functions should be written here
cache = {}

def getJSON(page):
	params = urlencode({
		'format': 'json', # TODO: complete this
		'action': 'parse', # TODO: complete this
		'prop': 'text', # TODO: complete this	
		'redirects': 'true', # TODO: complete this
		'page': page.encode('utf-8')})
	API = "http://en.wikipedia.org/w/api.php" # TODO: change this
	response = urlopen(API + "?" + params)
	return response.read().decode('utf-8')

def getRawPage(page):
	parsed = loads(getJSON(page))
	try:
		title = parsed["parse"]["title"]# TODO: replace this
		content = parsed["parse"]["text"]["*"]# TODO: replace this
		return title, content
	except KeyError:
		# page does not exist
		return None, None

def getPage(page):
	if (page in cache):
		return cache[page]	
	title , html = getRawPage(page)
	links = []
	if title == None:
		return None, []
	soup = BeautifulSoup(html)
	paragraphs = soup.find_all("p",recursive=False)
	for p in paragraphs:
		for a in p.find_all("a"):
			link = a.get('href')
			if link.startswith("/wiki"):	    
				link = urlparse.urldefrag(link[6:])
				link = urllib.unquote(link[0]).replace(u"_", " ").encode("utf-8")
				if not link in links:
					links.append(link)
	cache[page] = title,links[:10]
	return cache[page]
 

if __name__ == '__main__':
	# This code is executed when running the file.
	print("It works!")

	# here are things that you could write here to test your functions:
	print getPage("phylosophy")
	print getPage("phylosophy")
	print getPage("phylosophy")
	print getPage("phylosophy")
	# print(getJSON("phylosophy"))
	# print(getRawPage("User:A3_nm/COMASIC"))
	# print(getRawPage("History"))

