import uwebsockets.client
import uasyncio
import os
import ujson
import gc
import _thread as th
from machine import ADC, Pin
import time
import gc

adc = ADC(Pin(32))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_9BIT)

def read():
    try:
        flag_adc = False
        uri = 'ws://192.168.1.124/ws/websocket/admin/'
        with uwebsockets.client.connect(uri) as websocket:
            data_read = websocket.recv()
            y = ujson.loads(data_read)
            print(y['message'])
        #mem = gc.mem_alloc() # Return the number of bytes of heap RAM that are allocated.
        #free = gc.mem_free() # Return the number of bytes of available heap RAM, or -1 if this amount is not known.
        #print("> mem-alloc: {}, mem-free: {}".format(mem, free))
        flag_adc = True
    except:
        print("websocket not connected")
        raise

def loop_read_ws(e):
    while True:
        try:
            uasyncio.get_event_loop().run_until_complete(read())
            time.sleep(e)
            gc.collect()
        except:
            pass

def loop_read_adc(e):
    while True:
        if flag_adc == True:
            n = adc.read()
            print(n)
            #mem = gc.mem_alloc() # Return the number of bytes of heap RAM that are allocated.
            #free = gc.mem_free() # Return the number of bytes of available heap RAM, or -1 if this amount is not known.
            #print("> mem-alloc: {}, mem-free: {}".format(mem, free))
            time.sleep(e)
            gc.collect()

flag_adc = True
th.start_new_thread(loop_read_ws, (0,))
th.start_new_thread(loop_read_adc, (.5,))


