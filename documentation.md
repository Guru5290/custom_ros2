# Getting Started With ROS2 From Scratch
## Prerequisites
-**Ubuntu Machine**
-**ROS2 installed**
-**Basic CLI Usage Knowledge**
## Table of contents
- [Commands](#commands)
- [Nodes](#nodes)
- [Packages](#packages)


## Basic Commands to use:

- `Ros2 topic list` : *Lists the topics you have running*
- `Ros2 node list` : *Lists the nodes you have running*
- `Ros2 topic list` -t : *Lists the topics alongside with the message type*
- `Ros2 topic echo <topic_name>` : *Shows the info being published to the topic* 
- `ros2 topic pub --once <topic_name> <message_type> "{format needed}"`:
    To know the message type check first using:
    `ros2 topic list -t` (Here you see the message type for the particular topic you want)
    Then:
    `ros2 interface show <message_type>`
    e.g for /geometry_msg/msg/Twist : `ros2 topic pub --once <topic_name> <message_type> "{linear: {x: value, y: value, z: value}, angular: {x: value, y: value, z: value}}"`

    To publish multiple times omit --once. 
How to create your first non-oop node:

import the necessary modules:
1. import rclpy
2. from rclpy.node import Node

Enter to your main function: Contains what you want to do (functionality):

1. Define the function using def main(args=None) # none args to provide flexibility in parameter passing
2. Initialize ROS2 python interface using rclpy.init(args=args) # takes arguments passed to the main function
3. Then create an instance of your node: node = Node("name of your node")
4. Spin the node using rclpy.spin(node) # ensures it is continuously running until when manually stoped
5. Optionally you can destroy the node by node.destroy()
6. Shut it down using node.shutdown()

7 For direct execution of the node: use if __name__ ('__main__'):
                                            main()

Ensures the node can be executed as a single script by executing whatever is under main() or if imported as a module to another script, it can be used to to call a specific function eg my_module.my_function()





