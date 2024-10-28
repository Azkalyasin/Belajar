import threading

import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set (cv2.CAP_PROP_FRAME_WIDTH, 650)
cap.set (cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
wajah = False
lock = threading.Lock()


Reference_img = cv2.imread("reference.jpg")

def membac_wajah (frame):
    global wajah
    try:
        result = DeepFace.verify(frame, Reference_img)
        verified = result['verified']
        with lock:
            wajah = True   

    except ValueError:
        with lock:
          wajah = False

while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=membac_wajah,args=(frame.copy(),) ).start()
            except ValueError:
                pass
        counter += 1

        if wajah:
            cv2.putText (frame, "Azkal", (15, 350), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 255, 0), 3)
        else :
             cv2.putText (frame, "Tidak ditemukan", (15, 350), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow("video", frame)     

    key = cv2.waitKey(1)
    if key == ord ("q"):
        break

cv2.destroyAllWindows()    

