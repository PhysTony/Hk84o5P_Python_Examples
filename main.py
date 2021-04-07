import cv2
import numpy as np
import pyautogui
import time

SCREEN_SIZE = (1920,1080)

# MACOS AND LINUX: *'XVID' (MacOS users may want to try VIDX as well just in case)
# WINDOWS *'VIDX'
fourcc = cv2.VideoWriter_fourcc(*"DIVX")
out = cv2.VideoWriter("output.avi", fourcc, 25, (SCREEN_SIZE))

fps = 20
prev = 0

while True:
    time_elapsed = time.time() - prev
    
    img = pyautogui.screenshot()
    
    if time_elapsed > 1.0/fps:
        prev = time.time()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        
    cv2.waitKey(10)
    
cv2.destroyAllWindows()
out.release()

# RUN FROM COMMAND PROMPT: python main.py
# ctrl + C to release.