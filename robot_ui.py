# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Robot_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
from resources import resources_rc
from resources import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(1440, 900)
        MainWindow.setMinimumSize(QSize(1440, 900))
        MainWindow.setMaximumSize(QSize(2340, 1080))
        font = QFont()
        font.setFamilies([u"Roboto"])
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/logo/icon_APP.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"font-family:  \"Roboto\";\n"
"}")
        MainWindow.setIconSize(QSize(0, 0))
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1440, 900))
        self.centralwidget.setMaximumSize(QSize(2340, 1080))
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Dashboard = QStackedWidget(self.centralwidget)
        self.Dashboard.setObjectName(u"Dashboard")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Dashboard.sizePolicy().hasHeightForWidth())
        self.Dashboard.setSizePolicy(sizePolicy)
        self.Dashboard.setMinimumSize(QSize(260, 900))
        self.Dashboard.setMaximumSize(QSize(350, 1080))
        self.Dashboard.setFont(font)
        self.Dashboard.setStyleSheet(u"*{\n"
"	background-color: rgb(0, 41, 77);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(197, 225, 248);\n"
"	color: rgb(159, 190, 252);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"border-radius:  0px;\n"
"text-align: left;\n"
"padding-left: 30px;\n"
"spacing: 10px;\n"
"}\n"
"")
        self.Dashboard.setFrameShape(QFrame.NoFrame)
        self.Dashboard.setFrameShadow(QFrame.Plain)
        self.Dashboard.setLineWidth(0)
        self.Dashboard_signin = QWidget()
        self.Dashboard_signin.setObjectName(u"Dashboard_signin")
        self.Dashboard_signin.setMinimumSize(QSize(260, 900))
        self.Dashboard_signin.setMaximumSize(QSize(350, 1080))
        self.Dashboard_signin.setStyleSheet(u"QWidget {\n"
"background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(4, 3, 47), stop:0.5 rgb(86, 80, 140), stop:1 rgb(114, 159, 207))\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.Dashboard_signin)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Signin_logo = QFrame(self.Dashboard_signin)
        self.Signin_logo.setObjectName(u"Signin_logo")
        self.Signin_logo.setMinimumSize(QSize(260, 150))
        self.Signin_logo.setMaximumSize(QSize(350, 170))
        self.Signin_logo.setStyleSheet(u"")
        self.Signin_logo.setFrameShape(QFrame.NoFrame)
        self.Signin_logo.setFrameShadow(QFrame.Plain)
        self.Signin_logo.setLineWidth(0)
        self.gridLayout_4 = QGridLayout(self.Signin_logo)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_4.setHorizontalSpacing(12)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(20, 25, 20, 20)
        self.Logo_fab = QLabel(self.Signin_logo)
        self.Logo_fab.setObjectName(u"Logo_fab")
        sizePolicy.setHeightForWidth(self.Logo_fab.sizePolicy().hasHeightForWidth())
        self.Logo_fab.setSizePolicy(sizePolicy)
        self.Logo_fab.setMinimumSize(QSize(50, 50))
        self.Logo_fab.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"border-radius:  15px;")
        self.Logo_fab.setPixmap(QPixmap(u":/logos/Fablab Logo-aftercut.png"))
        self.Logo_fab.setScaledContents(True)
        self.Logo_fab.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.Logo_fab, 0, 0, 1, 1)

        self.Logo_BK = QLabel(self.Signin_logo)
        self.Logo_BK.setObjectName(u"Logo_BK")
        sizePolicy.setHeightForWidth(self.Logo_BK.sizePolicy().hasHeightForWidth())
        self.Logo_BK.setSizePolicy(sizePolicy)
        self.Logo_BK.setMinimumSize(QSize(50, 50))
        self.Logo_BK.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"border-radius:  15px;")
        self.Logo_BK.setFrameShape(QFrame.NoFrame)
        self.Logo_BK.setPixmap(QPixmap(u":/logo/Logo BK.png"))
        self.Logo_BK.setScaledContents(True)
        self.Logo_BK.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.Logo_BK, 0, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 1)

        self.verticalLayout_3.addWidget(self.Signin_logo)

        self.Signin_line = QFrame(self.Dashboard_signin)
        self.Signin_line.setObjectName(u"Signin_line")
        self.Signin_line.setMinimumSize(QSize(260, 20))
        self.Signin_line.setMaximumSize(QSize(350, 20))
        self.Signin_line.setFrameShape(QFrame.NoFrame)
        self.Signin_line.setFrameShadow(QFrame.Raised)
        self.Signin_line.setLineWidth(0)
        self.gridLayout = QGridLayout(self.Signin_line)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Line = QFrame(self.Signin_line)
        self.Line.setObjectName(u"Line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Line.sizePolicy().hasHeightForWidth())
        self.Line.setSizePolicy(sizePolicy1)
        self.Line.setMinimumSize(QSize(210, 3))
        self.Line.setMaximumSize(QSize(250, 3))
        self.Line.setSizeIncrement(QSize(0, 0))
        self.Line.setLayoutDirection(Qt.LeftToRight)
        self.Line.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        self.Line.setFrameShape(QFrame.NoFrame)
        self.Line.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.Line, 0, 0, 1, 1, Qt.AlignHCenter)

        self.Line_2 = QFrame(self.Signin_line)
        self.Line_2.setObjectName(u"Line_2")
        self.Line_2.setMinimumSize(QSize(160, 3))
        self.Line_2.setMaximumSize(QSize(200, 3))
        self.Line_2.setLayoutDirection(Qt.LeftToRight)
        self.Line_2.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        self.Line_2.setFrameShape(QFrame.NoFrame)
        self.Line_2.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.Line_2, 1, 0, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.Signin_line)

        self.Signin_btn = QFrame(self.Dashboard_signin)
        self.Signin_btn.setObjectName(u"Signin_btn")
        self.Signin_btn.setMinimumSize(QSize(260, 660))
        self.Signin_btn.setMaximumSize(QSize(350, 820))
        self.Signin_btn.setStyleSheet(u"")
        self.Signin_btn.setFrameShape(QFrame.NoFrame)
        self.Signin_btn.setFrameShadow(QFrame.Raised)
        self.Signin_btn.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.Signin_btn)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 150, 0, 150)
        self.Signin_btn_signin = QPushButton(self.Signin_btn)
        self.Signin_btn_signin.setObjectName(u"Signin_btn_signin")
        self.Signin_btn_signin.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(24)
        font1.setBold(False)
        self.Signin_btn_signin.setFont(font1)
        self.Signin_btn_signin.setFocusPolicy(Qt.NoFocus)
        self.Signin_btn_signin.setStyleSheet(u"")
        self.Signin_btn_signin.setIconSize(QSize(35, 35))
        self.Signin_btn_signin.setAutoRepeat(True)
        self.Signin_btn_signin.setAutoExclusive(False)
        self.Signin_btn_signin.setAutoRepeatDelay(0)
        self.Signin_btn_signin.setAutoRepeatInterval(0)

        self.verticalLayout_2.addWidget(self.Signin_btn_signin)

        self.Signin_btn_signup = QPushButton(self.Signin_btn)
        self.Signin_btn_signup.setObjectName(u"Signin_btn_signup")
        self.Signin_btn_signup.setMaximumSize(QSize(16777215, 50))
        self.Signin_btn_signup.setFont(font1)
        self.Signin_btn_signup.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_2.addWidget(self.Signin_btn_signup)

        self.verticalLayout_2.setStretch(1, 1)
        self.Signin_btn_signup.raise_()
        self.Signin_btn_signin.raise_()

        self.verticalLayout_3.addWidget(self.Signin_btn)

        self.Signin_text = QLabel(self.Dashboard_signin)
        self.Signin_text.setObjectName(u"Signin_text")
        self.Signin_text.setMinimumSize(QSize(260, 70))
        self.Signin_text.setMaximumSize(QSize(350, 70))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setItalic(True)
        self.Signin_text.setFont(font2)
        self.Signin_text.setLayoutDirection(Qt.LeftToRight)
        self.Signin_text.setStyleSheet(u"")
        self.Signin_text.setScaledContents(False)
        self.Signin_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.Signin_text, 0, Qt.AlignBottom)

        self.verticalLayout_3.setStretch(0, 170)
        self.verticalLayout_3.setStretch(1, 20)
        self.verticalLayout_3.setStretch(2, 820)
        self.verticalLayout_3.setStretch(3, 70)
        self.Dashboard.addWidget(self.Dashboard_signin)
        self.Dashboard_main = QWidget()
        self.Dashboard_main.setObjectName(u"Dashboard_main")
        sizePolicy.setHeightForWidth(self.Dashboard_main.sizePolicy().hasHeightForWidth())
        self.Dashboard_main.setSizePolicy(sizePolicy)
        self.Dashboard_main.setMinimumSize(QSize(240, 900))
        self.Dashboard_main.setMaximumSize(QSize(16777215, 1080))
        self.Dashboard_main.setFont(font)
        self.Dashboard_main.setStyleSheet(u"QWidget {\n"
"background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(4, 3, 47), stop:0.5 rgb(86, 80, 140), stop:1 rgb(114, 159, 207))\n"
"}")
        self.verticalLayout = QVBoxLayout(self.Dashboard_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Main_Logo = QFrame(self.Dashboard_main)
        self.Main_Logo.setObjectName(u"Main_Logo")
        self.Main_Logo.setMinimumSize(QSize(260, 150))
        self.Main_Logo.setMaximumSize(QSize(260, 120))
        self.Main_Logo.setStyleSheet(u"")
        self.Main_Logo.setFrameShape(QFrame.NoFrame)
        self.Main_Logo.setFrameShadow(QFrame.Plain)
        self.Main_Logo.setLineWidth(0)
        self.gridLayout_5 = QGridLayout(self.Main_Logo)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_5.setHorizontalSpacing(12)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(20, 25, 20, 20)
        self.Logo_fab_2 = QLabel(self.Main_Logo)
        self.Logo_fab_2.setObjectName(u"Logo_fab_2")
        sizePolicy.setHeightForWidth(self.Logo_fab_2.sizePolicy().hasHeightForWidth())
        self.Logo_fab_2.setSizePolicy(sizePolicy)
        self.Logo_fab_2.setMinimumSize(QSize(50, 50))
        self.Logo_fab_2.setMaximumSize(QSize(100, 100))
        self.Logo_fab_2.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"border-radius:  15px;")
        self.Logo_fab_2.setPixmap(QPixmap(u":/logos/Fablab Logo-aftercut.png"))
        self.Logo_fab_2.setScaledContents(True)
        self.Logo_fab_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.Logo_fab_2, 0, 0, 1, 1)

        self.Logo_BK_2 = QLabel(self.Main_Logo)
        self.Logo_BK_2.setObjectName(u"Logo_BK_2")
        sizePolicy.setHeightForWidth(self.Logo_BK_2.sizePolicy().hasHeightForWidth())
        self.Logo_BK_2.setSizePolicy(sizePolicy)
        self.Logo_BK_2.setMinimumSize(QSize(50, 50))
        self.Logo_BK_2.setMaximumSize(QSize(100, 100))
        self.Logo_BK_2.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"border-radius:  15px;")
        self.Logo_BK_2.setPixmap(QPixmap(u":/logo/Logo BK.png"))
        self.Logo_BK_2.setScaledContents(True)
        self.Logo_BK_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.Logo_BK_2, 0, 1, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 1)

        self.verticalLayout.addWidget(self.Main_Logo)

        self.Main_btn = QFrame(self.Dashboard_main)
        self.Main_btn.setObjectName(u"Main_btn")
        sizePolicy.setHeightForWidth(self.Main_btn.sizePolicy().hasHeightForWidth())
        self.Main_btn.setSizePolicy(sizePolicy)
        self.Main_btn.setMinimumSize(QSize(260, 200))
        self.Main_btn.setMaximumSize(QSize(260, 770))
        self.Main_btn.setFont(font)
        self.Main_btn.setStyleSheet(u"QPushButton#Main_btn_orders{ \n"
"background-color: rgb(216, 229, 254);\n"
" color: rgb(0, 41, 77); \n"
"}")
        self.Main_btn.setFrameShape(QFrame.NoFrame)
        self.Main_btn.setFrameShadow(QFrame.Raised)
        self.Main_btn.setLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.Main_btn)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Main_line = QFrame(self.Main_btn)
        self.Main_line.setObjectName(u"Main_line")
        self.Main_line.setMinimumSize(QSize(260, 20))
        self.Main_line.setMaximumSize(QSize(350, 20))
        self.Main_line.setContextMenuPolicy(Qt.NoContextMenu)
        self.Main_line.setFrameShape(QFrame.NoFrame)
        self.Main_line.setFrameShadow(QFrame.Raised)
        self.Main_line.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.Main_line)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.Line_3 = QFrame(self.Main_line)
        self.Line_3.setObjectName(u"Line_3")
        sizePolicy.setHeightForWidth(self.Line_3.sizePolicy().hasHeightForWidth())
        self.Line_3.setSizePolicy(sizePolicy)
        self.Line_3.setMaximumSize(QSize(16777215, 3))
        self.Line_3.setSizeIncrement(QSize(0, 0))
        self.Line_3.setLayoutDirection(Qt.LeftToRight)
        self.Line_3.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        self.Line_3.setFrameShape(QFrame.NoFrame)
        self.Line_3.setFrameShadow(QFrame.Raised)
        self.Line_3.setLineWidth(3)

        self.horizontalLayout_2.addWidget(self.Line_3)


        self.verticalLayout_6.addWidget(self.Main_line)

        self.Main__frame_admin = QFrame(self.Main_btn)
        self.Main__frame_admin.setObjectName(u"Main__frame_admin")
        self.Main__frame_admin.setMaximumSize(QSize(260, 300))
        self.Main__frame_admin.setFrameShape(QFrame.NoFrame)
        self.Main__frame_admin.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Main__frame_admin)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Label_admin = QLabel(self.Main__frame_admin)
        self.Label_admin.setObjectName(u"Label_admin")
        self.Label_admin.setMinimumSize(QSize(0, 20))
        self.Label_admin.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(19)
        self.Label_admin.setFont(font3)
        self.Label_admin.setStyleSheet(u"color: rgb(101, 230, 248);\n"
"margin-left: 10px;\n"
"")
        self.Label_admin.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Label_admin.setMargin(0)

        self.verticalLayout_8.addWidget(self.Label_admin)

        self.Main_btn_attendance = QPushButton(self.Main__frame_admin)
        self.Main_btn_attendance.setObjectName(u"Main_btn_attendance")
        self.Main_btn_attendance.setMinimumSize(QSize(0, 40))
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(18)
        self.Main_btn_attendance.setFont(font4)
        self.Main_btn_attendance.setFocusPolicy(Qt.NoFocus)
        self.Main_btn_attendance.setFlat(True)

        self.verticalLayout_8.addWidget(self.Main_btn_attendance)

        self.Main_btn_camera = QPushButton(self.Main__frame_admin)
        self.Main_btn_camera.setObjectName(u"Main_btn_camera")
        self.Main_btn_camera.setMinimumSize(QSize(0, 40))
        self.Main_btn_camera.setFont(font4)
        self.Main_btn_camera.setFocusPolicy(Qt.NoFocus)
        self.Main_btn_camera.setFlat(True)

        self.verticalLayout_8.addWidget(self.Main_btn_camera)

        self.Main_btn_tracking = QPushButton(self.Main__frame_admin)
        self.Main_btn_tracking.setObjectName(u"Main_btn_tracking")
        self.Main_btn_tracking.setMinimumSize(QSize(0, 40))
        self.Main_btn_tracking.setFont(font4)
        self.Main_btn_tracking.setFocusPolicy(Qt.NoFocus)
        self.Main_btn_tracking.setFlat(True)

        self.verticalLayout_8.addWidget(self.Main_btn_tracking)


        self.verticalLayout_6.addWidget(self.Main__frame_admin)

        self.Main_frame_admin = QFrame(self.Main_btn)
        self.Main_frame_admin.setObjectName(u"Main_frame_admin")
        self.Main_frame_admin.setMaximumSize(QSize(260, 200))
        self.Main_frame_admin.setFrameShape(QFrame.NoFrame)
        self.Main_frame_admin.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.Main_frame_admin)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Account_username = QLabel(self.Main_frame_admin)
        self.Account_username.setObjectName(u"Account_username")
        self.Account_username.setMinimumSize(QSize(0, 20))
        self.Account_username.setMaximumSize(QSize(16777215, 30))
        self.Account_username.setFont(font4)
        self.Account_username.setStyleSheet(u"color: rgb(101, 230, 248);\n"
"margin-left: 10px;\n"
"")
        self.Account_username.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Account_username.setMargin(0)

        self.verticalLayout_9.addWidget(self.Account_username)

        self.Account__btnlogout = QPushButton(self.Main_frame_admin)
        self.Account__btnlogout.setObjectName(u"Account__btnlogout")
        self.Account__btnlogout.setMinimumSize(QSize(0, 40))
        self.Account__btnlogout.setFont(font4)
        self.Account__btnlogout.setFocusPolicy(Qt.NoFocus)
        self.Account__btnlogout.setFlat(True)

        self.verticalLayout_9.addWidget(self.Account__btnlogout)


        self.verticalLayout_6.addWidget(self.Main_frame_admin)


        self.verticalLayout.addWidget(self.Main_btn)

        self.Dashboard.addWidget(self.Dashboard_main)

        self.horizontalLayout.addWidget(self.Dashboard)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(240, 246, 255);")
        self.verticalLayout_16 = QVBoxLayout(self.widget)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 20))
        self.frame_3.setStyleSheet(u"\n"
"color: rgb(0, 41, 77);")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(2)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.label_battery = QLabel(self.frame_3)
        self.label_battery.setObjectName(u"label_battery")
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setBold(True)
        self.label_battery.setFont(font5)

        self.horizontalLayout_7.addWidget(self.label_battery)


        self.verticalLayout_16.addWidget(self.frame_3)

        self.Page = QStackedWidget(self.widget)
        self.Page.setObjectName(u"Page")
        self.Page.setMinimumSize(QSize(1180, 900))
        self.Page.setMaximumSize(QSize(1995, 1080))
        self.Page.setStyleSheet(u"background-color: rgb(240, 246, 255);")
        self.Page.setFrameShadow(QFrame.Raised)
        self.Page.setLineWidth(0)
        self.Page_signin = QWidget()
        self.Page_signin.setObjectName(u"Page_signin")
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(9)
        font6.setBold(False)
        self.Page_signin.setFont(font6)
        self.Page_signin.setStyleSheet(u"background-color: rgb(240, 246, 255);")
        self.gridLayout_2 = QGridLayout(self.Page_signin)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Sigin_form = QFrame(self.Page_signin)
        self.Sigin_form.setObjectName(u"Sigin_form")
        self.Sigin_form.setMaximumSize(QSize(720, 360))
        self.Sigin_form.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.Sigin_form.setFrameShape(QFrame.NoFrame)
        self.Sigin_form.setFrameShadow(QFrame.Raised)
        self.Sigin_form.setLineWidth(5)
        self.formLayout_2 = QFormLayout(self.Sigin_form)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.formLayout_2.setFormAlignment(Qt.AlignCenter)
        self.formLayout_2.setHorizontalSpacing(0)
        self.formLayout_2.setVerticalSpacing(0)
        self.formLayout_2.setContentsMargins(0, 0, 0, 25)
        self.Title = QFrame(self.Sigin_form)
        self.Title.setObjectName(u"Title")
        self.Title.setMinimumSize(QSize(720, 80))
        self.Title.setMaximumSize(QSize(720, 80))
        self.Title.setStyleSheet(u"color: rgb(0, 41, 77);")
        self.Title.setFrameShape(QFrame.NoFrame)
        self.Title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Title)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.Title)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(720, 0))
        self.label_2.setMaximumSize(QSize(720, 100))
        font7 = QFont()
        font7.setFamilies([u"Roboto"])
        font7.setPointSize(26)
        font7.setBold(True)
        self.label_2.setFont(font7)
        self.label_2.setFocusPolicy(Qt.TabFocus)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.label_4 = QLabel(self.Title)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMinimumSize(QSize(720, 0))
        self.label_4.setMaximumSize(QSize(720, 100))
        font8 = QFont()
        font8.setFamilies([u"Roboto"])
        font8.setPointSize(15)
        font8.setBold(False)
        font8.setItalic(True)
        self.label_4.setFont(font8)
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_4)


        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.Title)

        self.Frame_btnlogin = QFrame(self.Sigin_form)
        self.Frame_btnlogin.setObjectName(u"Frame_btnlogin")
        self.Frame_btnlogin.setMinimumSize(QSize(720, 60))
        self.Frame_btnlogin.setMaximumSize(QSize(720, 60))
        self.Frame_btnlogin.setFrameShape(QFrame.StyledPanel)
        self.Frame_btnlogin.setFrameShadow(QFrame.Raised)
        self.Signin_btn_login = QPushButton(self.Frame_btnlogin)
        self.Signin_btn_login.setObjectName(u"Signin_btn_login")
        self.Signin_btn_login.setGeometry(QRect(285, 10, 150, 50))
        self.Signin_btn_login.setMinimumSize(QSize(150, 50))
        self.Signin_btn_login.setMaximumSize(QSize(150, 50))
        font9 = QFont()
        font9.setFamilies([u"Roboto"])
        font9.setPointSize(17)
        font9.setBold(False)
        font9.setItalic(False)
        self.Signin_btn_login.setFont(font9)
        self.Signin_btn_login.setFocusPolicy(Qt.WheelFocus)
        self.Signin_btn_login.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(0, 41, 77);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(216, 229, 254);\n"
