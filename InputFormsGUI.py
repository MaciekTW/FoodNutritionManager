from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QCompleter, QDesktopWidget, \
    QLabel, QFrame, QLineEdit, QPushButton
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QFont
from BasicElementGUI import BasicElement


class FormInputBox(BasicElement):
    def __init__(self, xpos, ypos, width, height, text, where,numeric=True):
        BasicElement.__init__(self, xpos, ypos, width, height, where)
        self.formText = text
        self.formFrame = QFrame(where)
        self.formCheckImage = QLabel(self.formFrame)
        self.formLineEdit = QLineEdit(self.formFrame)
        self.isNumeric=numeric

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
        self.formLineEdit.textChanged.connect(lambda: self.alpha_correct(self.formLineEdit,self.formCheckImage,self.isNumeric))

        self.formFrame.setGraphicsEffect(self.shadow_make(20, 2, 2))

    def input_cls(self, input):
        input.clear()

    def numeric_correct(self):
        pass

    def alpha_correct(self, inputWidget, image,numeric):
        if not numeric:
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
        else:
            if inputWidget.text() == "":
                self.incorrect_icon_set(image)
                return

            digit=False
            if inputWidget.text()[0].isdigit():
                for char in inputWidget.text():
                    if not char.isdigit():
                        if char ==',' or char =='.' and digit==False:
                            digit=True
                        else:
                            self.incorrect_icon_set(image)
                    elif char.isalpha():
                        self.incorrect_icon_set(image)
                    else:
                        self.correct_icon_set(image)
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

    def get_text(self):
        return self.formLineEdit.text()

    def set_enable(self,isEnable):
        self.formLineEdit.setEnabled(isEnable)

    def clear(self):
        self.formLineEdit.clear()

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


    def alpha_correct(self, inputWidget, image,numeric):
        pass

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


        self.optionsFrame = QFrame(self.startFrame)
        self.formFrame.mousePressEvent=self.hide_combo_box
        self.optionsFrame.resize(self.width, len(self.optionList) * 80)
        self.optionsFrame.move(self.x, self.y + self.height + 10)
        self.optionsFrame.show()
        self.optionsFrame.activateWindow()
        self.optionsFrame.raise_()
        self.optionsFrame.setStyleSheet(
            "background-color:#fff;border-bottom-right-radius:20px;border-bottom-left-radius:30px;")
        self.optionsFrame.setGraphicsEffect(self.shadow_make(20, 3, 2))

        buttonlist=[]
        for type in self.optionList:
            tempButton=QPushButton(self.optionsFrame)
            tempButton.setText(type)
            tempButton.resize(self.width,80)
            tempButton.setStyleSheet("QPushButton{color:black;font-size:24px;border-bottom:1px dotted black;border-radius:0px;} QPushButton:hover{background-color:#42afc2;}")
            tempButton.setFont(QFont(self.get_roboto_medium_font()))
            tempButton.move(0,self.optionList.index(type)*80)
            tempButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            tempButton.clicked.connect(self.choice_pick)
            buttonlist.append(tempButton)

        buttonlist[-1].setStyleSheet("QPushButton{color:black;font-size:24px;border-top:1px dotted black;border-bottom-right-radius:20px;border-bottom-left-radius:30px;} QPushButton:hover{background-color:#42afc2;}")

        self.optionsFrame.setVisible(False)
        self.basic_icon_set("graphics/arrow.png")

    def hide_combo_box(self, event):
        if self.optionsFrame.isVisible():
            self.optionsFrame.hide()
            self.formFrame.setStyleSheet("background-color:#fff;border-radius:30px;color:black;font-size:20px;")
            self.basic_icon_set("graphics/arrow.png")
        else:
            self.optionsFrame.show()
            self.formFrame.setStyleSheet(
            "{}border-bottom-left-radius:0px;border-bottom-right-radius:0px;".format(self.formFrame.styleSheet()))
            self.basic_icon_set("graphics/arrow-up.png")

    def choice_pick(self):
        text=QtCore.QObject()
        choice=text.sender().text()
        self.formLineEdit.setText(choice)
        self.hide_combo_box(self.formLineEdit)

    def alpha_correct(self, inputWidget, image, image2):
        pass


class FormViewEmpty(FormInputBox):
    def __init__(self, xpos, ypos, width, height, text, where):
        super().__init__(xpos, ypos, width, height, text, where)

        FormInputBox.create_element(self)

        self.create_element2()

    def create_element2(self):
        self.basic_icon_set("")
        self.formLineEdit.setMinimumWidth(self.width-30)
        self.formLineEdit.setText(self.formText)
        self.formLineEdit.setReadOnly(True)

    def alpha_correct(self, inputWidget, image,numeric):
        pass


class FormCompleterInput(FormInputBox):
    def __init__(self, xpos, ypos, width, height, text, where,predictionList):
        super().__init__(xpos, ypos, width, height, text, where)
        self.items=predictionList

        FormInputBox.create_element(self)

        self.create_element2()

    def create_element2(self):
        self.model = QStandardItemModel()
        completer = QCompleter(self.model, self.formLineEdit)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.formLineEdit.setCompleter(completer)

        for i in self.items:
            self.model.appendRow(QStandardItem(i))

    def alpha_correct(self, inputWidget, image,numeric):
        pass