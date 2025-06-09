import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
import cv2
import numpy as np

class RedCircleDetector(Node):
    def __init__(self):
        super().__init__('red_circle_detector')
        self.publisher_ = self.create_publisher(PoseStamped, 'detected_object_pose', 10)
        self.timer = self.create_timer(0.5, self.detect_red_circle)
        self.cap = cv2.VideoCapture(0)

    def detect_red_circle(self):
        ret, frame = self.cap.read()
        if not ret:
            return
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red = np.array([0, 120, 70])
        upper_red = np.array([10, 255, 255])
        mask = cv2.inRange(hsv, lower_red, upper_red)

        moments = cv2.moments(mask)
        if moments['m00'] > 0:
            cx = int(moments['m10']/moments['m00'])
            cy = int(moments['m01']/moments['m00'])

            # Here, map (cx, cy) to 3D space if possible (e.g., using camera calibration or a known z)
            pose = PoseStamped()
            pose.header.frame_id = "camera_link"
            pose.pose.position.x = float(cx) / 1000.0
            pose.pose.position.y = float(cy) / 1000.0
            pose.pose.position.z = 0.5  # Assume height from camera
            pose.pose.orientation.w = 1.0
            self.publisher_.publish(pose)
            self.get_logger().info(f"Published pose: {pose.pose.position}")

def main(args=None):
    rclpy.init(args=args)
    node = RedCircleDetector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
