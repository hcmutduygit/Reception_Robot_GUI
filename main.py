import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap

from robot_ui import Ui_MainWindow
# Hello world
from camera_client import SocketReceiver
from camera_server import CameraServer   

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Set the size
        self.resize(950, 630)

        # list user
        self.registered_users = [
    {
        "username": "admin",
        "password": "123",
        "fullname": "Admin User",
        "phone": "0123456789",
        "verify": "fablab"
    }
]
        self.camera_server = None

        # set moi vô thi hien cai nao 
        self.ui.Page.setCurrentWidget(self.ui.Page_signin)
        self.ui.Dashboard.setCurrentWidget(self.ui.Dashboard_signin)   

        # click sang tab khac thi chuyen trang 
        self.ui.Signin_btn_signup.clicked.connect(lambda: self.ui.Page.setCurrentWidget(self.ui.Page_signup))
        self.ui.Signin_btn_signin.clicked.connect(lambda: self.ui.Page.setCurrentWidget(self.ui.Page_signin))

        self.ui.Signin_btn_login.clicked.connect(self.handle_login)
        self.ui.Signup_btn_signup.clicked.connect(self.handle_signup)

        # click sang tab khac thi chuyen trang 
        self.ui.Main_btn_camera.clicked.connect(lambda: self.switch_to_page(self.ui.Page_Camera))
        self.ui.Main_btn_tracking.clicked.connect(lambda: self.switch_to_page(self.ui.Page_tracking))
        self.ui.Account__btnlogout.clicked.connect(self.handle_logout)

        # khoi tao camera
        self.camera_thread = None


    def handle_login(self):
        username = self.ui.Signin_username.text()
        password = self.ui.Signin_password.text()

        for user in self.registered_users:
            if user["username"] == username and user["password"] == password:
                self.switch_to_page(self.ui.Page_Camera)  # sang giao diện chính
                self.ui.Dashboard.setCurrentWidget(self.ui.Dashboard_main)
                return
        else:
            QMessageBox.warning(self, "Login Failed", "Incorrect username or password")
        
        
    def handle_signup(self):
        fullname = self.ui.Signup_name.text()
        phone    = self.ui.Signup_phone.text()
        username = self.ui.Signup_username.text()
        password = self.ui.Signup_password.text()
        verify   = self.ui.Signup_code.text()

        # da du truong thong tin chua?
        if not all([fullname, phone, username, password, verify]):
            QMessageBox.warning(self, "Sign Up Failed", "Please fill in all fields.")
            return

        # verify code?
        if verify.strip().lower() != "fablab":
            QMessageBox.warning(self, "Sign Up Failed", "Incorrect verification code.")
            return

        # co trung username?
        for user in self.registered_users:
            if user["username"] == username:
                QMessageBox.warning(self, "Sign Up Failed", "Username already exists.")
                return

        # Lưu lại nếu hợp lệ
        self.registered_users.append({
            "fullname": fullname,
            "phone": phone,
            "username": username,
            "password": password,
            "verify": verify
        })

        QMessageBox.information(self, "Success", "Account created successfully!")
        self.ui.Page.setCurrentWidget(self.ui.Page_signin)

    def handle_logout(self):
        # Tạo hộp thoại
        msg = QMessageBox(self)
        msg.setWindowTitle("Confirm Logout")
        msg.setText("Are you sure you want to log out?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setIcon(QMessageBox.Question)

        
        # van chua canh giua duoc, chi dam bao no nam trong frame 
        msg.adjustSize()
        main_rect = self.geometry()
        x = main_rect.x() + (main_rect.width() - msg.width()) // 2
        y = main_rect.y() + (main_rect.height() - msg.height()) // 2
        msg.move(x, y)

        # Hiển thị hộp thoại
        reply = msg.exec()

        if reply == QMessageBox.Yes:
            self.ui.Page.setCurrentWidget(self.ui.Page_signin)
            self.ui.Dashboard.setCurrentWidget(self.ui.Dashboard_signin)
        
    
    def switch_to_page(self, page_widget):
        self.ui.Page.setCurrentWidget(page_widget)

        # dung cac process dang chay 
        self.stop_camera()

        # Bật process phù hợp
        page_handlers = {
            self.ui.Page_Camera: self.start_camera,
            #self.ui.Page_tracking: self.start_tracking,...
        }

        handler = page_handlers.get(page_widget)
        if handler:
            handler()


    def start_camera(self):
        self.stop_camera()
        if not self.camera_server:
            self.camera_server = CameraServer()
            self.camera_server.start()
        # khoi tao camera dua tren class SocketReceiver
        # if not self.camera_thread:
        self.camera_thread = SocketReceiver(self.ui.camera_label)
        self.camera_thread.ImageUpdate.connect(self.update_camera_frame)
        self.camera_thread.start()

    def stop_camera(self):
        # xoa camera de lan sau gan lai va start lai 
        if self.camera_thread:
            self.camera_thread.stop()
            self.camera_thread = None

    def update_camera_frame(self, image):
        # hien thi len QLabel trong ui 
        self.ui.camera_label.setPixmap(QPixmap.fromImage(image))

    def closeEvent(self, event):
        self.stop_camera()
        event.accept()  



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
