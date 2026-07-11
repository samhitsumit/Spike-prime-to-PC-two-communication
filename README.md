# SPIKE Prime Remote Control (Python + Pybricks)

Control a LEGO SPIKE Prime hub wirelessly from your computer using Python and Bluetooth.

This project allows a computer (Mac, Linux, or Windows with Bluetooth) to send commands to a SPIKE Prime hub running Pybricks firmware. The hub receives text commands over Bluetooth and executes actions such as changing the hub light. This provides a simple foundation for larger robotics projects where the computer performs AI, computer vision, speech recognition, or path planning while the SPIKE Prime hub controls the motors and sensors.

## Features

* Wireless Bluetooth communication
* Two-way communication between computer and hub
* Send commands from Python
* Easy to extend with custom commands
* Uses official Pybricks firmware
* Works with `pybricksdev`

## Project Structure

```text
.
├── controller.py      # Runs on your computer
├── hub.py             # Download to the SPIKE Prime hub
└── README.md
```

## Requirements

### Hub

* LEGO SPIKE Prime Hub
* Pybricks firmware installed

### Computer

* Python 3.10 or newer
* Bluetooth support
* `pybricksdev`
* `bleak`

## Setup

1. Flash your hub with Pybricks firmware.
2. Download `hub.py` to the hub using the Pybricks Code website.
3. Disconnect the Pybricks website from the hub.
4. Run `controller.py`.
5. Press the center button on the hub to start the program.
6. Type commands into the terminal.

## Available Commands

```text
GREEN
RED
BLUE
OFF
```

These can easily be expanded to support robot actions such as:

```text
DRIVE 500
TURN 90
STOP
ARM UP
ARM DOWN
CLAW OPEN
CLAW CLOSE
```

## Example

```text
> GREEN
Hub: OK

> RED
Hub: OK

> BLUE
Hub: OK
```

## How It Works

The hub waits for commands from the computer using standard input (`stdin`).

The computer sends commands over Bluetooth using `pybricksdev`, while the hub responds through standard output (`stdout`). A simple ready/response protocol keeps both devices synchronized.

## Possible Applications

* Computer Vision (OpenCV)
* AI Robot Control
* Object Detection
* Voice Control
* Autonomous Navigation
* Remote Control
* Reinforcement Learning
* Machine Learning

## License

MIT License
