import pigpio
import time

pi = pigpio.pi()
pi.set_mode(19, pigpio.OUTPUT)
pi.write(19,0)
time.sleep(1.0)
pi.write(19,1)
