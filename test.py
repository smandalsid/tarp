import cv2
from pyzbar.pyzbar import decode

def reader(img):
    # img=cv2.imread(img)
    # width=int(img.shape[1]*.40) #scalethe image width
    # height=int(img.shape[0]*.40)
    # dim=(width, height)
    # img=cv2.resize(img, dim)
    
    barcode=decode(img)

    if not barcode:
        print("No barcode detected")
    else:
        for b in barcode:
            # (x, y, w, h) = b.rect
            # cv2.rectangle(img, (x-10, y-10), (x + w+10, y + h+10), (255, 0, 0), 2)
            if b.data!="":
                print(b.data)
                print(b.type)

    # while True:
    #     cv2.imshow("TEST", img)
    #     if cv2.waitKey(1) & 0xFF==ord('q'):
    #         cv2.destroyAllWindows()
    #         break

cap=cv2.VideoCapture(0)
cap.set(3, 640) # id 3 is to set the width of the window
cap.set(4, 480) # id 4 is to set the height of the window
cap.set(10, 150) # id 10 is to set the brightness of the image captured

while True:
    success, img = cap.read()
    cv2.imshow("Camera", img)
    reader(img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        cv2.destroyAllWindows()
        break