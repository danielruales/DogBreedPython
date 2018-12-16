# Dog Breed Predictor
Predicts dog breed.

## Getting Started

Download the source code into a folder. Jump to the Prerequisites below to ensure the necessary installations are complete.
Once they are complete, continue to Deployment.

### Prerequisites

You should have Python installed on your machine first. I used version 3.7.1 to run this application.
<br>To check if Python is installed and to see your version, try running the following command in your terminal:
```
python --version
```
If you need to download or update it, go to: https://www.python.org/
<br>
Depending on how you installed Python, you may need to use the command python3 and pip3 instead of python and pip when referenced below. I created aliases for these in my bash_profile so that I could use python/pip instead of python3/pip3.
```
nano ~/.bash_profile
```
In nano:
```
alias python3=python
alias pip3=pip
```
**Next Steps:**
<br>
Download Flask: http://flask.pocoo.org/
```
pip install Flask
```
Navigate to requirements.txt, a text file in the repo. This contains the libraries and versions needed for this application.
Install them by running:
```
pip install -r "requirements.txt"
```


## Deployment

I compiled my web application from my terminal. From the command line, cd to your source code's
directory. You can then run the following command to deploy your web app. Go to http://localhost:5000/ to view it.
```
python app.py
```

## Built With

* [Python](https://www.python.org/) - Programming Language
* [Flask](http://flask.pocoo.org/) - Web framework
* [Sublime Text](https://www.sublimetext.com/) - Text editor
* [BootstrapCDN](https://www.bootstrapcdn.com/) - Used to load CSS
