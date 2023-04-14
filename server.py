from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('/thank_you.html')
    else: 
        return 'something went wrong'