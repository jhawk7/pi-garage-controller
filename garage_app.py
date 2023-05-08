from flask import Flask, render_template, request, json
from garage_relay import GarageRelay

import RPi.GPIO as GPIO
import time
import _thread

app = Flask(__name__)

@app.route("/")
def form():
  return render_template('index.html')

@app.route("/toggle")
def web_trigger():
  g_control.acquire()
  trigger("web app")
  g_control.release()
  response = app.response_class(
    response=None,
    status=200,
    mimetype='application/json'
  )
  return response


def trigger(source):
    print(f'relay triggered from {source}\n')
    garage.trigger()

def button_thread():
  while True:
    if GPIO.input(button) == 0:
      g_control.acquire()
      trigger("button")
      g_control.release()


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
button = 22
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP) #pullup makes button high by default unless connected to ground via button push (long press)
garage = GarageRelay(26) #init garage relay on gpio pin 26
g_control = _thread.allocate_lock() #garage semaphore lock; only 1 thread will control garage at a time
_thread.start_new_thread(button_thread, ()) #start garage button thread

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)

