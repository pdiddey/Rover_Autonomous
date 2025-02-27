#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_bot_mini',              # Replace with your package name
            executable='transform_publisher.py',
            output='screen',
            parameters=[{'use_sim_time': True}]
        )
    ])
