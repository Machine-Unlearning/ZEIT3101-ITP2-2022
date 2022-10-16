#python3
import sys
sys.path.append('/spherov2/')
import time
import threading
from spherov2 import scanner
from spherov2.sphero_edu import EventType, SpheroEduAPI
from spherov2.types import Color
robots = ["SB-8427", "SB-B85A"]


def thread_function(name):
    print("Testing Starting...")
    print("Connecting to Bolt...")
    toy = scanner.find_toy(toy_name=name)
    if toy is not None:
        print("Connected.")
        with SpheroEduAPI(toy) as droid:
            index=robots.index(name)
            print("Testing Start...",index)
            # start = time.time()
            if index == 0:
                droid.set_main_led(Color(r=255, g=0, b=0)) #Sets whole set_matrix
                droid.roll(0, 100, 1)
                droid.start_ir_broadcast(0,7)
                    # droid.send_ir_message(0,30)
            if index == 1:
                droid.set_main_led(Color(r=0, g=255, b=0)) #Sets whole set_matrix
                droid.start_ir_evade(0,7)
                    # droid.listen_for_ir_message(0, 100)
                    # droid.onIRMessage4(4)
                    # end = time.time()
            time.sleep(10)
            print("Testing End...")


for robot in robots:
    robot = threading.Thread(target=thread_function, args=(robot,))
    robot.start()
