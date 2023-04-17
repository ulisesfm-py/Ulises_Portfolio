from flask import Flask, render_template, request, redirect
import os
import csv

app = Flask(__name__)

def write_to_file(dict1):
    with open('database.txt', mode='a') as my_file:
            for key, value in dict1.items():
                my_file.write(f'{key}: {value}\n')
    return 'Info written in new file'

def write_to_csv(dict1):
     with open('database.csv', newline='', mode='a') as database:
          name = dict1['name']
          email = dict1['email']
          message = dict1['message']
          csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
          csv_writer.writerow([name, email, message])


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
        write_to_csv(data)
        
        return redirect('/thank_you.html')
    else: 
        return 'something went wrong'