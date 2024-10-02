import rclpy 
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts
from functools import partial 

class MexicoClient(Node):
    def __init__(self):
        super().__init__("mexico_client")
        self.call_mexico_server(8,7)

    def call_mexico_server(self, a, b):
        client = self.create_client(AddTwoInts, "mexico")

        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for server")
        
        request = AddTwoInts.Request()
        request.a = a 
        request.b = b 

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_func, a=a, b=b))

    def callback_func(self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info(f"{a} + {b} = {response.sum}")
        except Exception as e:
            self.get_logger().info("Server Error %r",(e,))

def main(args = None):
    rclpy.init(args=args)
    node = MexicoClient()
    rclpy.spin(node)
    rclpy.shutdown 

if __name__ == "__main__":
    main()