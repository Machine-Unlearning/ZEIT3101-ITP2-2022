#python3
import sys
import time

sys.path.append('/spherov2/')
import timeit
import threading
from spherov2 import scanner
from spherov2.sphero_edu import EventType, SpheroEduAPI
from spherov2.types import Color
#robots = ["SB-09D3"]
robots = ["SB-09D3", "SB-41F2", "SB-B11E", "SB-DAA6"]
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

            # Sub function for readability
            # Need to align the timings so they execute at the same time.
            def turnRightLine(amount):
                num = 0

                while num < amount:
                    if name == robots[0]:

                        droid.reset_aim()
                        droid.roll(0, 60, 2)
                        droid.spin(90, 3.5)
                        break

                    if name == robots[num]:

                        droid.reset_aim()
                        droid.roll(0, 60, 2)
                        droid.roll(0, 60, 1*num)
                        droid.spin(90, 1)
                        droid.roll(90, 60, 1.1*num)

                    num = num + 1

            def turnLeftLine(amount):
                num = 0

                while num < amount:
                    if name == robots[len(robots)-1]:
                        droid.reset_aim()
                        droid.roll(0, 60, 2)
                        droid.spin(-90, 3.5)
                        break

                    if name == robots[len(robots)-1-num]:
                        droid.reset_aim()
                        droid.roll(0, 60, 2)
                        droid.roll(0, 60, 1 * num)
                        droid.spin(-90, 1)
                        droid.roll(-90, 60, 1.1 * num)

                    num = num + 1



            def turnRightSquare():

                if name == robots[0]:

                    droid.reset_aim()

                    droid.spin(90, 0.5)
                    droid.roll(90, 60, 1)

                if name == robots[1]:

                    droid.reset_aim()

                    droid.roll(0, 60, 1)
                    droid.spin(90, 0.5)
                    droid.roll(90, 60, 1)
                    droid.roll(90, 60, 1)

                if name == robots[2]:
                    while time.process_time() < 8:
                        continue
                    droid.reset_aim()

                    droid.roll(0, 40, 2)
                    droid.spin(90, 1)

                if name == robots[3]:
                    while time.process_time() < 8:
                        continue
                    droid.reset_aim()

                    droid.roll(0, 60, 1)

                    droid.roll(0, 60, 1)
                    droid.spin(90, 1)
                    droid.roll(90, 60, 1.1)

            def turnLeftSquare():

                if name == robots[1]:
                    while time.process_time() < 7:
                        continue
                    droid.reset_aim()

                    droid.spin(-90, 0.5)
                    droid.roll(-90, 60, 1)

                if name == robots[0]:
                    while time.process_time() < 7:
                        continue

                    droid.reset_aim()

                    droid.roll(0, 60, 1)
                    droid.spin(-90, 0.5)
                    droid.roll(-90, 60, 1)
                    droid.roll(-90, 60, 1)

                if name == robots[3]:
                    while time.process_time() < 10:
                        continue
                    droid.reset_aim()

                    while time.process_time() < 12:
                        continue
                    droid.roll(0, 60, 1.25)
                    droid.spin(-90, 1)

                if name == robots[2]:
                    while time.process_time() < 13:
                        continue
                    droid.reset_aim()

                    droid.roll(0, 60, 1)

                    droid.roll(0, 60, 1)
                    droid.spin(-90, 1)
                    droid.roll(-90, 60, 1.1)

            #while time.process_time() < 10:
                #continue
            #turnRightLine(4)
            turnLeftLine(4)
            #turnRightSquare()
            #turnRightSquare()

            print("Testing End...")








for robot in robots:
    x += 1
    robot = threading.Thread(target=thread_function, args=(robot,))
    robot.start()


#droid.register_event(EventType.on_sensor_streaming_data, droid.SensorStreamingInfo) #how you would register to data (function name is custom)
