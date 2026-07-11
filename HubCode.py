from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

from usys import stdin, stdout
from uselect import poll

hub = PrimeHub()

keyboard = poll()
keyboard.register(stdin)

while True:
    stdout.buffer.write(b"rdy")

    while not keyboard.poll(0):
        wait(10)

    cmd = stdin.readline().strip().upper()

    if cmd == "GREEN":
        hub.light.on(Color.GREEN)
        print("OK")

    elif cmd == "RED":
        hub.light.on(Color.RED)
        print("OK")

    elif cmd == "BLUE":
        hub.light.on(Color.BLUE)
        print("OK")

    elif cmd == "OFF":
        hub.light.off()
        print("OK")
