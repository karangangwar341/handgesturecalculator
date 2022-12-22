
import cv2
import mediapipe as mp
import time
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
def inpt(dig):

  num = 0
  while dig > 0:
    timeout = 10
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:

      # For webcam input:
      cap = cv2.VideoCapture(0)
      with mp_hands.Hands(
          model_complexity=0,
          min_detection_confidence=0.5,
          min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
          success, image = cap.read()
          if not success:
            print("Ignoring empty camera frame.")
            continue

          image.flags.writeable = False
          image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
          results = hands.process(image)

          image.flags.writeable = True
          image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

          # Initially set finger count to 0 for each cap
          fingerCount = 0

          if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:
              # Get hand index to check label (left or right)
              handIndex = results.multi_hand_landmarks.index(hand_landmarks)
              handLabel = results.multi_handedness[handIndex].classification[0].label


              handLandmarks = []


              for landmarks in hand_landmarks.landmark:
                handLandmarks.append([landmarks.x, landmarks.y])

              if handLabel == "Left" and handLandmarks[4][0] > handLandmarks[3][0]:
                fingerCount = fingerCount+1
              elif handLabel == "Right" and handLandmarks[4][0] < handLandmarks[3][0]:
                fingerCount = fingerCount+1

              # Other fingers: TIP y position must be lower than PIP y position,
              #   as image origin is in the upper left corner.
              if handLandmarks[8][1] < handLandmarks[6][1]:       #Index finger
                fingerCount = fingerCount+1
              if handLandmarks[12][1] < handLandmarks[10][1]:     #Middle finger
                fingerCount = fingerCount+1
              if handLandmarks[16][1] < handLandmarks[14][1]:     #Ring finger
                fingerCount = fingerCount+1
              if handLandmarks[20][1] < handLandmarks[18][1]:     #Pinky
                fingerCount = fingerCount+1


              mp_drawing.draw_landmarks(
                  image,
                  hand_landmarks,
                  mp_hands.HAND_CONNECTIONS,
                  mp_drawing_styles.get_default_hand_landmarks_style(),
                  mp_drawing_styles.get_default_hand_connections_style())

          # Display finger count

          cv2.putText(image, str(fingerCount), (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 10)
          cv2.putText(image, str(num), (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 40, 40), 10)

          # Display image
          cv2.imshow('MediaPipe Hands', image)
          if cv2.waitKey(1) == ord('q'):
            break
    num = num*10+int(fingerCount)
    dig = dig-1
    cap.release()

  return num