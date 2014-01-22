import serial
import time

class Arduino:
  def __init__(self,port):
    self.ser=serial.Serial(port,9600)

  def lightLed(self,r,g,b):
    red = str(chr(r)) #Convert the decimal number to ASCII
    blue = str(chr(b))
    green = str(chr(g))
  
    self.ser.writelines(red+green+blue) # send color to the Arduino     
