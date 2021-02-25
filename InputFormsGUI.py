from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QCompleter, QDesktopWidget, \
    QLabel, QFrame, QLineEdit, QPushButton
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QFont
from BasicElementGUI import BasicElement


class FormInputBox(BasicElement):
    def __init__(self, xpos, ypos, width, height, text, where):
        BasicElement.__init__(self, xpos, ypos, width, height, where)
        self.formText = text
        self.formFrame = QFrame(where)
        self.formCheckImage = QLabel(self.formFrame)
        self.formLineEdit = QLineEdit(self.formFrame)

        self.create_element()

    def create_element(self):

        self.formFrame.resize(self.width, self.height)
        self.formFrame.move(self.x, self.y)
        self.formFrame.setStyleSheet("background-color:#fff;border-radius:30px;color:black;font-size:20px;")

        self.formCheckImage.resize(48, 48)
        self.formCheckImage.setPixmap(QtGui.QPixmap("graphics/001-plus.png").scaled(48, 48, QtCore.Qt.KeepAspectRatio,
                                                                                    QtCore.Qt.SmoothTransformation))
        self.formCheckImage.move(self.width - 60, self.height / 2 - 24)

        self.formLineEdit.setPlaceholderText(self.formText)
        self.formLineEdit.move(35, self.height / 2 - 15)
        self.formLineEdit.setFont(self.get_roboto_medium_font())
        self.formLineEdit.resize(self.width - 100, 30)
        self.formLineEdit.textChanged.connect(lambda: self.alpha_correct(self.formLineEdit,self.formCheckImage))

        self.formFrame.setGraphicsEffect(self.shadow_make(20, 2, 2))

    def input_cls(self, input):
        input.clear()

    def numeric_correct(self):
        pass

    def alpha_correct(self, inputWidget, image):
        if inputWidget.text() == "":
            self.incorrect_icon_set(image)
            return

        if inputWidget.text()[0].isdigit() or len(inputWidget.text()) < 3:
            self.incorrect_icon_set(image)
        elif inputWidget.text()[0].isalpha():
            for char in inputWidget.text():
                if char.isspace() or char.isalnum():
                    self.correct_icon_set(image)
                else:
                    self.incorrect_icon_set(image)
        else:
            self.incorrect_icon_set(image)

    def correct_icon_set(self, input):
        self.formCheckImage.setPixmap(
            QtGui.QPixmap("graphics/003-checked.png").scaled(48, 48, QtCore.Qt.KeepAspectRatio,
                                                             QtCore.Qt.SmoothTransformation))

    def incorrect_icon_set(self, input):
        self.formCheckImage.setPixmap(QtGui.QPixmap("graphics/002-minus.png").scaled(48, 48, QtCore.Qt.KeepAspectRatio,
                                                                                     QtCore.Qt.SmoothTransformation))

    def basic_icon_set(self, ImageSrc):
        self.formCheckImage.setPixmap(QtGui.QPixmap("{}".format(ImageSrc)).scaled(48, 48, QtCore.Qt.KeepAspectRatio,
                                                                                  QtCore.Qt.SmoothTransformation))


class FromLargeInputBox(FormInputBox):
    def __init__(self, xpos, ypos, width, height, text, where):
        FormInputBox.__init__(self, xpos, ypos, width, height, text, where)
        self.formLineEdit = QTextEdit(self.formFrame)

        FormInputBox.create_element(self)

        self.create_element()

    def create_element(self):
        self.formCheckImage.move(24, 16)
        self.formLineEdit.move(80, 25)
        self.formLineEdit.textChanged.connect(self.dupa)
        self.formLineEdit.resize(self.width - 100, self.height - 50)
        self.basic_icon_set("graphics/005-open-book-1.png")


class FormComboBox(FormInputBox):
    def __init__(self, xpos, ypos, width, height, text, where, options):
        super(FormComboBox,self).__init__(xpos, ypos, width, height, text, where)
        self.optionList = options


        FormInputBox.create_element(self)

        self.create_element2()

    def create_element2(self):
        self.formFrame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.formLineEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.formLineEdit.setReadOnly(True)


        optionsFrame = QFrame(self.startFrame)
        optionsFrame.resize(self.width, len(self.optionList) * 80)
        optionsFrame.move(self.x, self.y + self.height + 10)
        optionsFrame.show()
        optionsFrame.activateWindow()
        optionsFrame.raise_()
        optionsFrame.setStyleSheet(
            "background-color:#fff;border-bottom-right-radius:20px;border-bottom-left-radius:30px;")
        optionsFrame.setGraphicsEffect(self.shadow_make(20, 3, 2))

        buttonlist=[]
        for type in self.optionList:
            tempButton=QPushButton(optionsFrame)
            tempButton.setText(type)
            tempButton.resize(self.width,80)
            tempButton.setStyleSheet("QPushButton{color:black;font-size:24px;border-bottom:1px dotted black;border-radius:0px;} QPushButton:hover{background-color:#42afc2;}")
            tempButton.setFont(QFont(self.get_roboto_medium_font()))
            tempButton.move(0,self.optionList.index(type)*80)
            buttonlist.append(tempButton)

        buttonlist[-1].setStyleSheet("QPushButton{color:black;font-size:24px;border-top:1px dotted black;border-bottom-right-radius:20px;border-bottom-left-radius:30px;} QPushButton:hover{background-color:#42afc2;}")


        self.formFrame.setStyleSheet(
            "{}border-bottom-left-radius:0px;border-bottom-right-radius:0px;".format(self.formFrame.styleSheet()))
        self.basic_icon_set("graphics/arrow.png")
