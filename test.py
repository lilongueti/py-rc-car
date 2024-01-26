import RPi.GPIO as GPIO
import gpiozero
import time
import threading, queue
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
def input_loop():
    while(True):
        var = input("Nuevo porcentaje: ")
        porcentaje.put(int(var))

led = gpiozero.LED(2)
led2 = gpiozero.LED(3)
porcentaje.put(0)
hilo=threading.Thread(target=gpio_loop)
hilo_input=threading.Thread(target=input_loop)
hilo.start()
hilo_input.start()

