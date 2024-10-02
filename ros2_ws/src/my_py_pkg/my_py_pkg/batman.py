import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class Batman(Node):

    def __init__(self):
        super().__init__("batman")

        #Publisher
        self.publisher_ = self.create_publisher(String, "gotham", 10)
        self.timer_ = self.create_timer(1, self.bat_news)
        self.get_logger().info("Batman Node is activated")

    def bat_news(self):
        msg = String()
        msg.data = "bat"
        self.publisher_.publish(msg)

def main(args = None):
    rclpy.init(args = args)
    node = Batman()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()


