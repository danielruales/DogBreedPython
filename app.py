from flask import Flask, render_template, request
from data import displayData
from randomizer import Randomize
from random import randint
import requests

app = Flask(__name__)
count_list = []

@app.route('/')
def index():
	global count_list
	if request.method == 'GET':
		count_list, rand_int = Randomize(count_list)
		return render_template('unity_page.html', unity_data = displayData(rand_int))

if __name__ == '__main__':
	app.run()

