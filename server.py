from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def Dimension():
    return render_template('index.html')

# def write_to_file(data):
#     with open('database.txt', mode = 'a') as database:
#         name = data ['name']
#         pronouns = data ['pronouns']
#         subject = data ['subject']
#         email = data['email']
#         message = data['message']
#         file = database.write(f'\n{name},{pronouns},{subject},{email},{message}')

def write_to_csv(data):
    with open('database.csv', mode = 'a', newline='') as database:
        name = data ['name']
        pronouns = data ['pronouns']
        subject = data ['subject']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,pronouns,email,message])

@app.route('/send_message', methods=['POST', 'GET'])
def send_message():
    data = request.form.to_dict()
    write_to_csv(data)
    return render_template('thankyou.html') 