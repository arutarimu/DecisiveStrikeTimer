import winsound
import time
import keyboard


def timer():
    while True:
        time.sleep(0.1)
        if keyboard.is_pressed('page up'):
            time.sleep(60)
            winsound.MessageBeep(-1)
        elif keyboard.is_pressed('page down'):
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            break


timer()
