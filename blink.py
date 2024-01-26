import RPi.GPIO as GPIO
import gpiozero
import time
import threading, queue
porcentaje=queue.Queue()



def gpio_loop():
    while(True):
        if porcentaje.empty()!=True:
            current=porcentaje.get()
        led.on()
        time.sleep(current)
        led.off()
        led2.on()
        time.sleep(current)
        led2.off()
def input_loop():
    while(True):
        var = input("tiempo en segundos")
        porcentaje.put(float(var))

led = gpiozero.LED(3)
led2 = gpiozero.LED(2)
porcentaje.put(1)
hilo=threading.Thread(target=gpio_loop)
hilo_input=threading.Thread(target=input_loop)
hilo.start()
hilo_input.start()
