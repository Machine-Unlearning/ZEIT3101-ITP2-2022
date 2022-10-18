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
    toy = scanner.find_BOLT(toy_name=name)
    if toy is not None:
        print("Connected.")
        with SpheroEduAPI(toy) as droid:

            index=robots.index(name)
            print("Testing Start...",index)
            if index == 0:
                droid.set_main_led(Color(r=255, g=0, b=0)) #Sets whole set_matrix
                droid.listen_for_ir_message(4)
            if index == 1:
                droid.set_main_led(Color(r=0, g=255, b=0)) #Sets whole set_matrix
                droid.send_ir_message(4,5)
            time.sleep(10)
            print(droid.get_last_ir_message())
            print("Testing End...")


for robot in robots:
    robot = threading.Thread(target=thread_function, args=(robot,))
    robot.start()
