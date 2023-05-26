import cv2
from pyzbar.pyzbar import decode

def reader(img):
    img=cv2.imread(img)
    
    barcode=decode(img)

    if not barcode:
        print("No barcode detected")
    else:
        for b in barcode:
            (x, y, w, h) = b.rect
            cv2.rectangle(img, (x-10, y-10), (x + w+10, y + h+10), (255, 0, 0), 2)
            if b.data!="":
                # print(b.data)
                print(b.data.decode())
                # print(b.type)

    while True:
        cv2.imshow("TEST", img)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            cv2.destroyAllWindows()
            break

imgs=["1.jpeg", "2.jpeg", "3.jpeg", "bct.jpeg"]
# imgs=["bct.jpeg"]
for i in imgs:
    reader(i)
    # print(i)
