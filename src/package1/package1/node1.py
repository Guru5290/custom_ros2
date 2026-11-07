#!/usr/bin/env python3
import csv
import time

import rclpy
from rclpy.node import Node

# from sensor_msgs.msg import Image
# import non_OPP_node


class ImageSubscriber(Node):
    def __init__(self):
        super().__init__("node1")
        # self.subscription = self.create_subscription()
        self.get_logger().info("Node Started")
        self.counter = 0
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Logging every one second")
        self.counter += 1
        self.value = str(self.counter)
        print(f"The counter now is: {self.counter}")
        with open(
            "/home/d/custom_ros2/data.csv", mode="a", encoding="UTF-8", newline=""
        ) as file:
            self.writer = csv.writer(file)
            self.data = [time.strftime("%H:%M:%S"), self.value]
            self.writer.writerow(self.data)


def main(args=None):
    rclpy.init(args=args)
    node = ImageSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
