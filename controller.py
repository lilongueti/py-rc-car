
import time
import threading, queue

#import evdev
from evdev import InputDevice#, categorize, ecodes

porcentaje=queue.Queue()
direccion=queue.Queue()



def gpio_loop():
    while(True):
        
        if porcentaje.empty()!=True:
            current=porcentaje.get()
        if direccion.empty()!=True:
            currentdireccion=direccion.get()
        if(current!=0):
            if(current>0):
                #led.on()
                print("Reversa "+str(current)+"%")
            else:
                #led2.on()
                print("Avanza "+str(current)+"%")
            time.sleep(abs(current)/10000)
        if(currentdireccion!=0):
            if(currentdireccion>0):
                #led.on()
                print("Derecha "+str(currentdireccion)+"%")
            else:
                #led2.on()
                print("Izquierda "+str(currentdireccion)+"%")
        #led.off()
        #led2.off()
        time.sleep(.01-abs(current)/10000)


porcentaje.put(0)
direccion.put(0)
hilo=threading.Thread(target=gpio_loop)
hilo.start()


#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event27')

#prints out device info at start
print(gamepad)
rTrig=9 #max-1023
lTrig=10 #max=1023
lThumbX=0 #max 65535
#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
    
    if(event.type== 3):
        if(event.code==rTrig):
            porcentaje.put(-event.value*100/255)
        elif(event.code==lTrig):
            porcentaje.put(event.value*100/255)
        elif(event.code==lThumbX):
            direccion.put((event.value-128)*100/127)
        else:
            print(event);
        
