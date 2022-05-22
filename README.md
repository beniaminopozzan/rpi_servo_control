# rpi_servo_control

This ROS2 package allows to control a PWM-based servomotor.



## Installation

Clone this repository insider the `src` folder of your ROS2 workspace and then build the package.

### Requirements

This package requires **RPi.GPIO** python packages (https://pypi.org/project/RPi.GPIO/) to control the GPIOs of the Raspberry.



## Usage

At the moment the package uses pin 12 to control the servo and this value is hardcoded [here](rpi_servo_control/subscriber_member_function.py), but it can be changed to any other valid pin.

To start the ROS2 node the command is

```bash
ros2 run rpi_servo_control servo_pos_listener
```

This will start a subscriber to the topic *angleServo* of type `std_msgs/msg/Float32`. Publishing on this topic a value between 0 and 180 will move the servo accordingly.

**WARNING**: no pre-check is performed on the received value, the user must ensure that the limits are satisfied.