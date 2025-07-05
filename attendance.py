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
            {"id": "E001", "name": "Alice", "dept": "HR", "email": "alice@example.com", "status": None},
            {"id": "E002", "name": "Bob", "dept": "IT", "email": "bob@example.com", "status": None},
            {"id": "E003", "name": "Charlie", "dept": "Finance", "email": "charlie@example.com", "status": None},
        ]

        # Nhan du lieu tu MQTT va them vao data 
        self.id = "E002"
        self.status = "Present"
        self.update_status(id=self.id, status=self.status)

        # Gan nut search 
        self.ui.search_btn.clicked.connect(self.search_attendance)

        # Hien thi bang 
        self.load_attendance_table(self.attendance_data)

    # hien bang 
    def load_attendance_table(self, data):
        self.ui.table_attendance.setRowCount(len(data))
        for row, entry in enumerate(data):
            self.ui.table_attendance.setItem(row, 0, QTableWidgetItem(entry["id"]))
            self.ui.table_attendance.setItem(row, 1, QTableWidgetItem(entry["name"]))
            self.ui.table_attendance.setItem(row, 2, QTableWidgetItem(entry["dept"]))
            self.ui.table_attendance.setItem(row, 3, QTableWidgetItem(entry.get("status") or "—"))
            self.ui.table_attendance.setItem(row, 4, QTableWidgetItem(entry["email"]))
        
    # ham cap nhat trang thai 
    def update_status(self, id=None, status=None):
        for entry in self.attendance_data:
            if (id and entry["id"] == id):
                entry["status"] = status
                break

        self.load_attendance_table(self.attendance_data)

    # ham search 
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
