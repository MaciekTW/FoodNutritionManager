from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QCompleter, QDesktopWidget
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QFont
from InputFormsGUI import FormInputBox,FromLargeInputBox,FormComboBox


class MealAddGUI:
    def __init__(self, workspace):
        self.robotoFontFamily = QtGui.QFontDatabase.applicationFontFamilies(
            QtGui.QFontDatabase.addApplicationFont("Fonts/Roboto-Regular.ttf"))

        self.robotoFontFamily.append(QtGui.QFontDatabase.applicationFontFamilies(
            QtGui.QFontDatabase.addApplicationFont("Fonts/Roboto-MediumItalic.ttf")))

        self.robotoFontFamily.append(QtGui.QFontDatabase.applicationFontFamilies(
            QtGui.QFontDatabase.addApplicationFont("Fonts/Roboto-BoldCondensed.ttf")))

        self.workScreen = workspace
        self.mainScreen = QtWidgets.QFrame(self.workScreen)
        self.mainScreen.hide()
        self.mainScreen.resize(1820, 1000)

        self.leftWidget = QtWidgets.QFrame(self.mainScreen)
        self.leftWidget.resize(910, 1000)
        self.leftWidget.setStyleSheet("background-color:#42afc2;")

        self.leftWidgetMiddleFrame = QtWidgets.QFrame(self.leftWidget)
        self.leftWidgetMiddleFrame.resize(790, 800)
        self.leftWidgetMiddleFrame.move(60, 100)
        self.frameLogo = QtWidgets.QLabel(self.leftWidgetMiddleFrame)
        self.frameLogo.setPixmap(QtGui.QPixmap('graphics/006-cooking.png').scaled(386, 386, QtCore.Qt.KeepAspectRatio))
        self.frameLogo.move(202, 207)
        self.frameTitle = QtWidgets.QLabel(self.leftWidgetMiddleFrame)
        self.frameTitle.setText("Cooking is your passion, isn't it?")
        self.frameTitle.setFont(QtGui.QFont(self.robotoFontFamily[0]))
        self.frameTitle.setMinimumWidth(790)
        self.frameTitle.setAlignment(QtCore.Qt.AlignHCenter)
        self.frameTitle.setStyleSheet("font-size:24px;color:#fff;padding:10px;")
        self.frameTitle.move(0, 65)

        self.frameTitle2 = QtWidgets.QLabel(self.leftWidgetMiddleFrame)
        self.frameTitle2.setText("enter a new recipe!")
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


        options=["Brekfakt","Dinner","Supper","Snack"," ij"]

        self.productNameInput=FormInputBox(15,0,630,80,"Meal name",self.formFrame)

        self.sugarInput=FormInputBox(15,240,430,80,"First Ingredient",self.formFrame)
        self.proteinInput = FormInputBox(475, 240, 170, 80, "Weight", self.formFrame)
        self.descInput=FromLargeInputBox(15,360,630,200,"Description",self.formFrame)
        self.kcalInput = FormComboBox(15, 120, 630, 80, "Meal type", self.formFrame,options)


        self.submitButton=QtWidgets.QPushButton(self.formFrame)
        self.submitButton.resize(260,80)
        self.submitButton.move(60,620)
        self.submitButton.setStyleSheet("QPushButton{"
                                        "background-color:#42afc2;"
                                        "color:#fff;"
                                        "font-size:30px;} "
                                        "QPushButton:hover{"
                                        "background-color:#f61fff;}")
        self.submitButton.setFont(QtGui.QFont(self.robotoFontFamily[2][0]))
        self.submitButton.setText("Submit")
        self.submitButton.setGraphicsEffect(self.shadow_make())

        self.clsButton=QtWidgets.QPushButton(self.formFrame)
        self.clsButton.resize(260,80)
        self.clsButton.move(360,620)
        self.clsButton.setStyleSheet("QPushButton{"
                                        "background-color:#42afc2;"
                                        "color:#fff;"
                                        "font-size:30px;} "
                                        "QPushButton:hover{"
                                        "background-color:#f61fff;}")
        self.clsButton.setFont(QtGui.QFont(self.robotoFontFamily[2][0]))
        self.clsButton.setText("Clear")
        self.clsButton.setGraphicsEffect(self.shadow_make())



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
