#python3
import sys
sys.path.append('/spherov2/')
import time
import threading
from spherov2 import scanner
from spherov2.sphero_edu import EventType, SpheroEduAPI
from spherov2.types import Color
robots = ["SB-CE32", "SB-B85A"]


def thread_function(name):
    print("Testing Starting...")
    print("Connecting to Bolt...")
    toy = scanner.find_BOLT(toy_name=name)
    if toy is not None:
        print("Connected.")
        with SpheroEduAPI(toy) as droid:
            index=robots.index(name)
            print("Testing Start...",index)
            start = time.time()
            while True:
                if index == 0:
                    droid.set_main_led(Color(r=255, g=0, b=0)) #Sets whole set_matrix
                    # droid.start_ir_broadcast(0,1)
                    droid.send_ir_message(0,30)
                if index == 1:
                    droid.set_main_led(Color(r=0, g=255, b=0)) #Sets whole set_matrix
                    # droid.start_ir_follow(0,1)
                    droid.listen_for_ir_message(0, 100)
                    # droid.onIRMessage4(4)
                end = time.time()
                if end - start > 10:
                    break
            print("Testing End...")


for robot in robots:
    robot = threading.Thread(target=thread_function, args=(robot,))
    robot.start()
