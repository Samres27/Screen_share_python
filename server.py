import socket
from io import BytesIO
import cv2
import numpy as np
import struct

#ipHost = "169.254.12.171"
ipHost = "127.0.0.1"
portHost = 1234
sock = socket.socket()

sock.bind((ipHost,portHost))
sock.listen(1)
conn, address = sock.accept()

def bytes_to_array(b: bytes) -> np.ndarray:
    np_bytes = BytesIO(b)
    
    return np.load(np_bytes,allow_pickle=True)

while True:
    dat=b""
    dat=conn.recv(1922400) #resolution x*y*3
    mscreen = np.frombuffer(dat,dtype=np.uint8)
    mscreen=mscreen.reshape(600,1068,3)
    mscreen = cv2.cvtColor(mscreen, cv2.COLOR_BGR2RGB)
    cv2.imshow("capturado pantalla",mscreen)
    conn.send(b'o')
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

