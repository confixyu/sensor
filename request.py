#!/usr/local/bin/python
import requests
import json
import datetime
import RPi.GPIO as GPIO
import time

__author__ = 'Gus (Adapted from Adafruit)'
__license__ = "GPL"
__maintainer__ = "pimylifeup.com"

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_circuit = 7

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interupted, cleanup correctly
try:
    # Main loop
    while True:
        # Need to change the ip endPoint
        url = 'http://192.168.0.194:5000/sensor'
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        payload = {'statu':rc_time(pin_to_circuit),'voltage':'3v3','time':current_time}
        r = requests.post(url, json=payload)
        print(r.content)
        print payload
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

