import pyautogui
from pynput.keyboard import Controller as KeyboardController, Key
import time

keyboard = KeyboardController()

class GestureMapper:
    def __init__(self):
        self.last_gesture = None
        self.cooldown = 0.3  # Even shorter cooldown for easier control
        self.last_action_time = time.time()
        self.is_accelerating = False

    def map_gesture_to_action(self, gesture):
        now = time.time()

        if gesture == self.last_gesture and now - self.last_action_time < self.cooldown:
            return

        self.last_gesture = gesture
        self.last_action_time = now

        # Simple controls: just gas and balance
        if gesture == "POINT":
            # Gas (hold right arrow)
            print("[ACTION] Gas!")
            keyboard.press(Key.right)
            self.is_accelerating = True
        elif gesture == "PALM":
            # Release gas and balance
            print("[ACTION] Stop & Balance")
            if self.is_accelerating:
                keyboard.release(Key.right)
                self.is_accelerating = False
            keyboard.press(Key.down)
            time.sleep(0.1)
            keyboard.release(Key.down)
        elif gesture == "NONE":
            # Stop when no gesture
            if self.is_accelerating:
                keyboard.release(Key.right)
                self.is_accelerating = False