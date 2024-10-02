import rclpy 
from rclpy.node import Node 
from example_interfaces.msg import Int32

class Publisher1(Node):
    def __init__(self):
        super().__init__("publisher_1")
        self.publisher_ = self.create_publisher(Int32, "control", 10)
        self.create_timer(1.0, self.callback_func)
        self.get_logger().info("Publisher 1 is active")

    def callback_func(self):
        msg = Int32()
        msg.data = 32
        self.publisher_.publish(msg)

def main(args = None):
    rclpy.init()
    node = Publisher1()
    rclpy.spin(node)
    rclpy.shutdown() 

if __name__ == "__main__":
    main()



