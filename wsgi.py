import os
from flask import Flask, render_template, request
import traceback
import random as rand
app = Flask(__name__)
import json


index_counter = 0

__author__ = 'hanvitha'

 # APP_ROOT = "/opt/app-root/src/aahack"
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
with open('data.json', 'r') as f:
    data_dict = json.load(f)
    question_count = len(data_dict)

@app.route("/", methods=["GET", "POST"])
def home():
    global index_counter
    index_counter  = index_counter+1
    i = rand.randrange(question_count)
    return render_template("home.html", question = data_dict[i]['question'], image = data_dict[i]['img'], options = data_dict[i]['options'])


@app.route("/stats", strict_slashes=False)
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


@app.route("/users/<status>", strict_slashes=False, methods=["GET"])
def usersall(status=None):
    try:
        return render_template("usersRegistered.html")
    except Exception as e:
        print(traceback.print_exc())
        return "<h1>Oops! Something went wrong.. Could you try after sometime or reach out to the host!</h1>"
    finally:
        print("blah")



if __name__ == '__main__':
    app.run()
