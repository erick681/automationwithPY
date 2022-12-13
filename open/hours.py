from datetime import datetime as dt
from pynput.mouse import Button ,Controller 
from playsound import playsound
import time 
import webbrowser as wb 
hours=6
minutes=20
mouse =Controller()
while True :
    if hours == dt.now().hour and minutes == dt.now().minute:
        playsound("SnapInsta.io - Madvillain - All Caps (320 kbps).mp3")
        wb.open("https://mail.google.com/mail/u/0/#inbox")
        time.sleep(15)
        mouse.position = (712, 244)
        time.sleep(5)
        mouse.click(Button.left,2)
        break

    
