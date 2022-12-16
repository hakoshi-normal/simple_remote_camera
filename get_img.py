import base64
from socket import socket, AF_INET, SOCK_DGRAM
import cv2
import numpy as np

def base64_to_cv(img_str):
    img_raw = np.frombuffer(base64.b64decode(img_str), np.uint8)
    img = cv2.imdecode(img_raw, cv2.IMREAD_UNCHANGED)
    return img

PORT = 5000                             # 任意のポート番号
sock = socket(AF_INET, SOCK_DGRAM)      # ソケットを用意
sock.bind(("", PORT))

while True:
    msg, address = sock.recvfrom(65535)
    msg = msg.decode()
    img = base64_to_cv(msg)
    img = cv2.resize(img, dsize=None, fx=3, fy=3)
    cv2.imshow("test", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

sock.close()
