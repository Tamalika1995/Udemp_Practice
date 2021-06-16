import pyautogui as pygui
width,height=pygui.size()
print(width,height)
print(pygui.position())
pygui.moveTo(10,10,duration=5)
print(pygui.position())
pygui.click(468,17)
print(pygui.position())