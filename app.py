import ast
import os
import sys
import time
import threading
from datetime import date
from time import sleep
from camera import Camera
from flask import Flask, jsonify, redirect, render_template, request, url_for, Response

from waitress import serve

#env_path = "~/server"
#sys.path.append(env_path)

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/') # INDEX
def index():
    return render_template('index.html',
                           bab = 'img/image.jpg',
                           every_5min = 'img/live.jpg')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=5678, threads=90) # If error occurs pip install waitress

