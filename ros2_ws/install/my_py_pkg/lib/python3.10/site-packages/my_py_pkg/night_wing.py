import rclpy
from rclpy.node import Node 
from example_interfaces.msg import String 

class NightWing(Node):
    def __init__ (self):
        super().__init__("night_wing")
        self.publisher_ = self.create_publisher(String, "gotham", 10)
        self.timer_ = self.create_timer(1, self.publish_night_wing)
        self.get_logger().info("Night Wing publisher is active")

    def publish_night_wing(self):
        msg = String()
        msg.data = "night wing"
        self.publisher_.publish(msg)

def main(args = None):
    rclpy.init(args=args)
    node = NightWing()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()



