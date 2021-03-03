from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QCompleter, QDesktopWidget
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QFont
from InputFormsGUI import FormInputBox,FromLargeInputBox,FormViewEmpty,FormCompleterInput
import GlobalVariables
import re

class RecordAddGui:
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
        self.leftWidget.setStyleSheet("background-color:#6e41ff;")

        self.leftWidgetMiddleFrame = QtWidgets.QFrame(self.leftWidget)
        self.leftWidgetMiddleFrame.resize(790, 800)
        self.leftWidgetMiddleFrame.move(60, 100)
        self.frameLogo = QtWidgets.QLabel(self.leftWidgetMiddleFrame)
        self.frameLogo.setPixmap(QtGui.QPixmap('graphics/004-database-storage.png').scaled(386, 386, QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation))
        self.frameLogo.move(202, 207)
        self.frameTitle = QtWidgets.QLabel(self.leftWidgetMiddleFrame)
        self.frameTitle.setText("Finally, time to eat something delicious!")
        self.frameTitle.setFont(QtGui.QFont(self.robotoFontFamily[0]))
        self.frameTitle.setMinimumWidth(790)
        self.frameTitle.setAlignment(QtCore.Qt.AlignHCenter)
        self.frameTitle.setStyleSheet("font-size:24px;color:#fff;padding:10px;")
        self.frameTitle.move(0, 65)

        self.frameTitle2 = QtWidgets.QLabel(self.leftWidgetMiddleFrame)
        self.frameTitle2.setText("add a new meal!")
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
        self.titleLab.setText("Use the form below to add a new meal")

        self.formFrame=QtWidgets.QFrame(self.rightWidgetMiddleFrame)
        self.formFrame.resize(660,730)
        self.formFrame.move(0,120)
        #self.formFrame.setStyleSheet("background-color:green")


        self.mealNameInput=FormCompleterInput(15,0,500,80,"Meal name",self.formFrame,GlobalVariables.DB.get_meals_names())

        self.mealNameInput.get_text_element().textChanged.connect(self.kcal_view)
        self.mealKcalView = FormViewEmpty(535, 0, 110, 80, "Kcal", self.formFrame)


        self.descInput=FromLargeInputBox(15,120,630,440,"Ingredients List",self.formFrame)



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
        self.submitButton.clicked.connect(self.add_daily_meal)


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
        self.clsButton.clicked.connect(self.input_clear)



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

    def kcal_view(self):
        mealID=GlobalVariables.DB.DB_meal_find(self.mealNameInput.get_text())

        if mealID != -1:
            kcal=GlobalVariables.DB.get_meal_kcal(mealID)
            ingredientList=""
            for ingredient in GlobalVariables.DB.get_meal_ingredients(mealID):
                ingredientList+=ingredient[0]+"\t\t"+str(ingredient[1])+"\n"
            self.mealKcalView.set_text(str(kcal[0]))
            self.descInput.set_text(ingredientList)
        else:
            return


    def add_daily_meal(self):
        weights=re.findall('[0-9]+',self.descInput.get_text())
        mealID=GlobalVariables.DB.DB_meal_find(self.mealNameInput.get_text())
        ingredients=GlobalVariables.DB.get_meal_ingredients(mealID)

        for i in ingredients:
            GlobalVariables.DB.DB_record_insert(mealID,GlobalVariables.DB.DB_product_find(i[0]),weights[ingredients.index(i)])

        GlobalVariables.DB.Set_record_ID()
        GlobalVariables.DB.DB_daily_record_insert(GlobalVariables.DB.DB_record_find(mealID),GlobalVariables.userAccount)
        self.input_clear()

    def input_clear(self):
        self.descInput.clear()
        self.mealNameInput.clear()
        self.mealKcalView.clear()




