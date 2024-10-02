import rclpy 
from rclpy.node import Node 
from example_interfaces.msg import String 

class RadioStation(Node):
    def __init__(self):
        super().__init__("radio_station")

        #Publisher
        self.publisher_ =  self.create_publisher(String, "Hot_97", 10)
        self.timer_ = self.create_timer(1, self.radio_news)
        self.get_logger().info("Radio Station is now broad casting")

    def radio_news(self):
        msg = String()
        msg.data = "This is Funk Flex and I'm dropping bombs tonight"
        self.publisher_.publish(msg)

def main(args = None):
    rclpy.init(args=args)
    node = RadioStation()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
