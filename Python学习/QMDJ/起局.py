import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QDesktopWidget, QComboBox, QFormLayout

# from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
#                              QSlider, QFormLayout, QMessageBox, ,

if __name__ == '__main__':
    # 创建QApplication实例
    app = QApplication(sys.argv)  # 获取命令行参数
    w = QWidget()  # 创建一个窗口
    # ######### 操作区 ########
    w.resize(400, 200)                  # 设置窗口的尺寸 # 宽，高
    w.move(300, 300)                    # 移动窗口左上角坐标，其实就移动了窗口
    center_pointer = QDesktopWidget().availableGeometry().center()  # print(center_pointer)
    w.move(center_pointer.x(), center_pointer.y())                  # 调整窗口在屏幕中央显示
    # print (w. frameGeometry())
    # print (w. frameGeometry().getRect())
    # ### （1）添加按钮 - buttons ### #
    # btn = QPushButton("Default" , w)     # 在窗口里面添加控件，设置按钮的父亲是当前窗口，等于是添加到窗口中显示
    # btn.setGeometry(0, 0, 40, 40)   # 位置1,2 宽 高
    # ### （1）下拉菜单 - buttons ### #
    opt_alogrithm = QComboBox()
    opt_alogrithm.addItem("Nested-Fork Join (NFJ1)")
    opt_alogrithm.addItem("Nested-Fork Join (NFJ2)")
    opt_alogrithm.addItem("Nested-Fork Join (NFJ3)")
    opt_alogrithm.addItem("Nested-Fork Join (NFJ4)")
    # create layout
    formLayout = QFormLayout()
    formLayout.addRow("&Algorithm:", opt_alogrithm)
    """
    # ### （2）label 纯文本### #
    # todo(hello) # 这里以后可能会有的功能
    # TODO(Zeke) Change this to use relations.
    label = QLabel("账号: ", w)           # 创建一个Label (纯文本),在创建的时候指定了父对象
    label.setGeometry(40, 40, 40, 40)    # 显示位置与大小: X, y, w, h位置1,2 宽 高
    # ### （3）文本框### #
    edit = QLineEdit(w)
    edit.setPlaceholderText("请输入账号")
    edit.setGeometry(55, 20, 200, 20)   # 位置1,2 宽 高
    """
    # ########################
    w.setWindowTitle('first page')  # 设置窗口标题
    w.show()                        # 显示窗口
    sys.exit(app.exec_())   # (死循环)进入程序主循环，循环扫描响应在窗口上的事件，让整个程序不会退出,通过exit函数确保主循环安全结束
