from machine import Pin
from mfrc522 import MFRC522
import utime
from time import sleep

from machine import Pin

from machine import PWM

pwm = PWM(Pin(0))

pwm.freq(50)

reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)
 
red = Pin(0, Pin.OUT)
green = Pin(1, Pin.OUT)
blue = Pin(2, Pin.OUT)
 
print("Bring RFID TAG Closer...")
print("")
 
 
while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            
            if card == 606483329:
                print("Card ID: "+ str(card)+" PASS: Green Light Activated")
                red.value(0)
                green.value(1)
                blue.value(0)
                
                
            elif card == 488735521:
                print("Card ID: "+ str(card)+" PASS: Blue Light Activated")
                red.value(0)
                green.value(0)
                blue.value(1)
                
            elif card == 3103879081:
                print("Shree harsit card")
                red.value(0)
                green.value(0)
                blue.value(1)
                
                def setServoCycle (position):

                    pwm.duty_u16(position)

                    sleep(0.01)

                while True:

                    for pos in range(1000,9000,50):
                        print("----")
                        setServoCycle(pos)

                    for pos in range(9000,1000,-50):

                        setServoCycle(pos)
                
            else:
                print("Card ID: "+ str(card)+" UNKNOWN CARD! Red Light Activated")
                red.value(1)
                green.value(0)
                blue.value(0)