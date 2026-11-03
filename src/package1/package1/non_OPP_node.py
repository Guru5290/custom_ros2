import rclpy
from rclpy.node import Node

def main (args=None):
    #initialize the ROS2 python interface
    rclpy.init(args=args)
    node = Node("non_OOP") # creating an instance of the node
    node.get_logger().info("Node started!") #useful for debugging 
    rclpy.spin(node) #keep the node running untill when manually stopped
    node.destroy_node() #optional to destroy the node when finished
    rclpy.shutdown() #shutdown the ros2 python interface

if __name__ =='__main__':
    main()






    