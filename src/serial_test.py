import serial
import time
arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    # arduino.write(x)
    time.sleep(0.10)
    data = arduino.readline()
    return data

for i in range(4):
    start_time = time.time()
    value = write_read('1')
    print(time.time() - start_time)
    print(value) # printing the value

# import serial
# import time

# ser = serial.Serial("COM6", 9600)

# ser.write(b'1')
# time.sleep(0.05)
# ser.timeout = 5
# i = ser.readline().decode('utf-8')
# print(i)