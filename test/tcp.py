from spherov2.adapter.tcp_adapter import get_tcp_adapter
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI

with scanner.find_BOLT(adapter=get_tcp_adapter('localhost')) as toy:
    print(toy)

    api= SpheroEduAPI(toy)
    api.roll(heading=180, speed=150, duration=2)
