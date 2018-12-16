from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

UPLOAD_FOLDER = "/Users/danielruales/Documents/aaaProjects/test/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
	print(UPLOAD_FOLDER)
	print(app.config['UPLOAD_FOLDER'])
	#print(request.files['image'])
	#print(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
	return render_template('index.html')
	#global count_list
	#if request.method == 'GET':
		#count_list, rand_int = Randomize(count_list)
		#return render_template('unity_page.html', unity_data = displayData(rand_int))

@app.route('/upload', methods=['POST'])
def upload_file():
	#print(UPLOAD_FOLDER)
	#print(app.config['UPLOAD_FOLDER'])
	file = request.files['image']
	print(file)
	f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
	#f = "/Users/danielruales/Documents/aaaProjects/test/" + file
	file.save(f)
	return render_template('index.html', gg_data = file)

if __name__ == '__main__':
	app.debug = True
	app.run()
