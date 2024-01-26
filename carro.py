
import RPi.GPIO as GPIO
import gpiozero
import time
import threading, queue

#import evdev
from evdev import InputDevice, categorize, ecodes

porcentaje=queue.Queue()



def gpio_loop():
    while(True):
        
        if porcentaje.empty()!=True:
            current=porcentaje.get()
        if(current!=0):
            if(current>0):
                led.on()
            else:
                led2.on()
            time.sleep(abs(current)/10000)
        led.off()
        led2.off()
        time.sleep(.01-abs(current)/10000)


led = gpiozero.LED(2)
led2 = gpiozero.LED(3)
porcentaje.put(0)
hilo=threading.Thread(target=gpio_loop)
hilo.start()


#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event4')

#prints out device info at start
print(gamepad)
rTrig=5 #max-1023
lTrig=2 #max=1023
lThumbX=0 #max 65535
lThumbY=1 #min 0
rThumbX=3 #max 65535
rThumbY=4 #min 0
y=307 # 0 and 1
#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
    
    if(event.type== 3):
        if(event.code==rTrig):
            porcentaje.put(-event.value*100/1023)
        elif(event.code==lTrig):
            porcentaje.put(event.value*100/1023)
        
