from setuptools import setup

package_name = 'rpi_servo_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Beniamino Pozzan',
    maintainer_email='beniamino.pozzan@phd.unipd.it',
    description='ROS2 servo controller for Raspberry Pi',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'servo_pos_listener = rpi_servo_control.subscriber_member_function:main',
        ],
    },
)
