#!/usr/bin/python3
from flask import Flask, render_template, request, redirect, url_for, make_response
import time
import RPi.GPIO as GPIO

# Define GPIO pins for relays
pin1 = 4
pin2 = 22
pin3 = 6
pin4 = 26

# Ignore GPIO warnings and set the mode
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Set all relay pins as output
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

# Set all relay pins to high
GPIO.output(pin1, 1)
GPIO.output(pin2, 1)
GPIO.output(pin3, 1)
GPIO.output(pin4, 1)

# Create the Flask app
app = Flask(__name__)

# Return the index.html page when the IP address is selected
@app.route('/')
def index():
    return render_template('index.html')

# Receive POST requests from HTML buttons and control the relays accordingly
@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):
    changePin = int(changepin)   # cast changepin to an int

    # Control individual relays based on the input button
    if changePin == 1:
        print("Relais1 On")
        GPIO.output(pin1, 0)
    if changePin == 10:
        print("Relais1 Off")
        GPIO.output(pin1, 1)
    if changePin == 2:
        print("Relais2 On")
        GPIO.output(pin2, 0)
    if changePin == 20:
        print("Relais2 Off")
        GPIO.output(pin2, 1)
    if changePin == 3:
        print("Relais3 On")
        GPIO.output(pin3, 0)
    if changePin == 30:
        print("Relais3 Off")
        GPIO.output(pin3, 1)
    if changePin == 4:
        print("Relais4 On")
        GPIO.output(pin4, 0)
    if changePin == 40:
        print("Relais4 Off")
        GPIO.output(pin4, 1)
    # Control all relays based on the input button
    elif changePin == 5:
        print("Relais1 Off")
        print("Relais2 Off")
        print("Relais3 Off")
        print("Relais4 Off")
        GPIO.output(pin1, 1)
        GPIO.output(pin2, 1)
        GPIO.output(pin3, 1)
        GPIO.output(pin4, 1)
    elif changePin == 6:
        print("Relais1 On")
        print("Relais2 On")
        print("Relais3 On")
        print("Relais4 On")
        GPIO.output(pin1, 0)
        GPIO.output(pin2, 0)
        GPIO.output(pin3, 0)
        GPIO.output(pin4, 0)

    # Redirect to the index page after a button press
    response = make_response(redirect(url_for('index')))
    return response

# Run the Flask app on port 8000 in debug mode
app.run(debug=True, host='0.0.0.0', port=8000)
