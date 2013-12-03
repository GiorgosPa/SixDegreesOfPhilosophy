#!/usr/bin/python
# -*- coding: utf-8 -*-

# Here are imports, do not worry about them
import setpath
from bs4 import BeautifulSoup
from json import loads
from urllib import urlopen, urlencode, unquote
from urlparse import urldefrag

# optional helper functions should be written here

def getJSON(page):
  params = urlencode({
    'key1': 'value1', # TODO: complete this
    'key2': 'value2', # TODO: complete this
    'key3': 'value3', # TODO: complete this
    'page': page.encode('utf-8')})
  API = "http://example.com/apiurl" # TODO: change this
  response = urlopen(API + "?" + params)
  return response.read().decode('utf-8')

def getRawPage(page):
  parsed = loads(getJSON(page))
  try:
    title = "FIXME" # TODO: replace this
    content = "FIXME" # TODO: replace this
    return title, content
  except KeyError:
    # page does not exist
    return None, None

def getPage(page):
  pass # TODO write this

if __name__ == '__main__':
  # This code is executed when running the file.
  print("It works!")
  
  # here are things that you could write here to test your functions:
  # print(getJSON("User:A3_nm/COMASIC"))
  # print(getRawPage("User:A3_nm/COMASIC"))
  # print(getRawPage("History"))

