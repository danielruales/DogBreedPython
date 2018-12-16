from flask import Flask, render_template, request
import requests
import os
import sys
import urllib3
from predict import getPrediction
import pandas as pd

app = Flask(__name__)

#UPLOAD_FOLDER = "/Users/danielruales/Documents/aaaProjects/DogBreedPython/static/"
UPLOAD_FOLDER = os.getcwd() + "/static/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

gg_data = ""
gg_data2 = {}

@app.route('/')
def index():
	print(UPLOAD_FOLDER)
	print(app.config['UPLOAD_FOLDER'])
	#print(request.files['image'])
	#print(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
	return render_template('index.html', gg_data2 = gg_data2)
	#global count_list
	#if request.method == 'GET':
		#count_list, rand_int = Randomize(count_list)
		#return render_template('unity_page.html', unity_data = displayData(rand_int))

@app.route('/upload', methods=['POST'])
def upload_file():
	#print(UPLOAD_FOLDER)
	#print(app.config['UPLOAD_FOLDER'])
	file = request.files['image']
	f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
	#f = "/Users/danielruales/Documents/aaaProjects/test/" + file
	file.save(f)
	render_dir = "/static/" + str(file.filename)
	dog_breed_table = getPrediction("." + render_dir)
	print(type(dog_breed_table))
	highest_perc = dog_breed_table.iloc[0]['prob']
	most_likely_breed = dog_breed_table.iloc[0]['breed']
	print(highest_perc)
	print(dog_breed_table)
	output_table = "prob breed"
	output_table_arr = []
	output_table_arr.append("Prob\tBreed")
	for index, row in dog_breed_table.iterrows():
		output_table += str(round(row['prob'],2)) + str(row['breed']) + "\n"
		number = round(row['prob'],3)
		if (number >= 0.0001):
			output_table_arr.append(str(number) + "\t" + str(row['breed']))
		print (row['prob'], row['breed'])
	if (highest_perc < 0.15):
		print("***\nNOT A DOG!\n***")
	else:
		print("***\nIssa " + most_likely_breed + "\n***")
	outdict = {
		"dog_breed_table" : output_table_arr,
		"render_dir" : render_dir
	}
	return render_template('index.html', gg_data2 = outdict)

if __name__ == '__main__':
	app.debug = True
	app.run()
