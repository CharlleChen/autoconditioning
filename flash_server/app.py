"""
A sample Hello World server.
"""
import os
import requests

from flask import Flask, render_template
from server import sock
import threading

import sys



# pylint: disable=C0103
app = Flask(__name__)


@app.route('/')
def hello():


    return render_template('introduction.html')
@app.route('/status.html')
def sec():
    with open('status','r') as f:
        data = f.read().split('-')
        if len(data) == 3:
            number, temp, humidity = data
        else:
            number, temp, humidity = [-1, -1, -1]
    print(number, temp, humidity)

    return render_template('status.html', temp=temp, humidity=humidity, number=number)

if __name__ == '__main__':

    threading._start_new_thread(sock,())
    print("started the thread")
    sys.stdout.flush()

    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')

