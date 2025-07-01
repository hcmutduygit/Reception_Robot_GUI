import socket
import cv2
import pickle
import struct
import imutils
import threading

class CameraServer(threading.Thread):
    def __init__(self, host='0.0.0.0', port=9999):
        super().__init__(daemon=True)  # daemon để thread này không ngăn app thoát
        self.host = host
        self.port = port
        self.running = True
        self.server_socket = None
        self.vid = None

    def run(self):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(1)

            print(f"[SERVER] Listening at {(self.host, self.port)}")

            while self.running:
                print("[SERVER] Waiting for client connection...")
                self.server_socket.settimeout(1.0)
                try:
                    client_socket, addr = self.server_socket.accept()
                except socket.timeout:
                    continue

                print(f"[SERVER] Got connection from {addr}")
                self.handle_client(client_socket)

        except Exception as e:
            print(f"[SERVER ERROR] {e}")
        finally:
            self.cleanup()

    def handle_client(self, client_socket):
        self.vid = cv2.VideoCapture(0)
        while self.running and self.vid.isOpened():
            ret, frame = self.vid.read()
            if not ret:
                break

            frame = imutils.resize(frame, width=320)
            data = pickle.dumps(frame)
            message = struct.pack("Q", len(data)) + data

            try:
                client_socket.sendall(message)
            except (BrokenPipeError, ConnectionResetError):
                print("[SERVER] Client disconnected.")
                break

        client_socket.close()
        if self.vid:
            self.vid.release()

    def stop(self):
        self.running = False
        self.cleanup()

    def cleanup(self):
        if self.vid:
            self.vid.release()
        if self.server_socket:
            try:
                self.server_socket.close()
            except:
                pass
        print("[SERVER] Cleaned up and stopped.")
