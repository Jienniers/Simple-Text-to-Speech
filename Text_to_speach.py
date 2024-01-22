from PyQt5 import QtCore, QtGui, QtWidgets
import pyttsx3

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 410)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/conversation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 801, 411))
        self.stackedWidget.setStyleSheet("background-color: rgb(25, 25, 25)")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Text_to_speach_page = QtWidgets.QWidget()
        self.Text_to_speach_page.setObjectName("Text_to_speach_page")
        self.Title = QtWidgets.QLabel(self.Text_to_speach_page)
        self.Title.setGeometry(QtCore.QRect(190, 20, 391, 61))
        self.Title.setStyleSheet("font: 48pt \"Impact\";\n"
"color: rgb(255, 255, 255);")
        self.Title.setObjectName("Title")
        self.frame = QtWidgets.QFrame(self.Text_to_speach_page)
        self.frame.setGeometry(QtCore.QRect(779, 389, 21, 21))
        self.frame.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Write_anything_label = QtWidgets.QLabel(self.Text_to_speach_page)
        self.Write_anything_label.setGeometry(QtCore.QRect(40, 140, 231, 51))
        self.Write_anything_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 28pt \"Impact\";")
        self.Write_anything_label.setObjectName("Write_anything_label")
        self.line = QtWidgets.QFrame(self.Text_to_speach_page)
        self.line.setGeometry(QtCore.QRect(10, 100, 781, 16))
        self.line.setStyleSheet("color:white;\n"
"height:4px;\n"
"border-radius:5px;\n"
"background-color: rgb(122, 122, 122);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit_Speach = QtWidgets.QLineEdit(self.Text_to_speach_page)
        self.lineEdit_Speach.setGeometry(QtCore.QRect(290, 140, 281, 51))
        self.lineEdit_Speach.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 28pt \"Impact\";\n"
"border-radius:5px;\n"
"border:solid;\n"
"border-color: rgb(100, 100, 100);\n"
"background-color: rgb(103, 103, 103);")
        self.lineEdit_Speach.setObjectName("lineEdit_Speach")
        self.Speach_btn = QtWidgets.QPushButton(self.Text_to_speach_page)
        self.Speach_btn.setGeometry(QtCore.QRect(270, 250, 281, 71))
        self.Speach_btn.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"font: 28pt \"Impact\";\n"
"border-radius:5px;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 92, 157);\n"
"\n"
"}\n"
"QPushButton:Pressed{\n"
"background-color: rgb(0, 84, 140);\n"
"}")
        self.Speach_btn.setObjectName("Speach_btn")
        self.Saying_label = QtWidgets.QLabel(self.Text_to_speach_page)
        self.Saying_label.setGeometry(QtCore.QRect(280, 340, 231, 51))
        self.Saying_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 28pt \"Impact\";")
        self.Saying_label.setText("")
        self.Saying_label.setObjectName("Saying_label")
        self.stackedWidget.addWidget(self.Text_to_speach_page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
###########################Connections#####################################


        self.Speach_btn.clicked.connect(self.speach)
        



##############################End#########################################

######################Functions########################################

    def speach(self):
            friend = pyttsx3.init()
            friend.say(self.lineEdit_Speach.text())
            friend.runAndWait()


############################End############################

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Text To Speech"))
        self.Title.setText(_translate("Form", "Text To Speech"))
        self.Write_anything_label.setText(_translate("Form", "Write Anything:"))
        self.Speach_btn.setText(_translate("Form", "Speach"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    Form.setWindowFlags(Form.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
    Form.setFixedSize(800, 410)
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
