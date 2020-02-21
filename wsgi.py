import os
from flask import Flask, render_template, request
import traceback
import random as rand
app = Flask(__name__)
import json

__author__ = 'hanvitha'

 # APP_ROOT = "/opt/app-root/src/aahack"
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
with open('data.json', 'r') as f:
    data_dict = json.load(f)
    question_count = len(data_dict)

index_counter = 0

@app.route("/", methods=["GET", "POST"])
def home():
    global index_counter
    index_counter = index_counter+1
    i = rand.randrange(question_count)
    if index_counter%5 == 0:
        print(index_counter)
    return render_template("home.html", question = data_dict[i]['question'], image = data_dict[i]['img'], options = data_dict[i]['options'])


@app.route("/stats", methods=["GET"], strict_slashes=False)
def users():
    return render_template("stats.html", count=index_counter)

@app.route("/result", strict_slashes=False, methods=["GET","POST"])
def result():
    options = request.form['options']
    correct = options.split("_")[0]
    answer = options.split("_")[1]
    if(correct == '1'):
        result = "Good one Buddy! \nYou are a Genius! \n Dont forget to collect your goodie..."
    else:
        result = "Oops! " + answer
    return render_template("result.html", result=result)

if __name__ == '__main__':
    app.run()
