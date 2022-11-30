import serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port= 'COM16'
ser.open()

while True:
    data=str(ser.readline())
    data= data.replace("b", "")
    data= data.replace("'", "")
    data= data.replace(" ", "")
    data= data.replace("\\r\\n", "")
    if len(data) >0:
        print(data)
        file= open ("temps.csv",'a')
        file.write(data+",")
        file.close 