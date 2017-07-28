import pigpio
import time

pi = pigpio.pi()

m0_center = 1500
m0_min = m0_center-450
m0_max = m0_center+450
m1_center = 1500
m1_min = m1_center-200
m1_max = m1_center+200

pi.set_servo_pulsewidth(12, m0_center)
pi.set_servo_pulsewidth(13, m1_center)
time.sleep(2.0)

pi.set_servo_pulsewidth(12, m0_min)
pi.set_servo_pulsewidth(13, m1_min)
time.sleep(2.0)

pi.set_servo_pulsewidth(12, m0_min)
pi.set_servo_pulsewidth(13, m1_max)
time.sleep(2.0)

pi.set_servo_pulsewidth(12, m0_max)
pi.set_servo_pulsewidth(13, m1_max)
time.sleep(2.0)

pi.set_servo_pulsewidth(12, m0_max)
pi.set_servo_pulsewidth(13, m1_min)
time.sleep(2.0)

pi.set_servo_pulsewidth(12, m0_center)
pi.set_servo_pulsewidth(13, m1_center)
