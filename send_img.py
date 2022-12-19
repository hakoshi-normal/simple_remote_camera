import base64
from socket import socket, AF_INET, SOCK_DGRAM
import cv2

def cv_to_base64(img):
    _, encoded = cv2.imencode(".jpg", img)
    img_str = base64.b64encode(encoded).decode("ascii")
    return img_str

cap = cv2.VideoCapture(0)

PORT = 5000                         # 任意のポート番号
ADDRESS = "192.168.XX.XXX"          # 送信先IPアドレス
sock = socket(AF_INET, SOCK_DGRAM)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, dsize=(240, 320))   # フレーム圧縮（ネットワーク制限対策）
    img_str = cv_to_base64(frame)
    sock.sendto(img_str.encode(), (ADDRESS, PORT))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
sock.close()
