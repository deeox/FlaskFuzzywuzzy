from flask import Flask, render_template, redirect, request, url_for, flash
from fuzzywuzzy import fuzz

app = Flask(__name__)


@app.route('/results')
def correct(val1, val2, A, B, C, D):
    return render_template("results.html", value1=val1, value2=val2, A=A, B=B, C=C, D=D)


@app.route('/')
def home():
    return render_template("homepage.html")


@app.route('/', methods=['POST'])
def homepage():
    value1 = str(request.form['input1'])
    value2 = str(request.form['input2'])
    print(value1, value2)
    func1 = fuzz.ratio(value1, value2)
    func2 = fuzz.partial_ratio(value1, value2)
    func3 = fuzz.token_sort_ratio(value1, value2)
    func4 = fuzz.token_set_ratio(value1, value2)

    redirect('/results')

    return correct(value1, value2, func1, func2, func3, func4)





