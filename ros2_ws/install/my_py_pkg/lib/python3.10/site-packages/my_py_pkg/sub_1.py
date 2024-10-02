import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class Sub1(Node):
    def __init__(self):
        super().__init__("sub_1")
        self.subscriber_ = self.create_subscription(String, "code", self.callback_func, 10)
        self.get_logger().info("Subscriber is active")
    
    def callback_func(self, msg):
        self.get_logger().info(msg.data)
    
def main(args = None):
    rclpy.init(args=args)
    node = Sub1()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()