
import time
import threading, queue


import pygame
from pygame import joystick


porcentaje=queue.Queue()
direccion=queue.Queue()



def gpio_loop():
    while(True):
        
        if porcentaje.empty()!=True:
            current=porcentaje.get()
            print("Power "+str(current)+"%")
        if direccion.empty()!=True:
            currentdireccion=direccion.get()
            print("Direction "+str(currentdireccion)+"%")
        if(current!=0):
            if(current>0):
                #led.on()
                #print("Power "+str(current)+"%")
                hola=1
            else:
                #led2.on()
                #print("Avanza "+str(current)+"%")
                hola=2
            time.sleep(abs(current)/10000)
        if(currentdireccion!=0):
            if(currentdireccion>0):
                #led.on()
                #print("Derecha "+str(currentdireccion)+"%")
                hola=1
            else:
                #led2.on()
                #print("Izquierda "+str(currentdireccion)+"%")
                hola=1
        #led.off()
        #led2.off()
        time.sleep(.01-abs(current)/10000)


porcentaje.put(0)
direccion.put(0)
hilo=threading.Thread(target=gpio_loop)
hilo.start()

joysticks={}
pygame.init()
pygame.joystick.init()
while True:
    for event in pygame.event.get():
        if(event.type==pygame.JOYDEVICEADDED):
            joysticks[event.device_index]=pygame.joystick.Joystick(event.device_index)
            joysticks[event.device_index].init()
        elif event.type == pygame.JOYAXISMOTION:
            if event.axis == 0:  # X-axis (left-right)
                if direccion.empty()==False:
                    direccion.get()
                direccion.put(round(100*event.value,0))
            elif event.axis == 2:  # Trigger left
                if porcentaje.empty()==False:
                    porcentaje.get()
                porcentaje.put(round(-100 * ((event.value)+1)/2,0))
            elif event.axis == 5:  # Trigger right
                if porcentaje.empty()==False:
                    porcentaje.get()
                porcentaje.put(round(100 * ((event.value)+1)/2,0))
