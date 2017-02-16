import serial
from flask import Flask, send_from_directory
app = Flask(__name__)
ser = serial.Serial("/dev/ttyACM0", 9600)

@app.route('/w/')
def forward():
    ser.write('w'.encode('utf-8'))
    return 'Sent "w"'

@app.route('/a/')
def left():
    ser.write('a'.encode('utf-8'))
    return 'Sent "a"'

@app.route('/s/')
def back():
    ser.write('s'.encode('utf-8'))
    return 'Sent "s"'

@app.route('/d/')
def right():
    ser.write('d'.encode('utf-8'))
    return 'Sent "d"'

@app.route('/u/')
def up():
    ser.write('u'.encode('utf-8'))
    return 'Sent "u"'

@app.route('/n/')
def down():
    ser.write('n'.encode('utf-8'))
    return 'Sent "n"'

@app.route('/jquery-2.2.2.min.js')
def jquery():
    return send_from_directory("html", "jquery-2.2.2.min.js")

@app.route('/')
def hello_world():
    return send_from_directory("html", "index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
