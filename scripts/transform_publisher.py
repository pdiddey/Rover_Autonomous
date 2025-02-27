#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped

class StaticTransformSimPublisher(Node):
    def __init__(self):
        super().__init__('static_transform_sim_publisher')
        # Declare and use simulation time
        self.tf_broadcaster = TransformBroadcaster(self)
        # Publish at 10 Hz (adjust as needed)
        self.timer = self.create_timer(0.1, self.publish_transform)
        self.get_logger().info("Static transform publisher (sim time) started.")

    def publish_transform(self):
        t = TransformStamped()
        # Use the node's clock, which will be in sim time if use_sim_time is True
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "map"
        t.child_frame_id = "odom"
        # Identity transform: no translation or rotation
        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        self.tf_broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = StaticTransformSimPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
