from PyQt4 import Qt, QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(531, 365)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/app_logo/app-logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.artist_label = QtGui.QLabel(self.centralwidget)
        self.artist_label.setGeometry(QtCore.QRect(200, 10, 138, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.artist_label.setFont(font)
        self.artist_label.setAlignment(QtCore.Qt.AlignCenter)
        self.artist_label.setObjectName(_fromUtf8("artist_label"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 10, 191, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(350, 10, 181, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.dir_label = QtGui.QLabel(self.centralwidget)
        self.dir_label.setGeometry(QtCore.QRect(20, 90, 131, 21))
        self.dir_label.setObjectName(_fromUtf8("dir_label"))
        self.dir_edit = QtGui.QLineEdit(self.centralwidget)
        self.dir_edit.setGeometry(QtCore.QRect(150, 90, 311, 20))
        self.dir_edit.setObjectName(_fromUtf8("dir_edit"))
        self.dir_button = QtGui.QPushButton(self.centralwidget)
        self.dir_button.setGeometry(QtCore.QRect(470, 90, 41, 21))
        self.dir_button.setObjectName(_fromUtf8("dir_button"))
        self.url_edit = QtGui.QLineEdit(self.centralwidget)
        self.url_edit.setGeometry(QtCore.QRect(150, 140, 311, 20))
        self.url_edit.setObjectName(_fromUtf8("url_edit"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 180, 511, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.url_label = QtGui.QLabel(self.centralwidget)
        self.url_label.setGeometry(QtCore.QRect(20, 140, 111, 21))
        self.url_label.setObjectName(_fromUtf8("url_label"))
        self.progress_bar = QtGui.QProgressBar(self.centralwidget)
        self.progress_bar.setGeometry(QtCore.QRect(30, 210, 491, 21))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setInvertedAppearance(False)
        self.progress_bar.setObjectName(_fromUtf8("progress_bar"))
        self.download_button = QtGui.QPushButton(self.centralwidget)
        self.download_button.setGeometry(QtCore.QRect(160, 260, 221, 61))
        self.download_button.setObjectName(_fromUtf8("download_button"))
        self.clear_button = QtGui.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(470, 140, 41, 21))
        self.clear_button.setObjectName(_fromUtf8("clear_button"))
        self.progress_label = QtGui.QLabel(self.centralwidget)
        self.progress_label.setGeometry(QtCore.QRect(100, 230, 341, 31))
        self.progress_label.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menu_bar = QtGui.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 531, 21))
        self.menu_bar.setObjectName(_fromUtf8("menu_bar"))
        self.menuFile = QtGui.QMenu(self.menu_bar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menu_bar)
        self.status_bar = QtGui.QStatusBar(MainWindow)
        self.status_bar.setObjectName(_fromUtf8("status_bar"))
        MainWindow.setStatusBar(self.status_bar)
        self.action_clear_all = QtGui.QAction(MainWindow)
        self.action_clear_all.setObjectName(_fromUtf8("action_clear_all"))
        self.action_quit = QtGui.QAction(MainWindow)
        self.action_quit.setObjectName(_fromUtf8("action_quit"))
        self.menuFile.addAction(self.action_clear_all)
        self.menuFile.addAction(self.action_quit)
        self.menu_bar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Band Loader", None))
        self.artist_label.setText(_translate("MainWindow", "SUPPORT THE ARTISTS", None))
        self.dir_label.setText(_translate("MainWindow", "What directory to save to:", None))
        self.dir_button.setText(_translate("MainWindow", "...", None))
        self.url_label.setText(_translate("MainWindow", "Bandcamp URL:", None))
        self.download_button.setText(_translate("MainWindow", "Download", None))
        self.clear_button.setText(_translate("MainWindow", "Clear", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.action_clear_all.setText(_translate("MainWindow", "Clear All ", None))
        self.action_clear_all.setShortcut(_translate("MainWindow", "Ctrl+C", None))
        self.action_quit.setText(_translate("MainWindow", "Quit", None))
        self.action_quit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))

import resources_rc