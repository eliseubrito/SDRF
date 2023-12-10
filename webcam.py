import cv2
import numpy as np
import face_recognition as fr
from engine import get_rostos, get_infos

face_cascade = cv2.CascadeClassifier('./classifier/haarcascade_frontalface_default.xml')
vid = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
rostos_conhecidos, nomes_dos_rostos = get_rostos()
nome, cargo, idade = get_infos()

while(True):
    ret, frame = vid.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor= 1.3, minNeighbors=5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)

    rgb_small_frame = np.ascontiguousarray(frame[:, :, ::-1])

    localizacao_dos_rostos = fr.face_locations(rgb_small_frame)
    rosto_desconhecidos = fr.face_encodings(rgb_small_frame, localizacao_dos_rostos)

    for (top, right, bottom, left), rosto_desconhecido in zip(localizacao_dos_rostos, rosto_desconhecidos):
        resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
        # print(resultados)

        face_distances = fr.face_distance(rostos_conhecidos, rosto_desconhecido)
        
        melhor_id = np.argmin(face_distances)
        if resultados[melhor_id]:
            nome = nomes_dos_rostos[melhor_id]
            idad = idade[melhor_id]
            profissao = cargo[melhor_id]
            
        else:
            nome = "Desconhecido(a)"
            idad = ""
            profissao = ""
        
        # Ao redor do rosto
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Embaixo
        cv2.rectangle(frame, (left, bottom -35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX

        #Texto
        cv2.putText(frame, nome, (left + 5, bottom - 25), font, 0.4, (255, 255, 255), 1)
        cv2.putText(frame, idad, (left + 5, bottom - 12), font, 0.4, (255, 255, 255), 1)
        cv2.putText(frame, profissao, (left + 5, bottom - 1), font, 0.4, (255, 255, 255), 1)
        # cv2.putText(frame, profissao, (left + 5, bottom - 20), font, 0.5, (255, 255, 255), 1)

        cv2.imshow('Webcam_facerecognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # for (x,y,width,height), rosto_desconhecido in zip(localizacao_dos_rostos, rosto_desconhecidos):
    #     resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
    #     print(resultados)
    #     face_distances = fr.face_distance(rostos_conhecidos, rosto_desconhecido)
            
    #     melhor_id = np.argmin(face_distances)
    #     if resultados[melhor_id]:
    #         nome = nomes_dos_rostos[melhor_id]
    #         profissao = cargo[melhor_id]
    #         idad = idade[melhor_id]
    #     else:
    #         nome = "Desconhecido"
    #         profissao = ""
    #         idad = ""

    #     cv2.rectangle(frame,(x,y),(x+width,y+height),(255,255,0),2)
    #     cv2.rectangle(frame, (x, y - 50 ), (x + width, y), (255,255,0), -1)
    #     cv2.putText(frame,nome, (x, y - 40 ), font, 0.5, (0,0,0), 1)
    #     cv2.putText(frame,idad, (x, y - 25 ), font, 0.5, (0,0,0), 1)
    #     cv2.putText(frame,profissao, (x, y - 10 ), font, 0.5, (0,0,0), 1)

    # cv2.imshow('Projeti',frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break


vid.release()
cv2.destroyAllWindows()