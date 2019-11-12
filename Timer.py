import time
import winsound
import keyboard

while True:
    if keyboard.is_pressed('page up'):
        time.sleep(60)
        winsound.PlaySound("*", winsound.SND_ALIAS)
    elif keyboard.is_pressed('page down'):
        break
