import rclpy 
from rclpy.node import Node 
from functools import partial
from example_interfaces.srv import AddTwoInts 


class GoogleClient(Node):
    def __init__(self):
        super().__init__("google_client") 
        self.call_google_server(7, 3)
        self.call_google_server(8, 11)
        self.call_google_server(6, 10)
    
    def call_google_server(self, a, b):
        client = self.create_client(AddTwoInts, "google") 

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
            self.get_logger().error("Service call failed %r" %(e,))

def main(args = None):
    rclpy.init(args=args)
    node = GoogleClient()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()