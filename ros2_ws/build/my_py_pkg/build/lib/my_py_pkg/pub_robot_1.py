import rclpy
from rclpy.node import Node 
from example_interfaces.msg import Int64 

class RobotP1(Node):
    def __init__(self):
        super().__init__("pub_robot_1")
        