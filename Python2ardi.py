import serial
import time
arduino = serial.Serial(port='COM7', baudrate=115200, timeout=.1)
def write_data(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
def read_data():
    data = arduino.readline()
    return data
while True:
    num = input("Enter a number: ") # Taking input from user
    write_data(num)
    data= read_data()# byte type data you can convert it to int by casting
    print(data)