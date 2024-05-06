from PIL import ImageGrab
from io import BytesIO
import numpy as np
import socket
import struct

ipHost = "169.254.12.171"
portHost = 1234
sock = socket.socket()
sock.connect((ipHost,portHost))

while True:
    screenShot=ImageGrab.grab()
    
    #screenShot.show()
    val=screenShot.resize((800,600))
    val=val.tobytes()
    sock.send(val)
    sock.recv(1)
   
    
    
   
      
