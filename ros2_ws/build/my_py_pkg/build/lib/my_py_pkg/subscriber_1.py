import rclpy 
from rclpy.node import Node 
from my_robot_interfaces import TargetCoordinates


class Subscriber_1(Node):
    def __init__(self):
        super().__init__("subscriber_1")
        self.subsciber = self.create_subscription(TargetCoordinates, "my_position", self.callback_func, 10)
    
    def callback_func(self, msg):
        self.get_logger().info(str(msg.data))

def main(args = None):
    rclpy.init()
    node = Subscriber_1()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()