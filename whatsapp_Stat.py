import os
import schedule
import time
import pywhatkit
from selenium import webdriver

def update_whatsapp_status():
    os.system(" youtube-dl https://www.youtube.com/watch?v=jsz6vXW77yc&ab_channel=InsiderBusiness -o video1.mp4")

    pywhatkit.sendwhatmsg("+233557113149", 0, 0, "video1.mp4", True)


schedule.every().day.at("01:00").do(update_whatsapp_status())

while True:
    schedule.run_pending()
    time.sleep(1)