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



#Threading function which every robot uses when it connects to the computer
def thread_function(name):

    print("Testing Starting...")
    print("Connecting to Bolt...")
    toy = scanner.find_BOLT(toy_name=name)

    # Error checking and making sure the robots are connected
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

            # This functions is used to turn a formation of straight line robots to the right in a 90 degree angle
            # It uses direction, engine power and time to make the robots move from point a to point b.
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

            # This functions is used to turn a formation of straight line robots to the left in a 90 degree angle
            # It uses direction, engine power and time to make the robots move from point a to point b.
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

            # This functions is used to turn a formation of square robots to the right in a 90 degree angle
            # It uses direction, engine power and time to make the robots move from point a to point b.
            def turnRightSquare():

                if name == robots[0]:

                    droid.reset_aim()

                    droid.spin(90, 0.5)
                    droid.roll(90, 60, 0.98)

                if name == robots[1]:

                    droid.reset_aim()

                    droid.roll(0, 60, 1)
                    droid.spin(90, 0.5)
                    droid.roll(90, 60, 1)
                    droid.roll(90, 60, 0.7)

                if name == robots[2]:

                    droid.reset_aim()

                    droid.roll(0, 40, 1.65)
                    droid.spin(90, 0.5)

                if name == robots[3]:

                    droid.reset_aim()

                    droid.roll(0, 60, 1)

                    droid.roll(0, 60, 0.7)
                    droid.spin(90, 1)
                    droid.roll(90, 60, 0.8)


            #This functions is used to turn a formation of square robots to the left in a 90 degree angle
            # It uses direction, engine power and time to make the robots move from point a to point b.
            def turnLeftSquare():

                if name == robots[1]:
                    while time.process_time() < 8:
                        continue
                    droid.reset_aim()

                    droid.spin(-90, 0.5)
                    droid.roll(-90, 60, 0.98)

                if name == robots[0]:
                    while time.process_time() < 8:
                        continue
                    droid.reset_aim()

                    droid.roll(0, 60, 1)
                    droid.spin(-90, 0.5)
                    droid.roll(-90, 60, 1)
                    droid.roll(-90, 60, 0.7)

                if name == robots[3]:
                    while time.process_time() < 8:
                        continue
                    droid.reset_aim()

                    droid.roll(0, 40, 1.65)
                    droid.spin(-90, 0.5)

                if name == robots[2]:
                    while time.process_time() < 8:
                        continue
                    droid.reset_aim()

                    droid.roll(0, 60, 1)

                    droid.roll(0, 60, 0.7)
                    droid.spin(-90, 1)
                    droid.roll(-90, 60, 0.8)

            def turnRightArrow():

                if name == robots[0]:

                    droid.reset_aim()

                    droid.roll(90, 60, 1.35)

                if name == robots[1]:

                    droid.reset_aim()

                    droid.roll(0, 60, 0.7)
                    droid.roll(90, 60, 1.9)

                if name == robots[2]:

                    droid.spin(90, 1)

                if name == robots[3]:

                    droid.reset_aim()

                    droid.roll(0, 60, 1.8)
                    droid.roll(90, 60, 1.85)

            def turnLeftArrow():

                if name == robots[1]:

                    droid.reset_aim()

                    droid.roll(-90, 60, 1.35)


                if name == robots[0]:

                    droid.reset_aim()

                    droid.roll(0, 60, 0.7)
                    droid.roll(-90, 60, 1.9)

                if name == robots[3]:

                    droid.spin(-90, 1)

                if name == robots[2]:

                    droid.reset_aim()

                    droid.roll(0, 60, 1.8)
                    droid.roll(-90, 60, 1.85)


            #This is where the actual code gets executed
            #turnRightLine(4)
            #turnLeftLine(4)
            #turnRightSquare()
            #turnLeftSquare()


            #turnLeftLine(4)
            #time.sleep(15)
            #turnLeftLine(4)
            #time.sleep(15)
            #turnLeftLine(4)
            #time.sleep(15)
            #turnLeftLine(4)


            #turnLeftSquare()
            #time.sleep(8)
            #turnLeftSquare()
            #time.sleep(8)
            #turnLeftSquare()
            #time.sleep(8)
            #turnLeftSquare()

            turnLeftArrow()
            time.sleep(8)
            turnLeftArrow()
            time.sleep(8)
            turnLeftArrow()
            time.sleep(8)
            turnLeftArrow()
            print("Testing End...")







#Threading each robot
for robot in robots:
    x += 1
    robot = threading.Thread(target=thread_function, args=(robot,))
    robot.start()


#droid.register_event(EventType.on_sensor_streaming_data, droid.SensorStreamingInfo) #how you would register to data (function name is custom)
