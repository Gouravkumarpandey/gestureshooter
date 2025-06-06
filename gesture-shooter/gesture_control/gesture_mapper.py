import pyautogui
from pynput.keyboard import Controller as KeyboardController
import time

keyboard = KeyboardController()

class GestureMapper:
    def __init__(self):
        self.last_gesture = None
        self.cooldown = 0.8  # seconds
        self.last_action_time = time.time()

    def map_gesture_to_action(self, gesture):
        now = time.time()

        if gesture == self.last_gesture and now - self.last_action_time < self.cooldown:
            return  # Prevent spamming

        self.last_gesture = gesture
        self.last_action_time = now

        if gesture == "SHOOT":
            print("[ACTION] Shoot!")
            pyautogui.click()
        elif gesture == "POINT":
            print("[ACTION] Move Forward")
            keyboard.press('w')
            time.sleep(0.1)
            keyboard.release('w')
        elif gesture == "BACK":
            print("[ACTION] Move Backward")
            keyboard.press('s')
            time.sleep(0.1)
            keyboard.release('s')
        elif gesture == "PALM":
            print("[ACTION] Idle")
