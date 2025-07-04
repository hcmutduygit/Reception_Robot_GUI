import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import rclpy
from PySide6.QtCore import QThread
from rclpy.executors import SingleThreadedExecutor

class CameraPublisherThread(QThread):
    def __init__(self):
        super().__init__()
        self._active = True

    def run(self):
        node = rclpy.create_node('camera_publisher')
        executor = SingleThreadedExecutor()
        executor.add_node(node)
        publisher = node.create_publisher(Image, 'webcam_image', 10)
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        bridge = CvBridge()

        def publish():
            if self._active:
                ret, frame = cap.read()
                if ret:
                    msg = bridge.cv2_to_imgmsg(frame, encoding='bgr8')
                    publisher.publish(msg)

        timer = node.create_timer(0.03, publish)

        try:
            while self._active:
                executor.spin_once(timeout_sec=0.1)
        finally:
            cap.release()
            executor.shutdown()
            node.destroy_node()

    def stop(self):
        self._active = False
        self.quit()
        self.wait()