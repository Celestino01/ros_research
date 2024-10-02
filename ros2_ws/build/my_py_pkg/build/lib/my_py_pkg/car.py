import rclpy
from rclpy.node import Node
from example_interfaces.msg import String 

class Car(Node):
    def __init__(self):
        super().__init__("car")
        
        #Subscriber
        self.subscriber_ = self.create_subscription(String, "Hot_97", self.radio_station_callback, 10)
        self.get_logger().info("The Car is now listening to the radio")


    def radio_station_callback(self, msg):
        self.get_logger().info(msg.data)

def main(args = None):
    rclpy.init(args=args)
    node = Car()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__manin__":
    main()
        