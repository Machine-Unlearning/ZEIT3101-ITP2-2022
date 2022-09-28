from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
import threading
import math
import time

botInfo = dict()

"""class Formation:
    def __init__(self, name, list: coords, numBots, separation):
        self.name = name
        self.coords = coords
        self.numBots = numBots
        self.separation = separation

    def printFormation(self):
        x = self.coords[0]
        y = self.coords[1]
        print("moving ", self.numBots, " bots into ", self.name, " formation at (", x, ",", y, ").")

    def line(self, list: bots, spacing):
        numBots = len(bots)"""

class Move(SpheroEduAPI):
    def __init__(self, coords: list(), listOfBots: list()):
        self.coords = coords
        self.bots = listOfBots

    def move_relative(self, coords):
        global distFactor
        x = coords[0]
        y = coords[1]
        r = math.sqrt(x**2 + y**2)# * distFactor
        theta = math.atan2(x,y)

        currhead = math.radians(self.get_heading())
        newHead = int(math.degrees((currHead+theta) % (math.pi*2)))

        currentLoc = self.get_location()
        range = math.sqrt((currentLoc['x'] - x)**2 + (currentLoc['y'] -y)**2)
        lastRange = r

        print("spinning from ", currHead, " to ", newHead)
        self.spin(newHead, 1)

        """while(range<=(lastRange+0.01)):
            self.set_speed(20)

            lastRange = range
            currentLoc = self.get_location()
            range = math.sqrt((currentLoc['x'] - x) ** 2 + (currentLoc['y'] - y) ** 2)
            if range>(lastRange+0.01):
                self.set_speed(0)
                break

            print("range: ", range, ", difference: ", r - range)

        print("range: ", range, ", difference: ", r - range)"""
        self.roll(newHead, 10, r)
        self.spin(-newHead, 1)
        time.sleep(1)

    def move_into_position(self, coords, heading=0):
        bot.set_main_led(Color(r=0, g=0, b=255))
        input(str("Please move bot " + bot + " (Blue) to the start point. Press enter when ready"))
        bot.set_main_led(Color(r=255, g=255, b=0))
        bot.move_relative(coords[0], coords[1])
        print(bot, "successfully moved into position.")
        bot.set_main_led(Color(r=0, g=255, b=0))
        botInfo[bot][3] = False

    def move_into_formation(self, coords, listOfBots, heading=0):# self is list of bots, coords is list of (x, y) coords, heading is
        global botInfo
        i=0
        for bot in self.listOfBots:
            botInfo[bot] = (coords[i], botThread, False)
            botThread = threading.Thread(target=occupy, args=(bot, coords[i]))
            i+=1

toy=scanner.find_toy(toy_name="SB-E987")
with Move(toy) as droid:
    droid.move_relative((4,5))



def occupy(bot, coords):
    global botInfo
    while botInfo[self][2] == False:
        continue
    bot.Move.move_into_position(coords)


Move.move_into_formation(coords=[(0,5), (5,5)], listOfBots=["SB-E987", "SB-8427"])


class Triangle(Formation):
    def back(self, row=1, xDir="L"):
        oldX=self.coords[0]
        oldY=self.coords[1]
        sep=self.separation
        newY=oldY-((math.sqrt(3)*sep)/2)
        match xDir:
            case "L":
                newX=oldX-(sep/2)
            case "R":
                newX=oldX+(sep/2)
            case _:
                print("error")
                return
        return [newX, newY]

    def points(self):
        x=self.coords[0]
        y=self.coords[1]
        sep=self.separation
        match numBots:
            case 1:
                return list(x,y)
            case 2:
                return list(x,y)+ back()
            case 3:
                return list(x,y)+ back() + back(xDir="R")
            case 4:
                return list(x,y)+ back() + back(xDir="R") + list(x) + back

        return

class Square(Formation):
    def points(self):
        return

class Line(Formation):
    def points(self):
        return

class Vector(Formation):
    def points(self):
        return

class HollowCircle(Formation):
    def points(self):
        return