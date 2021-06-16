import pyautogui as pygui
pygui.click()
distance=200
while distance>0:
    print(distance,0)
    pygui.dragRel(distance,0,duration=1.5)
    distance=distance-25
    print(0,distance)
    pygui.dragRel(0,distance, duration=1.5)
    print(-distance,0)
    pygui.dragRel(-distance, 0,duration=1.5)
    distance = distance - 25
    print(0, -distance)
    pygui.dragRel(0, -distance, duration=1.5)