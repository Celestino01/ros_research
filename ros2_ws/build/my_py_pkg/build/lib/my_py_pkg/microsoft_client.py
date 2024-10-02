import rclpy
from rclpy.node import Node
from functools import partial

from example_interfaces.srv import AddTwoInts

class MicrosoftClient(Node):
    def __init__(self):
        super().__init__("microsoft_client")
        self.call_microsoft_server(7, 9)
        self.call_microsoft_server(13, 9)
        self.call_microsoft_server(7, 10)

    def call_microsoft_server(self, a, b):
        client = self.create_client(AddTwoInts, "microsoft")

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
            self.get_logger().info("Server Error %r" % (e,))

def main(args=None):
    rclpy.init(args=args)
    node = MicrosoftClient()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()