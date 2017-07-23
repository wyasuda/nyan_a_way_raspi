import pigpio
import time

pi = pigpio.pi()

pi.set_servo_pulsewidth(12, 1500)
pi.set_servo_pulsewidth(13, 1500)
time.sleep(2.0)

pi.set_servo_pulsewidth(12, 1500+900)
pi.set_servo_pulsewidth(13, 1500+900)
time.sleep(2.0)

pi.set_servo_pulsewidth(12, 1500)
pi.set_servo_pulsewidth(13, 1500)
time.sleep(2.0)

pi.set_servo_pulsewidth(12, 1500-900)
pi.set_servo_pulsewidth(13, 1500-900)
time.sleep(2.0)

pi.set_servo_pulsewidth(12, 1500)
pi.set_servo_pulsewidth(13, 1500)
