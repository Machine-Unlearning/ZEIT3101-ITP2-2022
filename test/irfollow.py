#python3
import sys
sys.path.append('/spherov2/')
import time
import threading
from spherov2 import scanner
from spherov2.sphero_edu import EventType, SpheroEduAPI
from spherov2.types import Color
robots = ["SB-8427", "SB-B85A", "SB-E987"]

def thread_function(name):
    print("Testing Starting...")
    print("Connecting to Bolt...")
    toy = scanner.find_BOLT(toy_name=name)
    if toy is not None:
        print("Connected.")
        with SpheroEduAPI(toy) as droid:

            index=robots.index(name)
            print("Testing Start...",index)
            if index == 0:
                droid.set_main_led(Color(r=255, g=0, b=0))
                droid.start_ir_broadcast(0,1)
            if index == 1:
                droid.set_main_led(Color(r=0, g=255, b=0))
                droid.start_ir_follow(0,1)
            if index == 2:
                droid.set_main_led(Color(r=0, g=255, b=0))
                droid.start_ir_follow(0,1)
            time.sleep(20)
            print(droid.get_last_ir_message())
            print("Testing End...")

for robot in robots:
    robot = threading.Thread(target=thread_function, args=(robot,))
    robot.start()
