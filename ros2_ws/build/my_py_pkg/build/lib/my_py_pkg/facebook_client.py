import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial

class FacebookClient(Node):
    def __init__(self):
        super().__init__("facebook_client")
        self.call_facebook_server(3,4)

    def call_facebook_server(self,a,b):
        client = self.create_client(AddTwoInts, "facebook")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for server")

        request = AddTwoInts.Request()
        request.a = a
        request.b = b 

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_facebook, a=a, b=b))

    def callback_facebook(self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info(f"{a} + {b} = {response.sum}")
        except Exception as e:
            self.get_logger().error("Server call Failed %r" % (e,))


def main(args=None):
    rclpy.init(args=args)
    node = FacebookClient()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()