#python3
import sys
sys.path.append('/spherov2/')
import time
import threading
from spherov2 import scanner
from spherov2.sphero_edu import EventType, SpheroEduAPI
from spherov2.types import Color
leaders = ["SB-09D3"]
robots = ["SB-B11E"]
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
                print("Setting matrix")
                if initiator == True:
                    print("break")
                    break
            print(y)
            print("Testing Start...")

            droid.start_ir_follow(0, 1)



            #droid.set_speed(30)
            #droid.spin(360, 20)
            #droid.set_main_led(Color(r=255, g=0, b=0)) #Sets whole Matrix
            print("Testing End...")


def turnRight(name):
    toy = scanner.find_toy(toy_name=name)
    with SpheroEduAPI(toy) as droid:
        droid.reset_aim()
        droid.roll(0, 50, 1)
        droid.reset_aim()
        droid.spin(90, 1)

for robot in robots:
    x += 1
    robot = threading.Thread(target=thread_function, args=(robot,))
    robot.start()
    for leader in leaders:
        toy = scanner.find_toy(toy_name=leader)
        with SpheroEduAPI(toy) as droid:
            droid.start_ir_broadcast(0, 1)

            droid.roll(0, 50, 1)
            droid.roll(90, 50, 1)
            droid.roll(180, 50, 1)
            droid.roll(270, 50, 1)
            droid.spin(0, 1)
#droid.register_event(EventType.on_sensor_streaming_data, droid.SensorStreamingInfo) #how you would register to data (function name is custom)
