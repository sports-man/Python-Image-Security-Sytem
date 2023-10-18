import cv2
import face_recognition

elonMusk = cv2.imread("resources/elon musk.jpg")
testImg = cv2.imread("resources/bill gates.jpg")

# (top, right, bottom, left)
faceLoc = face_recognition.face_locations(elonMusk)[0]
testLoc = face_recognition.face_locations(testImg)[0]

print(testLoc)

cv2.rectangle(elonMusk, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 255, 0), 3)
cv2.rectangle(testImg, (testLoc[3], testLoc[0]), (testLoc[1], testLoc[2]), (0, 255, 0), 3)

encodedElon = face_recognition.face_encodings(elonMusk)[0] 
encodedTest = face_recognition.face_encodings(testImg)[0] 
print(encodedTest)

result = face_recognition.compare_faces([encodedElon], encodedTest)
faceDis = face_recognition.face_distance([encodedElon], encodedTest)
print(result, faceDis)

cv2.putText(testImg, f'{result} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

cv2.imshow("Elon Musk", elonMusk)
cv2.imshow("Test Image", testImg)

cv2.waitKey(7000)

