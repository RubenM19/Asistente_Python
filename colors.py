import cv2 #Trabaja con GBR
import numpy as np

def draw(mask, color, frame_para):
    contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        if area > 1000:
            new_contours = cv2.convexHull(c)
            cv2.drawContours(frame_para, [new_contours], 0, color, 3)
    
def capture():
    cap = cv2.VideoCapture(0) #El 0 es el la camara principal

    #HSV / BGR / RGB tipos de conversiones de colores

    #Gracias a numpy y sus arreglos detectamos los colores:

    amarillo_suave = np.array([25, 190, 20], np.uint8)
    amarillo_fuerte = np.array([30, 255, 255], np.uint8)
    rojo_suave1 = np.array([0, 100, 20], np.uint8)
    rojo_fuerte1 = np.array([5, 255, 255], np.uint8)
    rojo_suave2 = np.array([175, 100, 20], np.uint8)
    rojo_fuerte2 = np.array([180, 255, 255], np.uint8)

    while True:
        comp, frame = cap.read()
        if comp == True:
            frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Transforma el color tipo BGR a HSV
            mask_amarillo = cv2.inRange(frame_HSV, amarillo_suave, amarillo_fuerte)
            mask_rojo1 = cv2.inRange(frame_HSV, rojo_suave1, rojo_fuerte1)
            mask_rojo2 = cv2.inRange(frame_HSV, rojo_suave2, rojo_fuerte2)
            mask_rojo = cv2.add(mask_rojo1, mask_rojo2)

            draw(mask_amarillo, [0, 255, 255], frame)
            draw(mask_rojo, [0, 0, 255], frame)

            cv2.imshow("WebCam", frame)

            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
                cap.release()
                cv2.destroyAllWindows