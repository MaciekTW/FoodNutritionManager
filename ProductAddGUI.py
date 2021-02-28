from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QCompleter, QDesktopWidget
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QFont
from InputFormsGUI import FormInputBox
from DatabaseImplementation import DBoperation
from GlobalVariables import GlobalVariables


class ProductAddGUI(GlobalVariables):
    def __init__(self, workspace):
        super().__init__()
        self.robotoFontFamily = QtGui.QFontDatabase.applicationFontFamilies(
            QtGui.QFontDatabase.addApplicationFont("Fonts/Roboto-Regular.ttf"))

        self.robotoFontFamily.append(QtGui.QFontDatabase.applicationFontFamilies(
            QtGui.QFontDatabase.addApplicationFont("Fonts/Roboto-MediumItalic.ttf")))

        self.robotoFontFamily.append(QtGui.QFontDatabase.applicationFontFamilies(
            QtGui.QFontDatabase.addApplicationFont("Fonts/Roboto-BoldCondensed.ttf")))

        print(self.robotoFontFamily)


        self.workScreen = workspace
        self.mainScreen = QtWidgets.QFrame(self.workScreen)
        self.mainScreen.hide()
        self.mainScreen.resize(1820, 1000)

        self.leftWidget = QtWidgets.QFrame(self.mainScreen)
        self.leftWidget.resize(910, 1000)
        self.leftWidget.setStyleSheet("background-color:#39b54a;")

        self.leftWidgetMiddleFrame = QtWidgets.QFrame(self.leftWidget)
        self.leftWidgetMiddleFrame.resize(790, 800)
        self.leftWidgetMiddleFrame.move(60, 100)
        self.frameLogo = QtWidgets.QLabel(self.leftWidgetMiddleFrame)
        self.frameLogo.setPixmap(QtGui.QPixmap('graphics/002-shop.png').scaled(386, 386, QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation))
        self.frameLogo.move(202, 207)
        self.frameTitle = QtWidgets.QLabel(self.leftWidgetMiddleFrame)
        self.frameTitle.setText("This is a place you can update")
        self.frameTitle.setFont(QtGui.QFont(self.robotoFontFamily[0]))
        self.frameTitle.setMinimumWidth(790)
        self.frameTitle.setAlignment(QtCore.Qt.AlignHCenter)
        self.frameTitle.setStyleSheet("font-size:24px;color:#fff;padding:10px;")
        self.frameTitle.move(0, 65)

        self.frameTitle2 = QtWidgets.QLabel(self.leftWidgetMiddleFrame)
        self.frameTitle2.setText("your kitchen database!")
        self.frameTitle2.setFont(QtGui.QFont(self.robotoFontFamily[0]))
        self.frameTitle2.setMinimumWidth(790)
        self.frameTitle2.setAlignment(QtCore.Qt.AlignHCenter)
        self.frameTitle2.setStyleSheet("font-size:24px;color:#fff;padding:10px;")
        self.frameTitle2.move(0, 105)

        self.firstHr = QtWidgets.QFrame(self.leftWidgetMiddleFrame)
        self.firstHr.move(185, 630)
        self.firstHr.resize(420, 4)
        self.firstHr.setStyleSheet("background-color:white;border:5px solid white;border-radius:2%")

        self.firstHr = QtWidgets.QFrame(self.leftWidgetMiddleFrame)
        self.firstHr.move(185, 630)
        self.firstHr.resize(420, 4)
        self.firstHr.setStyleSheet("background-color:white;border:5px solid white;border-radius:2%")
        self.firstHr.setGraphicsEffect(self.shadow_make(40, 3, 3))


        self.secondHr = QtWidgets.QFrame(self.leftWidgetMiddleFrame)
        self.secondHr.move(225, 685)
        self.secondHr.resize(340, 2)
        self.secondHr.setStyleSheet("background-color:white;border:5px solid white;border-radius:2%")
        self.secondHr.setGraphicsEffect(self.shadow_make(40, 3, 3))


        self.thirdHr = QtWidgets.QFrame(self.leftWidgetMiddleFrame)
        self.thirdHr.move(265, 725)
        self.thirdHr.resize(260, 1)
        self.thirdHr.setStyleSheet("background-color:white;border:5px solid white;border-radius:2%")
        self.thirdHr.setGraphicsEffect(self.shadow_make(40, 3, 3))


        self.rightWidget = QtWidgets.QFrame(self.mainScreen)
        self.rightWidget.resize(910, 1000)
        self.rightWidget.move(910,0)
        self.rightWidget.setStyleSheet("color:#fff;")


        self.rightWidgetMiddleFrame=QtWidgets.QFrame(self.rightWidget)
        self.rightWidgetMiddleFrame.resize(660,880)
        self.rightWidgetMiddleFrame.move(125,60)

        self.titleLab=QtWidgets.QLabel(self.rightWidgetMiddleFrame)
        self.titleLab.move(0,50)
        self.titleLab.setStyleSheet("font-size:24px;")
        self.titleLab.setFont(QtGui.QFont(self.robotoFontFamily[1][0]))
        self.titleLab.setText("Use the form below to add new product")

        self.formFrame=QtWidgets.QFrame(self.rightWidgetMiddleFrame)
        self.formFrame.resize(660,730)
        self.formFrame.move(0,120)
        #self.formFrame.setStyleSheet("background-color:green")


        self.productNameInput=FormInputBox(15,0,630,80,"Product name",self.formFrame,False)
        self.kcalInput=FormInputBox(15,120,300,80,"Kcal",self.formFrame,True)
        self.carboInput = FormInputBox(345, 120, 300, 80, "Carbo", self.formFrame,True)
        self.sugarInput=FormInputBox(15,240,300,80,"Sugar",self.formFrame,True)
        self.proteinInput = FormInputBox(345, 240, 300, 80, "Protein", self.formFrame,True)
        self.fatInput=FormInputBox(15,360,300,80,"Fat",self.formFrame,True)
        self.weightInput = FormInputBox(345, 360, 300, 80, "Product weight", self.formFrame,True)
        self.descInput=FormInputBox(15,480,440,80,"Description",self.formFrame,False)
        self.priceInput = FormInputBox(485, 480, 160, 80, "Price", self.formFrame,True)


        self.submitButton=QtWidgets.QPushButton(self.formFrame)
        self.submitButton.resize(260,80)
        self.submitButton.move(60,620)
        self.submitButton.setStyleSheet("QPushButton{"
                                        "background-color:#39b54a;"
                                        "color:#fff;"
                                        "font-size:30px;} "
                                        "QPushButton:hover{"
                                        "background-color:#2ce246;}")
        self.submitButton.setFont(QtGui.QFont(self.robotoFontFamily[2][0]))
        self.submitButton.setText("Submit")
        self.submitButton.setGraphicsEffect(self.shadow_make())

        self.clsButton=QtWidgets.QPushButton(self.formFrame)
        self.clsButton.resize(260,80)
        self.clsButton.move(360,620)
        self.clsButton.setStyleSheet("QPushButton{"
                                        "background-color:#39b54a;"
                                        "color:#fff;"
                                        "font-size:30px;} "
                                        "QPushButton:hover{"
                                        "background-color:#2ce246;}")
        self.clsButton.setFont(QtGui.QFont(self.robotoFontFamily[2][0]))
        self.clsButton.setText("Clear")
        self.clsButton.setGraphicsEffect(self.shadow_make())

        self.clsButton.clicked.connect(self.clear)
        self.submitButton.clicked.connect(self.product_add)



    def show(self):
        self.mainScreen.setVisible(True)

    def hide(self):
        self.mainScreen.setVisible(False)

    def shadow_make(self, blur=20, xOff=0, yOff=0):
        shadowObj = QtWidgets.QGraphicsDropShadowEffect()
        shadowObj.setColor(QtGui.QColor(0, 0, 0))
        shadowObj.setBlurRadius(blur)
        shadowObj.setXOffset(xOff)
        shadowObj.setYOffset(yOff)
        return shadowObj

    def product_add(self):
        print(self.productNameInput.get_text())
        self.DB.DB_product_insert(self.productNameInput.get_text(),
                                  float(self.kcalInput.get_text()),
                                  float(self.carboInput.get_text()),
                                  float(self.sugarInput.get_text()),
                                  float(self.proteinInput.get_text()),
                                  float(self.fatInput.get_text()),
                                  float(self.priceInput.get_text()),
                                  float(self.weightInput.get_text()))



        self.clear()

    def clear(self):
        self.productNameInput.clear()
        self.carboInput.clear()
        self.kcalInput.clear()
        self.sugarInput.clear()
        self.proteinInput.clear()
        self.fatInput.clear()
        self.priceInput.clear()
        self.weightInput.clear()

