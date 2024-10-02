import rclpy 
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

class MicrosoftServer(Node):
    def __init__(self):
        super().__init__("microsoft_server")
        self.server_ = self.create_service(AddTwoInts, "microsoft", self.callback_func)
        self.get_logger().info("Server is Active")

    def callback_func(self, request, response):
        response.sum = request.a + request.b 
        self.get_logger().info(f"{request.a} + {request.b} = {response.sum}")

        return response
    
def main(args=None):
    rclpy.init(args=args)
    node = MicrosoftServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()