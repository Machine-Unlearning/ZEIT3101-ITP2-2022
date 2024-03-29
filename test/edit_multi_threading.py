#python3
import sys
sys.path.append('/spherov2/')
import time
import threading
from spherov2 import scanner
from spherov2.sphero_edu import EventType, SpheroEduAPI
from spherov2.types import Color
robots = ["SB-DAA6", "SB-B11E"]
x = 0
y = 0
initiator = False

def thread_function(name):
    print("Testing Starting...")
    print("Connecting to Bolt...")
    toy = scanner.find_BOLT(toy_name=name)

    if toy is not None:
        print("Connected.")
        with SpheroEduAPI(toy) as droid:
            def turnRight(position):
                droid.reset_aim()
                droid.roll(0, 50, 1*position)
                droid.spin(90, 3.5)
                droid.roll(90, 50, 1*position)

            droid.set_main_led(Color(r=255, g=0, b=0)) #Sets whole set_matrix
            global y
            global initiator

            y += 1
            print(y)
            if y == x:
                initiator = True
                print("Initiator true")
            while not ((y == x) and (initiator == True)):
                droid.set_main_led(Color(r=0, g=255, b=0)) #Sets whole set_matrix
                if initiator == True:
                    print("break")
                    break
            print("Testing Start...")
            index=robots.index(name)
            turnRight(index)
            print("Testing End...")

for robot in robots:
    x += 1
    robot = threading.Thread(target=thread_function, args=(robot,))
    robot.start()
