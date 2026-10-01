import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands.Hands()
draw_utils = mp.solutions.drawing_utils
finger_counter = 0
finger_tips = [16, 20]

cap = cv2.VideoCapture(0)

while True:
    finger_counter = 0
    success, frame = cap.read()

    if not success:
        break

    framRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = mp_hands.process(framRGB)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            landmark = hand.landmark
#draw_utils.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
            if landmark[8].y < landmark[6].y and landmark[12].y < landmark[10].y:
                for tip in finger_tips:
                    if landmark[tip].y > landmark[tip-2].y:
                        finger_counter += 1

                if landmark[4].x < landmark[3].x:
                    finger_counter += 1

    if finger_counter == 3:
        cv2.putText(frame, "Victory", (50, 100), cv2.FONT_HERSHEY_COMPLEX, 5, (255,0,0), 3)
        cv2.imwrite(r"C:\Users\pooya\OneDrive\Pictures\Screenshots", frame)
    else:
        cv2.putText(frame, "Not Okay", (50, 100), cv2.FONT_HERSHEY_COMPLEX, 5, (255, 0, 0), 3)

    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()