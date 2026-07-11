import asyncio

from pybricksdev.ble import find_device
from pybricksdev.connections.pybricks import PybricksHubBLE

HUB_NAME = "Gochi"

ready = asyncio.Event()


def handle_stdout(data):
    global ready

    # Convert bytearray to bytes
    if isinstance(data, bytearray):
        data = bytes(data)

    print("Hub:", data)

    # Hub may send b"rdy" or b"OKrdy"
    if b"rdy" in data:
        ready.set()


async def main():
    print("Looking for hub...")

    device = await find_device(HUB_NAME)

    hub = PybricksHubBLE(device)

    hub.stdout_observable.subscribe(handle_stdout)

    await hub.connect()

    print("Connected!")
    print("Press the center button on the hub to start the program.")

    while True:
        cmd = input("> ").strip().upper()

        if cmd == "QUIT":
            break

        # Wait until the hub says it's ready
        await ready.wait()
        ready.clear()

        await hub.write_line(cmd)

    await hub.disconnect()


asyncio.run(main())
