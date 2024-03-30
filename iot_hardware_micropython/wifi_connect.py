import time
import network
from machine import Pin
import urequests as requests

def wi_connect(ssid,password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    # Wait for connect or fail
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(1)
    # Handle connection error
    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        s = 3
        while s > 0:
            s -= 1
        status = wlan.ifconfig()
        print( 'Connected to ' + ssid + '. ' + 'Device IP: ' + status[0] )
        status =1
        return status
wi_connect()
