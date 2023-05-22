import pyautogui
from PIL import ImageGrab
import keyboard
import time

# define the RGB values of the colors you want to detect
colors = [(223, 184, 224), (70, 200, 229), (80, 211, 146)]

# set the delay between clicks in seconds
delay = 0.1

# main loop
while True:
    # take a screenshot of the screen
    screenshot = ImageGrab.grab()
    
    # check if any of the colors are present on the screen
    for color in colors:
        if color in screenshot.getcolors(screenshot.size[0] * screenshot.size[1]):
            # get the coordinates of the color
            coordinates = pyautogui.locateAllOnScreen(color, confidence=0.9)
            
            # click on each coordinate with a delay of 0.1 seconds
            for coordinate in coordinates:
                pyautogui.click(coordinate[0], coordinate[1], interval=delay)
                
    # check if the Ctrl key is pressed to terminate the program
    if keyboard.is_pressed('ctrl'):
        break
        
    # add a small delay to reduce the CPU usage
    time.sleep(0.1)
