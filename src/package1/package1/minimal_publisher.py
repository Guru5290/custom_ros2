import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class minimal_publisher(Node):
    def __init__(self):
        super().__init__('talk')
        self.publisher_ = self.create_publisher(String, 'communicator', 10)
        self.timer = self.create_timer(5, self.callback_func)
        self.i = 0

    def callback_func(self):
        msg = String()
        msg.data = 'Hello World: 'f"{self.i}"
        self.publisher_.publish(msg)
        self.get_logger().info("Publishing" f'{msg.data}')
        self.i+=1


def main(args=None):
    rclpy.init(args=args)
    talker = minimal_publisher()
    rclpy.spin(talker)
    talker.destroy_node()
    rclpy.shutdown()

if __name__ =='__main__':
    main()