"	color: rgb(0, 41, 77);\n"
"}")
        self.Signin_btn_login.setAutoDefault(True)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.Frame_btnlogin)

        self.LineEdit_sigin = QFrame(self.Sigin_form)
        self.LineEdit_sigin.setObjectName(u"LineEdit_sigin")
        self.LineEdit_sigin.setMinimumSize(QSize(720, 170))
        self.LineEdit_sigin.setMaximumSize(QSize(720, 170))
        self.LineEdit_sigin.setFrameShape(QFrame.StyledPanel)
        self.LineEdit_sigin.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.LineEdit_sigin)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Signin_username = QLineEdit(self.LineEdit_sigin)
        self.Signin_username.setObjectName(u"Signin_username")
        sizePolicy.setHeightForWidth(self.Signin_username.sizePolicy().hasHeightForWidth())
        self.Signin_username.setSizePolicy(sizePolicy)
        self.Signin_username.setMinimumSize(QSize(500, 50))
        self.Signin_username.setMaximumSize(QSize(500, 50))
        font10 = QFont()
        font10.setFamilies([u"Roboto"])
        font10.setPointSize(17)
        font10.setBold(False)
        self.Signin_username.setFont(font10)
        self.Signin_username.setFocusPolicy(Qt.StrongFocus)
        self.Signin_username.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 41, 77);")
        self.Signin_username.setAlignment(Qt.AlignCenter)
        self.Signin_username.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.Signin_username.setClearButtonEnabled(False)

        self.verticalLayout_10.addWidget(self.Signin_username, 0, Qt.AlignHCenter)

        self.Signin_password = QLineEdit(self.LineEdit_sigin)
        self.Signin_password.setObjectName(u"Signin_password")
        sizePolicy.setHeightForWidth(self.Signin_password.sizePolicy().hasHeightForWidth())
        self.Signin_password.setSizePolicy(sizePolicy)
        self.Signin_password.setMinimumSize(QSize(500, 50))
        self.Signin_password.setMaximumSize(QSize(500, 50))
        font11 = QFont()
        font11.setFamilies([u"Roboto"])
        font11.setPointSize(17)
        self.Signin_password.setFont(font11)
        self.Signin_password.setFocusPolicy(Qt.StrongFocus)
        self.Signin_password.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 41, 77);")
        self.Signin_password.setEchoMode(QLineEdit.Password)
        self.Signin_password.setAlignment(Qt.AlignCenter)
        self.Signin_password.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.Signin_password.setClearButtonEnabled(True)

        self.verticalLayout_10.addWidget(self.Signin_password, 0, Qt.AlignHCenter)


        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.LineEdit_sigin)


        self.gridLayout_2.addWidget(self.Sigin_form, 0, 0, 1, 1)

        self.Page.addWidget(self.Page_signin)
        self.Page_signup = QWidget()
        self.Page_signup.setObjectName(u"Page_signup")
        self.Page_signup.setStyleSheet(u"background-color: rgb(240, 246, 255);")
        self.gridLayout_3 = QGridLayout(self.Page_signup)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Signup_form = QFrame(self.Page_signup)
        self.Signup_form.setObjectName(u"Signup_form")
        self.Signup_form.setMaximumSize(QSize(720, 650))
        self.Signup_form.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.Signup_form.setFrameShape(QFrame.NoFrame)
        self.Signup_form.setFrameShadow(QFrame.Raised)
        self.Signup_form.setLineWidth(5)
        self.formLayout = QFormLayout(self.Signup_form)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, -1, 0)
        self.Title_signup = QLabel(self.Signup_form)
        self.Title_signup.setObjectName(u"Title_signup")
        sizePolicy2.setHeightForWidth(self.Title_signup.sizePolicy().hasHeightForWidth())
        self.Title_signup.setSizePolicy(sizePolicy2)
        self.Title_signup.setMinimumSize(QSize(720, 70))
        self.Title_signup.setMaximumSize(QSize(720, 70))
        self.Title_signup.setFont(font7)
        self.Title_signup.setScaledContents(False)
        self.Title_signup.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.Title_signup)

        self.LineEdit_signup = QFrame(self.Signup_form)
        self.LineEdit_signup.setObjectName(u"LineEdit_signup")
        self.LineEdit_signup.setMinimumSize(QSize(720, 500))
        self.LineEdit_signup.setMaximumSize(QSize(720, 500))
        self.LineEdit_signup.setFrameShape(QFrame.StyledPanel)
        self.LineEdit_signup.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.LineEdit_signup)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(110, 0, 0, -1)
        self.Signup_name = QLineEdit(self.LineEdit_signup)
        self.Signup_name.setObjectName(u"Signup_name")
        sizePolicy.setHeightForWidth(self.Signup_name.sizePolicy().hasHeightForWidth())
        self.Signup_name.setSizePolicy(sizePolicy)
        self.Signup_name.setMinimumSize(QSize(500, 50))
        self.Signup_name.setMaximumSize(QSize(500, 50))
        self.Signup_name.setFont(font10)
        self.Signup_name.setFocusPolicy(Qt.StrongFocus)
        self.Signup_name.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 41, 77);")
        self.Signup_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.Signup_name)

        self.Signup_phone = QLineEdit(self.LineEdit_signup)
        self.Signup_phone.setObjectName(u"Signup_phone")
        sizePolicy.setHeightForWidth(self.Signup_phone.sizePolicy().hasHeightForWidth())
        self.Signup_phone.setSizePolicy(sizePolicy)
        self.Signup_phone.setMinimumSize(QSize(500, 50))
        self.Signup_phone.setMaximumSize(QSize(500, 50))
        self.Signup_phone.setFont(font11)
        self.Signup_phone.setFocusPolicy(Qt.StrongFocus)
        self.Signup_phone.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 41, 77);")
        self.Signup_phone.setEchoMode(QLineEdit.Normal)
        self.Signup_phone.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.Signup_phone)

        self.Signup_username = QLineEdit(self.LineEdit_signup)
        self.Signup_username.setObjectName(u"Signup_username")
        sizePolicy.setHeightForWidth(self.Signup_username.sizePolicy().hasHeightForWidth())
        self.Signup_username.setSizePolicy(sizePolicy)
        self.Signup_username.setMinimumSize(QSize(500, 50))
        self.Signup_username.setMaximumSize(QSize(500, 50))
        self.Signup_username.setFont(font11)
        self.Signup_username.setFocusPolicy(Qt.StrongFocus)
        self.Signup_username.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 41, 77);")
        self.Signup_username.setEchoMode(QLineEdit.Normal)
        self.Signup_username.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.Signup_username)

        self.Signup_password = QLineEdit(self.LineEdit_signup)
        self.Signup_password.setObjectName(u"Signup_password")
        sizePolicy.setHeightForWidth(self.Signup_password.sizePolicy().hasHeightForWidth())
        self.Signup_password.setSizePolicy(sizePolicy)
        self.Signup_password.setMinimumSize(QSize(500, 50))
        self.Signup_password.setMaximumSize(QSize(500, 50))
        self.Signup_password.setFont(font11)
        self.Signup_password.setFocusPolicy(Qt.StrongFocus)
        self.Signup_password.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 41, 77);")
        self.Signup_password.setEchoMode(QLineEdit.Password)
        self.Signup_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.Signup_password)

        self.Signup_code = QLineEdit(self.LineEdit_signup)
        self.Signup_code.setObjectName(u"Signup_code")
        sizePolicy.setHeightForWidth(self.Signup_code.sizePolicy().hasHeightForWidth())
        self.Signup_code.setSizePolicy(sizePolicy)
        self.Signup_code.setMinimumSize(QSize(500, 50))
        self.Signup_code.setMaximumSize(QSize(500, 50))
        self.Signup_code.setFont(font10)
        self.Signup_code.setFocusPolicy(Qt.StrongFocus)
        self.Signup_code.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 41, 77);")
        self.Signup_code.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.Signup_code)


        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.LineEdit_signup)

        self.Frame_btn_signup = QFrame(self.Signup_form)
        self.Frame_btn_signup.setObjectName(u"Frame_btn_signup")
        self.Frame_btn_signup.setMinimumSize(QSize(720, 80))
        self.Frame_btn_signup.setMaximumSize(QSize(720, 80))
        self.Frame_btn_signup.setFrameShape(QFrame.StyledPanel)
        self.Frame_btn_signup.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.Frame_btn_signup)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(235, 0, 0, 0)
        self.Signup_btn_signup = QPushButton(self.Frame_btn_signup)
        self.Signup_btn_signup.setObjectName(u"Signup_btn_signup")
        self.Signup_btn_signup.setMinimumSize(QSize(250, 50))
        self.Signup_btn_signup.setMaximumSize(QSize(250, 50))
        self.Signup_btn_signup.setFont(font9)
        self.Signup_btn_signup.setFocusPolicy(Qt.TabFocus)
        self.Signup_btn_signup.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(0, 41, 77);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(216, 229, 254);\n"
