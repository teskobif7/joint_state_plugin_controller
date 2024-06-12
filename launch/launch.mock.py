from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                executable="mock",
                package="joint_state_plugin_controller",
                output="screen",
            ),
            Node(
                executable="controller",
                package="joint_state_plugin_controller",
                output="screen",
                parameters=[
                    {
                        "frequency": 10.0,
                        "plugin": "joint_state_plugin_controller.mock.CAN",
                        "params": ["interface=udp_multicast"],
                    }
                ],
            ),
        ]
    )
