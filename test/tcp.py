import sys
from spherov2.adapter.tcp_adapter import get_tcp_adapter
from spherov2 import scanner
from spherov2.sphero_edu import EventType, SpheroEduAPI

toy = scanner.find_BOLT(adapter=get_tcp_adapter('localhost'), toy_name="SB-CE32")
if toy is not None:
    print("Connected.",toy)
    with SpheroEduAPI(toy) as droid:
        droid.roll(heading=180, speed=150, duration=2)
