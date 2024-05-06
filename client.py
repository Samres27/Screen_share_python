from PIL import ImageGrab
from io import BytesIO
import numpy as np
import socket
import struct

ipHost = "169.254.12.171"
portHost = 1234
sock = socket.socket()
sock.connect((ipHost,portHost))


def array_to_bytes(x: np.ndarray) -> bytes:
    np_bytes = BytesIO()
    np.save(np_bytes, x, allow_pickle=False)
    return np_bytes.getvalue()

while True:
    screenShot=ImageGrab.grab()
    
    #screenShot.show()
    val=screenShot.resize((800,600))
    val=val.tobytes()
    #vls=array_to_bytes(np.array(val))
    value=struct.pack("s",val)
    np.frombuffer()
    sock.send(value)
   
    
    
   
      
