import cv2
#############################################

frameWidth = 640

frameHeight = 480

nPlateCascade = cv2.CascadeClassifier("D:\CST_Stuff\Odille\haarcascades\haarcascade_russian_plate_number.xml")

minArea = 200

color = (255,0,255)

###############################################

 

cap = cv2.VideoCapture(0)

cap.set(3, frameWidth)

cap.set(4, frameHeight)

cap.set(10,150)

count = 0

 

while True:

    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)

    for (x, y, w, h) in numberPlates:

        area = w*h

        if area >minArea:

            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)

            cv2.putText(img,"Number Plate",(x,y-5),

            cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)

            imgRoi = img[y:y+h,x:x+w]

            cv2.imshow("ROI", imgRoi)

            cv2.imshow("Result", img)
           
            if cv2.waitKey(1) & 0xFF == ord('s'):      
                print(f'hey')                                            #pressing s will save the detected number plate
                cv2.imwrite("D:\CST_Stuff\Odille\haarcascades",+str(count)+".jpg",imgRoi)                    #here we have defined where our image will be saved
                cv2.rectangle(img,(0,200),(648,300),(255,0,0),cv2.FILLED)
                cv2.putText(img,"SCAN SAVED",(15,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)       #after pressing s this will display SCAN SAVED on screen
                cv2.imshow("RESULT",img)
                cv2.waitKey(500)
                count= count+1