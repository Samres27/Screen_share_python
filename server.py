import socket
from io import BytesIO
import cv2
import numpy as np
import struct

ipHost = "169.254.12.171"
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
    dat=conn.recv(2916922) #cambiar pos resolucion
    #try:Aa
    dat=struct.unpack('s',dat)
    mscreen = bytes_to_array(dat)
    mscreen = cv2.cvtColor(mscreen, cv2.COLOR_BGR2RGB)
    #except:pass
    #mscreen=Image.fromarray(dat)
    cv2.imshow("capturado pantalla",mscreen)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

