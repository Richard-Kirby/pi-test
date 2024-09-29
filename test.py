import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# define the connections between the pins.
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
    (23, 11, 12),   (24, 8, 10),
    (25, 0, 0),    (26, 7, 0),# Odd GND
    (27, 0, 0),    (28, 0, 0), #GPIO0/1 - not usable.
    (29, 5, 16),    (30, 0, 0), # GND
    (31, 6, 20),    (32, 12, 11),
    (33, 13, 21),   (34, 0, 0), # GND
    (35, 19, 26),   (36, 16, 5),
    (37, 26, 19),   (38, 20, 6),
    (39, 0, 0),    (40, 21, 13)] # GND

for i in pinout_wiring:
    print(i)

# Class for testing pins
class Test:
    def __init__(self, pin_num, out_pin, in_pin):
        self.pin_num = pin_num
        self.out_pin = out_pin
        self.in_pin = in_pin
        print(f"test {self.pin_num}, {self.out_pin}, {self.in_pin}")

    def test(self):
        result = [False, False, False]
        GPIO.setup(self.out_pin, GPIO.OUT)
        GPIO.setup(self.in_pin, GPIO.IN)

        GPIO.output(self.out_pin, 0)
        if GPIO.input(self.in_pin) == 0:
            result[0] = True

        print(f"pin {self.pin_num} {self.out_pin} {self.in_pin} {GPIO.input(self.in_pin)}")
        time.sleep(0.2)

        GPIO.output(self.out_pin, 1)
        if GPIO.input(self.in_pin) == 1:
            result[1] = True

        print(f"pin {self.pin_num} {self.out_pin} {self.in_pin} {GPIO.input(self.in_pin)}")
        time.sleep(0.2)

        GPIO.output(self.out_pin, 0)
        if GPIO.input(self.in_pin) == 0:
            result[2] = True

        print(f"pin {self.pin_num} {self.out_pin} {self.in_pin} {GPIO.input(self.in_pin)}")
        time.sleep(0.2)

        print("True = PASS", result)
        return result


tests =[]
results =[]

# Cycle through all the pins, testing each pin separately.
for i in range (40):
    if pinout_wiring[i][1] != 0 and pinout_wiring[i][2] != 0:
        test = Test(pinout_wiring[i][0], pinout_wiring[i][1], pinout_wiring[i][2])
        tests.append(test)

overall_pass = True

# Determine the overall pass/fail result.
for test in tests:
    result = test.test()

    if result != [True, True, True]:
        overall_pass = False

    results.append(result)

print("True = Pass, False = Fail", results)

print(f"Overall Results (Pass = True, Fail = False) Overall Pass? {overall_pass}")