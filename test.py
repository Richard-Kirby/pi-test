import subprocess
import os
import time

pinout_wiring = [
    (1, 0, 0),     (2, 0, 0), # 3.V, 5V,
    (3, 2, 14),    (4, 0, 0), # 5V
    (5, 3, 15),    (6, 0, 0), # GND
    (7, 4, 18),    (8, 14, 2),
    (9, 0, 0),     (10, 15, 3), # odd= GND
    (11, 17, 23),  (12, 18, 4),
    (13, 27, 24),  (14, 0, 0), # GND
    (15, 22, 0),   (16, 23, 17),
    (17, 0, 0),    (18, 24, 27), # odd 3v3
    (19, 10, 8),   (20, 0, 0), # GND
    (21, 9, 7),    (22, 25, 22),
    (23, 11, 0),   (24, 8, 10),
    (25, 0, 0),    (26, 7, 0),# Odd GND
    (27, 0, 0),    (28, 0, 0), #GPIO0/1 - not usable.
    (29, 5, 0),    (30, 0, 0), # GND
    (31, 6, 0),    (32, 12, 0),
    (33, 13, 0),   (34, 0, 0), # GND
    (35, 19, 0),   (36, 16, 0),
    (37, 26, 0),   (38, 20, 0),
    (39, 0, 0),    (40, 21, 0)] # GND

for i in pinout_wiring:
    print(i)

"""
This bit just gets the pigpiod daemon up and running if it isn't already.
The pigpio daemon accesses the Raspberry Pi GPIO.
"""
"""
def start_pigpiod():
    p = subprocess.Popen(['pgrep', '-f', 'pigpiod'], stdout=subprocess.PIPE)
    out, err = p.communicate()

    if len(out.strip()) == 0:
        os.system("sudo pigpiod")
        time.sleep(3)

start_pigpiod()
import pigpio

pi = pigpio.pi()

"""

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, 0)
GPIO.setup(14, GPIO.IN)
print(f"res {GPIO.input(14)}")
time.sleep(1)
GPIO.output(2, 1)
print(f"res {GPIO.input(14)}")
time.sleep(1)

"""
pi.write(2, 0)
print(f"res {pi.read(14)}")
time.sleep(1)
pi.write(2, 1)
print(f"res {pi.read(14)}")
time.sleep(1)
"""

for i in range (40):
    # print(f"testing pin, from, to: {pinout_wiring[i][0]}, {pinout_wiring[i][1]}, {pinout_wiring[i][2]}")
    if pinout_wiring[i][1] != 0:
        pi.write(pinout_wiring[i][1], 0)

        print(f"  pin, from, to, results: {pinout_wiring[i][0]}, {pinout_wiring[i][1]}, {pinout_wiring[i][2]}, "
              f"{pi.read(pinout_wiring[i][2])}")

        time.sleep(1)
        pi.write(pinout_wiring[i][1], 1)
        print(f"  pin, from, to, results: {pinout_wiring[i][0]}, {pinout_wiring[i][1]}, {pinout_wiring[i][2]}, "
              f"{pi.read(pinout_wiring[i][2])}")
        time.sleep(1)


for i in range(2, 28):
    pi.write(i,0)

    results =[]

    for j in range(2, 28):
        result = pi.read(j)
        results.append((j, result))

    time.sleep(1)
    print(results)
    time.sleep(2)
    pi.write(i, 0)


