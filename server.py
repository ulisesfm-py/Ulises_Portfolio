from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/generic.html")
def my_generic():
    return render_template('generic.html')


@app.route("/elements.html")
def my_elements():
    return render_template('elements.html')