"	color: rgb(0, 41, 77);\n"
"}")
        self.Signup_btn_signup.setFlat(True)

        self.verticalLayout_12.addWidget(self.Signup_btn_signup)


        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.Frame_btn_signup)


        self.gridLayout_3.addWidget(self.Signup_form, 0, 0, 1, 1)

        self.Page.addWidget(self.Page_signup)
        self.Page_orders = QWidget()
        self.Page_orders.setObjectName(u"Page_orders")
        self.verticalLayout_13 = QVBoxLayout(self.Page_orders)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Page.addWidget(self.Page_orders)
        self.Page_robots = QWidget()
        self.Page_robots.setObjectName(u"Page_robots")
        self.verticalLayout_14 = QVBoxLayout(self.Page_robots)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.Page.addWidget(self.Page_robots)
        self.Page_tracking = QWidget()
        self.Page_tracking.setObjectName(u"Page_tracking")
        self.Page_tracking.setStyleSheet(u"*{\n"
"background-color: rgb(240, 246, 255);\n"
"}\n"
"#menu_tracking {\n"
"border: 1px solid gray;\n"
"}\n"
"QPushButton{\n"
"border-radius:none;\n"
"color: rgb(186, 189, 182);\n"
"}\n"
"QPushButton:hover{\n"
";\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.gridLayout_6 = QGridLayout(self.Page_tracking)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.menu_tracking = QFrame(self.Page_tracking)
        self.menu_tracking.setObjectName(u"menu_tracking")
        self.menu_tracking.setMinimumSize(QSize(0, 100))
        self.menu_tracking.setMaximumSize(QSize(16777215, 100))
        self.menu_tracking.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.menu_tracking.setFrameShape(QFrame.NoFrame)
        self.menu_tracking.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.menu_tracking)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_26 = QLabel(self.menu_tracking)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 70))
        self.label_26.setMaximumSize(QSize(16777215, 70))
        font12 = QFont()
        font12.setFamilies([u"Roboto"])
        font12.setBold(True)
        font12.setItalic(False)
        font12.setUnderline(False)
        font12.setStrikeOut(False)
        font12.setKerning(True)
        self.label_26.setFont(font12)
        self.label_26.setStyleSheet(u"font-size: 40px;\n"
"")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_26)


        self.gridLayout_6.addWidget(self.menu_tracking, 0, 0, 1, 1)

        self.tracking = QVBoxLayout()
        self.tracking.setObjectName(u"tracking")
        self.traking_label = QLabel(self.Page_tracking)
        self.traking_label.setObjectName(u"traking_label")
        self.traking_label.setAlignment(Qt.AlignCenter)

        self.tracking.addWidget(self.traking_label)


        self.gridLayout_6.addLayout(self.tracking, 1, 0, 1, 1)

        self.Page.addWidget(self.Page_tracking)
        self.Page_attendance = QWidget()
        self.Page_attendance.setObjectName(u"Page_attendance")
        self.Page_attendance.setStyleSheet(u"*{\n"
"background-color: rgb(240, 246, 255);\n"
"}\n"
"#menu_attendance {\n"
"	border: 1px solid gray;\n"
"} \n"
"#info_frame QLineEdit,\n"
"#info_frame QComboBox {\n"
"	padding: 4px 5px;\n"
"	border: 1px solid #838383;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"#info_frame QLineEdit:focus,\n"
"#info_frame QComboBox:focus\n"
" {\n"
"	border-color: #0055ff;\n"
"}\n"
"\n"
"QComboBox::drop-down { \n"
"	background: transparent; \n"
"	border: none;\n"
"	margin-right: 5px;\n"
"} \n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/icons/icons/expand_more.svg);\n"
"}\n"
"\n"
"#info_frame QPushButton {\n"
"	font-size: 14px;\n"
"	padding: 5px 10px;\n"
"	border: 2px solid #f0f0f0;\n"
"	border-radius: 5px;\n"
"	background-color: #84e8f7;\n"
"}\n"
"\n"
"#info_frame QPushButton:hover {\n"
"	border-color: #4c96f7;\n"
"	font-size: 15px;\n"
"}\n"
"#result_frame {\n"
"	border-radius: 5px;\n"
"}\n"
"QTableWidget::Item{\n"
"	border-bottom:1px solid #d0c6ff;\n"
"	color: black;\n"
"	padding-left: 3px;\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.Page_attendance)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.Page_attendance)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_15 = QVBoxLayout(self.widget_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.menu_attendance = QWidget(self.widget_2)
        self.menu_attendance.setObjectName(u"menu_attendance")
        self.menu_attendance.setMinimumSize(QSize(0, 100))
        self.menu_attendance.setMaximumSize(QSize(16777215, 100))
        self.menu_attendance.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.horizontalLayout_5 = QHBoxLayout(self.menu_attendance)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_28 = QLabel(self.menu_attendance)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setEnabled(True)
        self.label_28.setMinimumSize(QSize(0, 70))
        self.label_28.setMaximumSize(QSize(16777215, 100))
        self.label_28.setBaseSize(QSize(0, 70))
        self.label_28.setFont(font5)
        self.label_28.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"font-size: 40px;\n"
"")
        self.label_28.setFrameShape(QFrame.StyledPanel)
        self.label_28.setFrameShadow(QFrame.Sunken)
        self.label_28.setMidLineWidth(5)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_28)


        self.verticalLayout_15.addWidget(self.menu_attendance)

        self.info_frame = QFrame(self.widget_2)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setMaximumSize(QSize(16777215, 200))
        font13 = QFont()
        font13.setFamilies([u"Roboto"])
        font13.setPointSize(16)
        font13.setBold(False)
        self.info_frame.setFont(font13)
        self.info_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.gridLayout_9 = QGridLayout(self.info_frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(20)
        self.gridLayout_9.setVerticalSpacing(10)
        self.gridLayout_9.setContentsMargins(30, 0, 30, 0)
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(10)
        self.gridLayout_11.setVerticalSpacing(20)
        self.label = QLabel(self.info_frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font14 = QFont()
        font14.setFamilies([u"Roboto"])
        font14.setPointSize(12)
        self.label.setFont(font14)

        self.gridLayout_11.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.info_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 50))
        self.label_3.setFont(font14)

        self.gridLayout_11.addWidget(self.label_3, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.info_frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy3)
        self.lineEdit_2.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_11.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit = QLineEdit(self.info_frame)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy3.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy3)
        self.lineEdit.setMaximumSize(QSize(16777215, 50))
        self.lineEdit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_11.addWidget(self.lineEdit, 0, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_11, 0, 0, 1, 1)

        self.search_btn = QPushButton(self.info_frame)
        self.search_btn.setObjectName(u"search_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy4)
        self.search_btn.setMaximumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u"../QtPy_examples/PyQt5-Video-Book/#017_Students information system/icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_btn.setIcon(icon1)
        self.search_btn.setIconSize(QSize(20, 20))

        self.gridLayout_9.addWidget(self.search_btn, 0, 2, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(10)
        self.gridLayout_10.setVerticalSpacing(20)
        self.label_6 = QLabel(self.info_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 50))
        self.label_6.setFont(font14)

        self.gridLayout_10.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_5 = QLabel(self.info_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 50))
        font15 = QFont()
        font15.setFamilies([u"Roboto"])
        font15.setPointSize(12)
        font15.setBold(False)
        self.label_5.setFont(font15)

        self.gridLayout_10.addWidget(self.label_5, 0, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.info_frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy3.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy3)
        self.lineEdit_3.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_10.addWidget(self.lineEdit_3, 0, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.info_frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy3.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy3)
        self.lineEdit_4.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_10.addWidget(self.lineEdit_4, 1, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_10, 0, 1, 1, 1)


        self.verticalLayout_15.addWidget(self.info_frame)

        self.result_frame = QFrame(self.widget_2)
        self.result_frame.setObjectName(u"result_frame")
        self.result_frame.setMaximumSize(QSize(16777215, 625))
        self.gridLayout_8 = QGridLayout(self.result_frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.table_attendance = QTableWidget(self.result_frame)
        if (self.table_attendance.columnCount() < 5):
            self.table_attendance.setColumnCount(5)
        font16 = QFont()
        font16.setFamilies([u"DejaVu Sans"])
        font16.setPointSize(12)
        font16.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font16);
        self.table_attendance.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem1.setFont(font16);
        self.table_attendance.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem2.setFont(font16);
        self.table_attendance.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem3.setFont(font16);
        self.table_attendance.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem4.setFont(font16);
        self.table_attendance.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.table_attendance.setObjectName(u"table_attendance")
        font17 = QFont()
        font17.setFamilies([u"Roboto"])
        font17.setPointSize(11)
        self.table_attendance.setFont(font17)
        self.table_attendance.setFocusPolicy(Qt.NoFocus)
        self.table_attendance.setStyleSheet(u"")
        self.table_attendance.setFrameShape(QFrame.NoFrame)
        self.table_attendance.setFrameShadow(QFrame.Raised)
        self.table_attendance.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_attendance.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_attendance.setShowGrid(False)
        self.table_attendance.setGridStyle(Qt.NoPen)
        self.table_attendance.setSortingEnabled(True)
        self.table_attendance.setWordWrap(True)
        self.table_attendance.setCornerButtonEnabled(False)
        self.table_attendance.setRowCount(0)
        self.table_attendance.horizontalHeader().setCascadingSectionResizes(False)
        self.table_attendance.horizontalHeader().setMinimumSectionSize(50)
        self.table_attendance.horizontalHeader().setDefaultSectionSize(120)
        self.table_attendance.horizontalHeader().setHighlightSections(True)
        self.table_attendance.horizontalHeader().setStretchLastSection(True)
        self.table_attendance.verticalHeader().setVisible(False)
        self.table_attendance.verticalHeader().setCascadingSectionResizes(False)
        self.table_attendance.verticalHeader().setMinimumSectionSize(30)
        self.table_attendance.verticalHeader().setDefaultSectionSize(30)
        self.table_attendance.verticalHeader().setHighlightSections(False)
        self.table_attendance.verticalHeader().setProperty(u"showSortIndicator", True)
        self.table_attendance.verticalHeader().setStretchLastSection(False)

        self.gridLayout_8.addWidget(self.table_attendance, 0, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.result_frame)


        self.horizontalLayout_6.addWidget(self.widget_2)

        self.Page.addWidget(self.Page_attendance)
        self.Page_Camera = QWidget()
        self.Page_Camera.setObjectName(u"Page_Camera")
        self.Page_Camera.setStyleSheet(u"*{\n"
"background-color: rgb(240, 246, 255);\n"
"}\n"
"QPushButton{\n"
"border-radius:none;\n"
"color: rgb(186, 189, 182);\n"
"}\n"
"QPushButton:hover{\n"
";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#menu_camera {\n"
"	border: 1px solid gray;\n"
"} ")
        self.gridLayout_7 = QGridLayout(self.Page_Camera)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.menu_camera = QFrame(self.Page_Camera)
        self.menu_camera.setObjectName(u"menu_camera")
        self.menu_camera.setMinimumSize(QSize(0, 100))
        self.menu_camera.setMaximumSize(QSize(16777215, 100))
        self.menu_camera.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.menu_camera.setFrameShape(QFrame.NoFrame)
        self.menu_camera.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.menu_camera)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_27 = QLabel(self.menu_camera)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 70))
        self.label_27.setMaximumSize(QSize(16777215, 100))
        self.label_27.setFont(font12)
        self.label_27.setStyleSheet(u"font-size: 40px;\n"
"")
        self.label_27.setFrameShape(QFrame.StyledPanel)
        self.label_27.setFrameShadow(QFrame.Sunken)
        self.label_27.setMidLineWidth(5)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_27)


        self.gridLayout_7.addWidget(self.menu_camera, 0, 0, 1, 1)

        self.camera = QVBoxLayout()
        self.camera.setObjectName(u"camera")
        self.camera_label = QLabel(self.Page_Camera)
        self.camera_label.setObjectName(u"camera_label")
        self.camera_label.setAlignment(Qt.AlignCenter)

        self.camera.addWidget(self.camera_label)


        self.gridLayout_7.addLayout(self.camera, 1, 0, 1, 1)

        self.Page.addWidget(self.Page_Camera)

        self.verticalLayout_16.addWidget(self.Page)


        self.horizontalLayout.addWidget(self.widget)

        self.horizontalLayout.setStretch(0, 350)
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.Main_btn_tracking, self.Signin_btn_signin)
        QWidget.setTabOrder(self.Signin_btn_signin, self.Signin_btn_signup)

        self.retranslateUi(MainWindow)

        self.Dashboard.setCurrentIndex(0)
        self.Main_btn_attendance.setDefault(True)
        self.Main_btn_camera.setDefault(True)
        self.Main_btn_tracking.setDefault(True)
        self.Account__btnlogout.setDefault(True)
        self.Page.setCurrentIndex(5)
        self.Signin_btn_login.setDefault(True)
        self.Signup_btn_signup.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Robot Management", None))
        self.Logo_fab.setText("")
        self.Logo_BK.setText("")
        self.Signin_btn_signin.setText(QCoreApplication.translate("MainWindow", u"SIGN IN", None))
        self.Signin_btn_signup.setText(QCoreApplication.translate("MainWindow", u"SIGN UP", None))
        self.Signin_text.setText(QCoreApplication.translate("MainWindow", u"FAB-LAB \n"
" All rights reserved", None))
        self.Logo_fab_2.setText("")
        self.Logo_BK_2.setText("")
        self.Label_admin.setText(QCoreApplication.translate("MainWindow", u"ADMIN", None))
        self.Main_btn_attendance.setText(QCoreApplication.translate("MainWindow", u"ATTENDANCE", None))
        self.Main_btn_camera.setText(QCoreApplication.translate("MainWindow", u"CAMERA", None))
        self.Main_btn_tracking.setText(QCoreApplication.translate("MainWindow", u"TRACKING", None))
        self.Account_username.setText(QCoreApplication.translate("MainWindow", u"USERNAME", None))
        self.Account__btnlogout.setText(QCoreApplication.translate("MainWindow", u"LOGOUT", None))
        self.label_battery.setText(QCoreApplication.translate("MainWindow", u"battery", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SIGN IN", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Please enter your username and password", None))
        self.Signin_btn_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.Signin_username.setText("")
        self.Signin_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.Signin_password.setText("")
        self.Signin_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.Title_signup.setText(QCoreApplication.translate("MainWindow", u"SIGN UP", None))
        self.Signup_name.setText("")
        self.Signup_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Full name", None))
        self.Signup_phone.setText("")
        self.Signup_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone number", None))
        self.Signup_username.setText("")
        self.Signup_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.Signup_password.setText("")
        self.Signup_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.Signup_code.setText("")
        self.Signup_code.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Verify code", None))
        self.Signup_btn_signup.setText(QCoreApplication.translate("MainWindow", u"Create Account", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"TRACKING", None))
        self.traking_label.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"ATTENDANCE", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Employee ID", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.search_btn.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Email Address", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        ___qtablewidgetitem = self.table_attendance.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Employee ID", None));
        ___qtablewidgetitem1 = self.table_attendance.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.table_attendance.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Department", None));
        ___qtablewidgetitem3 = self.table_attendance.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem4 = self.table_attendance.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Email Address", None));
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"CAMERA", None))
        self.camera_label.setText("")
    # retranslateUi

