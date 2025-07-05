from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PySide6.QtGui import QFont, QBrush, QColor


class AttendanceTab(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui  # truyền Ui_MainWindow từ file main

        # font va cac thuoc tinh khac 
        font = QFont("Roboto", 13)
        self.ui.table_attendance.setFont(font)

        header = self.ui.table_attendance.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(QHeaderView.Interactive) 
        header.resizeSection(0, 200)  # Cột 0: ID
        header.resizeSection(1, 200)  # Cột 1: Name
        header.resizeSection(2, 200)  # Cột 2: Department 
        header.resizeSection(3, 200)  # Cột 3: Status
        header.resizeSection(4, 240)  # Cột 4: email

        self.ui.table_attendance.horizontalHeader().setFixedHeight(40)
        self.ui.table_attendance.verticalHeader().setDefaultSectionSize(40)
        self.ui.table_attendance.setColumnCount(5)
        self.ui.table_attendance.setHorizontalHeaderLabels([
            "Employee ID", "Name", "Department", "Status", "Email"
        ])
               
        # Du lieu gia 
        self.attendance_data = [
            {"id": "E001", "name": "Alice", "dept": "HR", "email": "alice@example.com", "status": "Present"},
            {"id": "E002", "name": "Bob", "dept": "IT", "email": "bob@example.com", "status": "Absent"},
            {"id": "E003", "name": "Charlie", "dept": "Finance", "email": "charlie@example.com", "status": "Present"},
        ]

        # Gắn sự kiện nút tìm kiếm
        self.ui.search_btn.clicked.connect(self.search_attendance)

        # Hiển thị bảng ban đầu
        self.load_attendance_table(self.attendance_data)

    def load_attendance_table(self, data):
        self.ui.table_attendance.setRowCount(len(data))
        for row, entry in enumerate(data):
            self.ui.table_attendance.setItem(row, 0, QTableWidgetItem(entry["id"]))
            self.ui.table_attendance.setItem(row, 1, QTableWidgetItem(entry["name"]))
            self.ui.table_attendance.setItem(row, 2, QTableWidgetItem(entry["dept"]))
            self.ui.table_attendance.setItem(row, 4, QTableWidgetItem(entry["email"]))
        
            # Ô trạng thái (có phân biệt màu)
            status_item = QTableWidgetItem(entry["status"])

            if entry["status"].lower() == "present":
                status_item.setBackground(QBrush(QColor("#d0f5d6")))  # nền xanh nhạt
                status_item.setForeground(QBrush(QColor("#008000")))  # chữ xanh đậm
            else:
                status_item.setBackground(QBrush(QColor("#ffd6d6")))  # nền đỏ nhạt
                status_item.setForeground(QBrush(QColor("#cc0000")))  # chữ đỏ đậm

            self.ui.table_attendance.setItem(row, 3, status_item)  # cột status

    def search_attendance(self):
        id_text = self.ui.lineEdit.text().strip().lower()
        name_text = self.ui.lineEdit_2.text().strip().lower()
        dept_text = self.ui.lineEdit_3.text().strip().lower()
        email_text = self.ui.lineEdit_4.text().strip().lower()

        filtered = []
        for entry in self.attendance_data:
            if (id_text in entry["id"].lower() and
                name_text in entry["name"].lower() and
                dept_text in entry["dept"].lower() and
                email_text in entry["email"].lower()):
                filtered.append(entry)

        self.load_attendance_table(filtered)
