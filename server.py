from flask import Flask
from modules import *
from serial.tools import list_ports


app = Flask(__name__)

dobot = CardioBot()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/connect_dobot")
def connect_dobot():
    available_ports = list(list_ports.comports())
    return available_ports
    # port = available_ports[0].device
    # print(port)

    # dobot.connect(port=port)
    # return "Dobot Connected"

@app.route("/disconnect_dobot")
def disconnect_dobot():
    dobot.disconnect()
    return "Dobot Disconnected"



if __name__ == '__main__':
    app.run()