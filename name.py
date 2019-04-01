import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    my_day = datetime.datetime.today().weekday()
    friday = my_day == 4
    return render_template("friday.html", friday=friday)
