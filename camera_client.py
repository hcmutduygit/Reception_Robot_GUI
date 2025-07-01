import pickle, socket, struct, cv2

from PySide6.QtCore import Qt, QThread
from PySide6 import QtCore
from PySide6.QtGui import QImage

class SocketReceiver(QThread):
    ImageUpdate = QtCore.Signal(QImage)

    def __init__(self, target_label):
        super().__init__()
        self._active = True             # bien self._active là cờ báo chạy hay k  
        self.target_label = target_label    # gan cai khung hinh vo 
        self.client_socket = None

    def run(self):
        # create socket
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        host_ip = '127.0.1.1' # paste your server ip address here
        port = 9999
        self.client_socket.connect((host_ip,port)) # a tuple
        data = b""
        payload_size = struct.calcsize("Q")
        while self._active:
            while len(data) < payload_size:
                packet = self.client_socket.recv(4*1024) # 4K
                if not packet: 
                    self._active = False
                    break
                data+=packet
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q",packed_msg_size)[0]
            
            while len(data) < msg_size:
                data += self.client_socket.recv(4*1024)
            frame_data = data[:msg_size]
            data  = data[msg_size:]
            frame = pickle.loads(frame_data)
            
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb.shape
            img = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)

            # scale lai 
            label_width = self.target_label.width()
            label_height = self.target_label.height()
            scaled = img.scaled(label_width, label_height, Qt.KeepAspectRatio)

            self.ImageUpdate.emit(scaled)   # gui anh 
            
        self.client_socket.close()

    def stop(self):
        self._active = False
        if self.client_socket:
            try:
                self.client_socket.shutdown(socket.SHUT_RDWR)
                self.client_socket.close()
            except:
                pass
        self.quit()
        self.wait()