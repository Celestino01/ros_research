import rclpy 
from rclpy.node import Node 

from example_interfaces.srv import AddTwoInts
from functools import partial

class NetflixClient(Node):
    def __init__(self):
        super().__init__("netflix_client")
        self.call_netflix_server(8, 4)
    
    def call_netflix_server(self, a, b):
        client = self.create_client(AddTwoInts, "netflix")

        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server")
        
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
            self.get_logger().info("Server Error %r" %(e,))

def main(args=None):
    rclpy.init(args=args)
    node = NetflixClient()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

