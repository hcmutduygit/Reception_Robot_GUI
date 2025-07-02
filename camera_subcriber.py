import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import rclpy
from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtGui import QImage
from rclpy.executors import SingleThreadedExecutor

class CameraSubscriberThread(QThread):
    ImageUpdate = Signal(QImage)

    def __init__(self, target_label):
        super().__init__()
        self.target_label = target_label
        self._active = True

    def run(self):
        node = rclpy.create_node('camera_subscriber')
        executor = SingleThreadedExecutor()
        executor.add_node(node)
        bridge = CvBridge()

        def callback(msg):
            frame = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb.shape
            img = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)
            scaled = img.scaled(self.target_label.width(), self.target_label.height(), Qt.KeepAspectRatio)
            self.ImageUpdate.emit(scaled)

        sub = node.create_subscription(Image, 'webcam_image', callback, 10)

        try:
            while self._active:
                executor.spin_once(timeout_sec=0.1)
        finally:
            executor.shutdown()
            node.destroy_node()

    def stop(self):
        self._active = False
        self.quit()
        self.wait()
