from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route("/") # this is actually the home
def home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def index(page_name):
    return render_template(page_name)


# when you are using urls it is better to use url_for from flask to create it not from the hard way

# GET means the browser wants us to send information
# POST means the browser wants us to save information

# this will write into database.txt
# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n Email: {email} || Subject: {subject} || Message: {message}')

def write_to_csv(data):
    with open('database.csv', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET']) 
def form_submit():
    if request.method == 'POST' :
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/form.html')
        except:
            return 'did not save to database'
    else:
        return redirect('./form_false.html')