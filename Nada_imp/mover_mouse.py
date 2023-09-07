import pyautogui 
import time
import random
# distance = 200
# time.sleep(1)
# pyautogui.moveTo(961, 498)
# pyautogui.hotkey('alt','tab')
# while distance > 0:
#         pyautogui.drag(distance, 0, duration=0.5)   # move right
#         distance -= 5
#         pyautogui.drag(0, distance, duration=0.5)   # move down
#         pyautogui.drag(-distance, 0, duration=0.5)  # move left
#         distance -= 5
#         pyautogui.drag(0, -distance, duration=0.5)  # move up



# def abir_sql():
#         pyautogui.hotkey('win')
#         pyautogui.write('SQ')
#         pyautogui.hotkey('Enter')
#         time.sleep(0.2)
#         pyautogui.hotkey('Enter')
#         pyautogui.hotkey('Enter')
#         pyautogui.hotkey('Enter')
#         pyautogui.hotkey('Enter')
#         # time.sleep(0.2)
#         pyautogui.write('12345')
#         pyautogui.hotkey('Enter')
#         # pyautogui.write('\c employees')
#         # pyautogui.hotkey('Enter')

def macro_minecraft():
        while True:
                num = random.randint(1,9)
                pyautogui.write(f'{num}')
if __name__ == '__main__':
        # abir_sql()
        macro_minecraft()