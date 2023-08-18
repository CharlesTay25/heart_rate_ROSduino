from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    heart_rate_node = Node(
        package='heart_rate_monitor',
        executable='heart_rate',
        output='screen',
    )

    finger_detect_node = Node(
        package='heart_rate_monitor',
        executable='finger_detect',
        output='screen',
    )
    return LaunchDescription([
        heart_rate_node,
        finger_detect_node
    ])
