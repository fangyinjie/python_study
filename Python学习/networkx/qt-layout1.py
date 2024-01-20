import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QLabel


class Winform():
    def __init__(self):
        self.window = QWidget()
        self.window.setWindowTitle("表单布局管理例子")
        self.window.resize(400, 100)
        self.fromlayout = QFormLayout()
        self.labl1       = QLabel("标签1")
        self.lineEdit1   = QLineEdit()
        self.fromlayout.addRow(self.labl1, self.lineEdit1)
        self.labl2       = QLabel("标签2")
        self.lineEdit2   = QLineEdit()
        self.fromlayout.addRow(self.labl2, self.lineEdit2)
        self.labl3       = QLabel("标签3")
        self.lineEdit3   = QLineEdit()
        self.fromlayout.addRow(self.labl3, self.lineEdit3)
        self.window.setLayout(self.fromlayout)
        self.window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Winform()
    sys.exit(app.exec_())
