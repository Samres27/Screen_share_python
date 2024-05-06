import sys
from PIL import Image
from io import BytesIO
import io
import cv2
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np

def test():
    # Creating a numpy array
    ls=Image.open("m1.png")
    ls=ls.resize((800,600))
    arr = np.array(ls)

    # Display original array
    #print("Original Array:\n",arr,"\n")

    # Converting array into byte array
    by = arr.tobytes()

    # Converting back the byte array into numpy array
    res = np.frombuffer(by, dtype=arr.dtype)

    # Checking both arrays
    res=res.reshape(600,800,3)
    ans = np.array_equal(res, arr)

    # Display result
    print("Are both arrays equal?:\n",ans)
    while True:
        cv2.imshow("hola",res)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

if __name__ == '__main__':
    test()