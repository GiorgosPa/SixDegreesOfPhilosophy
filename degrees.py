#!/usr/bin/python
# -*- coding: utf-8 -*-

# Here are imports, do not worry about them
#import setpath
from flask import Flask, render_template, session, request, g, redirect, url_for, flash
from getpage import getPage


app = Flask(__name__)

app.secret_key = "Any secret value"

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/new_game', methods=['POST'])
def new_game():
	title = request.form['title']
	session['article'] = title 
	session['score'] = 0
	return redirect("/game")
  

@app.route('/game', methods=['GET'])
def game():
	title = session['article']
	title,links = getPage(title)
	session['article'] = title
	if(title == "Philosophy" and session['score']!=0):
		flash("Congratulations You Won!!!","mes")
		return redirect("/")
	if not links:
		if session['score'] == 0:
			flash("The Requested Page Does Not Exists!!","error")
			return redirect("/")
		flash("You Lost The Game Because You Reached A Page With No Out-Links!!","mes")
		return redirect("/")
	return render_template('game.html', title = title, links = links)
  
@app.route('/move', methods=['POST'])
def move():
	previousPage = request.form['currentPage']
	t , links = getPage(previousPage)
	if previousPage!= session['article']:
		flash("Your Move Was Ignored Because The Game Was Progressed In A Different Window!!","error")
		return redirect("/game")
	title = request.form['choice']
	if not title in links:
		flash("Illegal Move!!","error")
		return redirect("/game")
	score = session['score']
	session['score'] = score + 1
	session['article'] = title   
	return redirect("/game")

  
if __name__ == '__main__':
	app.run(debug=True)

