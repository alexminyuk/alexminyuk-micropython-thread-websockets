# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc

def do_connect(ssid, password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.ifconfig(('192.168.1.135','255.255.255.0','192.168.1.1','192.168.1.1'))
        #sta_if.ifconfig('192.168.1.135','255.255.255.0','192.168.1.1','87.216.1.65')
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect('SSID', 'password')

#import webrepl
#webrepl.start()
gc.collect()
