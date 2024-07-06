import cv2
import mediapipe as mp


##captura de video
video = cv2.VideoCapture(0)

#Detectar mãos
hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)

#Desenhar mãos
mpDraw = mp.solutions.drawing_utils

##capturar video
while True:
    check,img = video.read()

    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    results = Hand.process(imgRGB)

    handsPoints = results.multi_hand_landmarks

    h,w,_= img.shape

    pontos = []

    if handsPoints:
        for points in handsPoints:
            #print(points)
            mpDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)

            for id,cord in enumerate(points.landmark):
                cx,cy = int(cord.x*w),int(cord.y*h)
                #cv2.putText(img,str(id),(cx,cy+10),cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2)
                pontos.append((cx,cy))

        dedos = [8,12,16,20]

        gesto = ""

        # --------------------- A L F A B E T O -----------------------------

        ## -------------DEDÃO------------------------INDICADOR----------------------------MEIO---------------------------ANELAR---------------------------MINDINHO------------
        if pontos[4][0] > pontos[2][0] and pontos[8][1] > pontos[5][1] and pontos[12][1] > pontos[9][1] and pontos[16][1] > pontos[13][1] and pontos[20][1] > pontos[17][1]:
            gesto += "A"

        ## -------------DEDÃO------------------------INDICADOR----------------------------MEIO---------------------------ANELAR---------------------------MINDINHO------------
        elif pontos[4][0] < pontos[2][0] and pontos[8][1] < pontos[5][1] and pontos[12][1] < pontos[19][1] and pontos[16][1] < pontos[13][1] and pontos[20][1] < pontos[19][1]:
            gesto += "B"

        ## -------------DEDÃO------------------------INDICADOR----------------------------MEIO---------------------------ANELAR---------------------------MINDINHO------------
        elif pontos[4][0] > pontos[2][0] and pontos[8][1] > pontos[6][1] and pontos[12][1] > pontos[10][1] and pontos[16][1] > pontos[14][1] and pontos[20][1] > pontos[19][1]:
            gesto += "C"

        ## -------------DEDÃO------------------------INDICADOR----------------------------MEIO---------------------------ANELAR---------------------------MINDINHO------------
        elif pontos[4][0] < pontos[2][0] and pontos[8][1] < pontos[6][1] and pontos[12][1] > pontos[10][1] and pontos[16][1] > pontos[14][1] and pontos[20][1] > pontos[19][1]:
            gesto += "D"

        ## -------------DEDÃO------------------------INDICADOR----------------------------MEIO---------------------------ANELAR---------------------------MINDINHO------------
        elif pontos[4][0] < pontos[2][0] and pontos[8][1] > pontos[5][1] and pontos[12][1] > pontos[9][1] and pontos[16][1] > pontos[13][1] and pontos[20][1] > pontos[17][1]:
            gesto += "E"

        ## -------------DEDÃO------------------------INDICADOR----------------------------MEIO---------------------------ANELAR---------------------------MINDINHO------------
        elif pontos[4][0] < pontos[2][0] and pontos[8][1] > pontos[7][1] and pontos[12][1] < pontos[10][1] and pontos[16][1] < pontos[14][1] and pontos[20][1] < pontos[19][1]:
            gesto += "F"

        ## -------------DEDÃO------------------------INDICADOR----------------------------MEIO---------------------------ANELAR---------------------------MINDINHO------------
        elif pontos[4][0] > pontos[2][0] and pontos[8][1] < pontos[5][1] and pontos[12][1] > pontos[9][1] and pontos[16][1] > pontos[13][1] and pontos[20][1] > pontos[17][1]:
            gesto += "G"


        ## -------------DEDÃO------------------------INDICADOR----------------------------MEIO---------------------------ANELAR---------------------------MINDINHO------------
        elif pontos[4][0] > pontos[2][0] and pontos[8][1] < pontos[6][1] and pontos[12][1] < pontos[10][1] and pontos[16][1] > pontos[14][1] and pontos[20][1] > pontos[19][1]:
            gesto += "H"

        ## -------------DEDÃO------------------------INDICADOR----------------------------MEIO---------------------------ANELAR---------------------------MINDINHO------------
        elif pontos[4][0] < pontos[2][0] and pontos[8][1] > pontos[5][1] and pontos[12][1] > pontos[9][1] and pontos[16][1] > pontos[13][1] and pontos[20][1] < pontos[17][1]:
            gesto += "i"



        cv2.putText(img, gesto, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 15)
        cv2.imshow("Imagem", img)

    cv2.imshow("Imagem", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()