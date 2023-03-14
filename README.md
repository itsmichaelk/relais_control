# Raspberry Pi 4-Channel Relay Control with Flask

This project provides a web interface for controlling a 4-channel relay module connected to a Raspberry Pi. The web interface is built using Flask, a Python web framework, and allows users to turn each relay on or off individually, as well as turn all relays on or off at once.

##### Requirements
Python 3 installed
Flask module for Python installed
4-channel relay module connected to Raspberry Pi
Installation
Clone this repository to your Raspberry Pi:

```bash
git clone https://github.com/yourusername/relay-control.git
pip3 install flask
```

Connect the 4-channel relay module to your Raspberry Pi as follows:

1. Connect the VCC pin of the relay module to a 5V pin on the Raspberry Pi.
2. Connect the GND pin of the relay module to a GND pin on the Raspberry Pi.
3. Connect each of the IN pins of the relay module to a GPIO pin on the Raspberry Pi, using the pin numbers specified in the code (GPIO4, GPIO22, GPIO6, and GPIO26).


Start the Flask server:
```bash
cd relay-control
python3 app.py
````

Access the web interface by navigating to your Raspberry Pi's IP address in a web browser, followed by :8000 (e.g. http://192.168.1.100:8000).
You should see a page with buttons to control each relay.

##### Usage
Click a button to turn the corresponding relay on or off.<br>
Click the "All Off" button to turn all relays off.<br>
Click the "All On" button to turn all relays on.<br>

##### Credits
This project was created by itsmichaelk.
