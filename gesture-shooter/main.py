import cv2
from gesture_control.detector import HandDetector
from gesture_control.gesture_classifier import classify_gesture
from gesture_control.gesture_mapper import GestureMapper

cap = cv2.VideoCapture(0)
detector = HandDetector()
mapper = GestureMapper()

if not cap.isOpened():
    print("❌ Cannot open camera")
    exit()

print("✅ Camera is running")

while True:
    success, frame = cap.read()
    if not success:
        break

    frame, landmarks_list = detector.find_hands(frame)
    gesture = "UNKNOWN"

    if landmarks_list:
        gesture = classify_gesture(landmarks_list[0])
        mapper.map_gesture_to_action(gesture)
        cv2.putText(frame, f"Gesture: {gesture}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("IGI Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
