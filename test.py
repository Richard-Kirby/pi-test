import subprocess
import os
import time

pinout_wiring = [
    (1, 0, 0), # 3v3
    (2, 0, 0), # 5V
    (3, 2, 0),
    (4, 0, 0), # GND
    (5, 3, 0),
    (6, 0, 0), # GND
    (7, 4, 0),
    (8, 14, 0),
    (9, 0, 0), # GND
    (10, 15, 0),
    (11, 17, 0),
    (12, 18, 0),
    (13, 27, 0),
    (14, 0, 0), # GND
    (15, 22, 0),
    (16, 23, 0),
    (17, 0, 0), # 3v3
    (18, 24, 0),
    (19, 10, 0),
    (20, 0, 0), # GND
    (21, 9, 0),
    (22, 25, 0),
    (23, 11, 0),
    (24, 8, 0),
    (25, 0, 0), # GND
    (26, 7, 0),
    (27, 0, 0), # GPIO0 - not usable.
    (28, 0, 0), # GPIO - no usable.
    (29, 5, 0),
    (30, 0, 0), # GND
    (31, 6, 0),
    (32, 12, 0),
    (33, 13, 0),
    (34, 0, 0), # GND
    (35, 19, 0),
    (36, 16, 0),
    (37, 26, 0),
    (38, 20, 0),
    (39, 0, 0), # GND
    (40, 21, 0)]

for i in pinout_wiring:
    print(i)

print(pinout_wiring)

"""
This bit just gets the pigpiod daemon up and running if it isn't already.
The pigpio daemon accesses the Raspberry Pi GPIO.
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
for i in range(2, 28):
    pi.write(i,1)

    results =[]

    for j in range(2, 28):
        result = pi.read(j)
        results.append((j, result))

    time.sleep(1)
    print(results)
    time.sleep(2)
    pi.write(i, 0)


