# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy

from rclpy.node import Node

from std_msgs.msg import Float32


# IO library for using the Raspberry GPIO
import RPi.GPIO as GPIO

# class for controlling the servo
class ServoController:
	def __init__(self, servoPin):
		self.servoPin = servoPin
		# servo PIN as output
		GPIO.setup(self.servoPin, GPIO.OUT)
		# PWM object connected on the servo pin working at 50Hz
		self.servo = GPIO.PWM(self.servoPin, 50)
		# Start PWM generation and set initial angle at 90 degree
		self.servo.start(self.getPWM(90.0))
	
	def __del__(self):
		# stop PWM once the object is destroyed
		self.servo.stop()
		# deinitialize the GPIOs		
		GPIO.cleanup()
		
	def update(self,angle):
		# update the PWM duty cycle
		self.servo.ChangeDutyCycle(self.getPWM(angle))
		
	# get the PWM duty cycle based on the desired angle.
	# 0   degree -> 1 ms   ON time
	# 90  degree -> 1.5 ms ON time
	# 180 degree -> 2 ms   ON time
	def getPWM(self, angle):
		return (angle/18.0) + 2.5
	


class MinimalSubscriber(Node):

	# initialize subscriber of topic angleServo, type Float32
	# at each received message updates the desired servo angle
	def __init__(self, servo):
		super().__init__('minimal_subscriber')
		self.servo=servo
		self.subscription = self.create_subscription(
			Float32,
			'angleServo',
			self.listener_callback,
			10)
		self.subscription  # prevent unused variable warning

	def listener_callback(self, msg):
		self.servo.update(msg.data)
		self.get_logger().info('new servo position %f degrees' % msg.data)
        


def main(args=None):
	# uses the BOARD mode pin numbering
	GPIO.setmode(GPIO.BOARD)
	# create servo object connected to pin 12
	myServo = ServoController(12)
	rclpy.init(args=args)

	minimal_subscriber = MinimalSubscriber(myServo)

	rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
	minimal_subscriber.destroy_node()
	rclpy.shutdown()
	


if __name__ == '__main__':
    main()
