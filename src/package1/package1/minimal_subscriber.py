import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class minimal_subscriber(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(String, 'communicator', self.listener_callback, 10)
        self.subscription # prevents unused variable warning


    def listener_callback(self, msg):
        self.get_logger().info("I heard: "f'{msg.data}')

def main(args=None):
    rclpy.init(args = args)
    minimal_sub = minimal_subscriber()
    rclpy.spin(minimal_sub)
    minimal_sub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
