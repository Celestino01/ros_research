import rclpy 
from rclpy.node import Node 

from my_robot_interfaces.msg import TargetCoordinates
from example_interfaces.msg import Int64

class Publisher2(Node):
    def __init__(self):
        super().__init__("publisher_2")

        #Publisher 
        self.publisher_ = self.create_publisher(TargetCoordinates, "my_position", 10)

        #Subscriber
        self.subscriber_= self.create_subscription(Int64, "control", self.subscriber_msg, 10)

    def subscriber_msg(self, msg):
        self.get_logger().info(str(msg.data))
        
        msgg = TargetCoordinates()

        msgg.x = float(msg.data)
        msgg.y = float(msg.data)
        msgg.z = float(msg.data)

        self.publisher_.publish(msgg)

def main(args = None):
    rclpy.init()
    node = Publisher2()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()