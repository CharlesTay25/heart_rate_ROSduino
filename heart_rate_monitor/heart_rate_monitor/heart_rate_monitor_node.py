import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class HeartRateMonitorNode(Node):
    def __init__(self):
        super().__init__('heart_rate_monitor_node')
        self.get_logger().info(f'Heart rate node established')
        self.serial_port = '/dev/ttyACM0'  # Modify this to match your Arduino's serial port
        self.baud_rate = 115200  # Modify this to match your Arduino's baud rate
        self.serial = serial.Serial(self.serial_port, self.baud_rate)
        self.publisher = self.create_publisher(String, 'heart_rate', 10)
        self.serial_data_callback()

    def serial_data_callback(self):
        while rclpy.ok():
            received_data = self.serial.readline().decode().strip()
            #self.get_logger().info(f'Received heart rate: {received_data}')
            msg = String()
            msg.data = received_data
            self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = HeartRateMonitorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
