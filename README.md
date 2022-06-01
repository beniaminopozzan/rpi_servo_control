# rpi_servo_control

This ROS2 package allows to control a PWM-based servomotor.



### Requirements

This package requires **rpi_hardware_pwm** python packages (https://pypi.org/project/rpi-hardware-pwm/) to control the GPIOs of the Raspberry.



## Installation

1. Enable the hardware PWM channel (notice that the audio output may not work anymore)

   1. add `dtoverlay=pwm-2chan` to `/boot/config.txt` or to `/boot/firmware/config.txt`. This defaults to `GPIO_18` as the pin for `PWM0` and `GPIO_19` as the pin for `PWM1`. Notice that `GPIO_18` is `PIN 12` and `GPIO_19` is `PIN 35`.

   2. Here is to use this package without `sudo` privileges: create an `udev` rule in `/etc/udev/rules.d` containing

      ```bash
      SUBSYSTEM=="pwm*", PROGRAM="/bin/sh -c '\
              chown -R root:gpio /sys/class/pwm && chmod -R 770 /sys/class/pwm;\
              chown -R root:gpio /sys/devices/platform/soc/*.pwm/pwm/pwmchip* && chmod -R 770 /sys/devices/platform/soc/*.pwm/pwm/pwmchip*\
      '"
      ```

   3. This will enable all user in the group `gpio` to access the hardware PWM channels.

2. Clone this repository insider the `src` folder of your ROS2 workspace and then build the package.



## Usage

At the moment the package uses `PIN 12` to control the servo and this value is hardcoded [here](rpi_servo_control/subscriber_member_function.py), but it can be changed to `PIN 35` using `pwm_channerl=1` when creating the `HardwarePWM` object.

To start the ROS2 node the command is

```bash
ros2 run rpi_servo_control servo_pos_listener
```

This will start a subscriber to the topic *angleServo* of type `std_msgs/msg/Float32`. Publishing on this topic a value between 0 and 180 will move the servo accordingly.

**WARNING**: no pre-check is performed on the received value, the user must ensure that the limits are satisfied.