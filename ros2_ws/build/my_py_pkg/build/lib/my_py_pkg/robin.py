import rclpy 
from rclpy.node import Node 
from example_interfaces.msg import String

class Robin(Node):
    def __init__(self):
        super().__init__("robin")
        self.subscriber_ = self.create_subscription(String, 'gotham', self.callback_func, 10)
        self.get_logger().info("Robin node is activated")

    def callback_func(self, msg):
        self.get_logger().info(msg.data)

def main(args = None):
    rclpy.init(args = args)
    node = Robin()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

