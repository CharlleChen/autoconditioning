# -*- coding:utf-8 -*-
# author: charlie
from visionseed import YtVisionSeed, YtDataLink
import serial
import time
import socket
import Adafruit_DHT
import time

# =================================
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
# =================================

vs = YtVisionSeed( serial.Serial("/dev/ttyACM0",115200,timeout=0.5) )

target_temp = 0
target_humi = 0

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setblocking(0)

# def main():
while True:

    # write data to server
    message = []
    
    result, msg = vs.recvRunOnce()

    if result:
        YtVisionSeedModel = YtDataLink.YtVisionSeedModel
        count = result.getResult([20])
        print("Number of people: ", count)
        message.append(count)
    else:
        message.append(0)
    
    temperature, humidity = [0,0] #Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    message.append(temperature if temperature is not None else 0)
    message.append(humidity if humidity is not None else 0)
    
    message = [str(m) for m in message]

    msg = "-".join(message)
    # print("Sending message:", msg)

    s.sendto(msg.encode('utf-8'), ('192.168.0.101', 6666))

    
    # read data from server
    try:
        data = s.recv(1024).decode('utf-8').split('-')
    except:
        data = None

    if data and len(data) == 2:
        target_temp, target_humi = data
    
    print("Target temp:", target_temp, "| Target humi:", target_humi)

    time.sleep(0.01)
        
