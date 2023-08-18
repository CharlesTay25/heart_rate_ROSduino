import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSHistoryPolicy, QoSReliabilityPolicy, QoSDurabilityPolicy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String,Int32

class FingerDetector(Node):
    def __init__(self):
        super().__init__('finger_detector')

        qos_profile_stop = QoSProfile(
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=1,
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            durability=QoSDurabilityPolicy.TRANSIENT_LOCAL
        )   
        self.heartrate_subscriber = self.create_subscription(String, 'heart_rate', self.heartrate_callback, 10)
        self._publisher_stop = self.create_publisher(Int32, '/i069/robot_stop' , qos_profile_stop)


    def heartrate_callback(self,msg):
        data = msg.data  # Get the data from the message
        if "Avg BPM=" in data:
            pass

        elif "No finger?" in data:
            self.get_logger().info('No finger detected, stopping the robot..')
            self._publisher_stop.publish(Int32(data=-1))
        else:
            pass

def main(args=None):
    rclpy.init(args=args)
    finger_detect = FingerDetector()
    rclpy.spin(finger_detect)
    finger_detect.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
