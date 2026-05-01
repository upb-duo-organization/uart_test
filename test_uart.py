import serial
import time

# ttyTHS1 is the standard port for pins 8 & 10
ser = serial.Serial('/dev/ttyTHS1', 115200, timeout=1)

try:
    while True:
        ser.write(b'Hello World\n')
        print("Data sent")
        time.sleep(1)
except KeyboardInterrupt:
    ser.close()
