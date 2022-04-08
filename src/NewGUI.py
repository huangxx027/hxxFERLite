import sys
from PyQt5 import QtWidgets
from newUI import Ui_MainWindow
from data_analysis import *
from recognition_camera import *

class MyPyQT_Form(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)

    def import_video(self):
        # 加载模型
        file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(caption="选取视频", directory=".",
                                                                     filter="All Files (*);;Text Files (*.txt)")
        # 显示原图
        if file_name is not None and file_name != "":
            vid_predict_expression(file_name)

    def cleardata(self):
        self.textEdit.setText("")
        self.textEdit_2.setText("")

    def emotion_recognition(self):
        self.textEdit.setText(biaoqingfenxi)

    def data_analysis(self):
        self.textEdit_2.setText(xueqingfenxi)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())