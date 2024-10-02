import rclpy 
from rclpy.node import Node 

from example_interfaces.msg import String 

class Pub1(Node):
    def __init__(self):
        super().__init__("pub_1")
        self.publisher_ = self.create_publisher(String, "code", 10)
        self.create_timer(1.0, self.callback_func)
        self.get_logger().info("Pub 1 is ready")

    def callback_func(self):
        msg = String()
        msg.data = """We're active"""
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Pub1()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
