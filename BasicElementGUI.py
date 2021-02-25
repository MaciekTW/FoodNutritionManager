from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QCompleter, QDesktopWidget,QLabel,QFrame,QLineEdit
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QFont


class BasicElement:
    def __init__(self, xpos=0,ypos=0, width=0, height=0, where=0):
        self.x=xpos
        self.y=ypos
        self.width=width
        self.height=height
        self.startFrame=where


    def shadow_make(self, blur=20, xOff=0, yOff=0):
        shadowObj = QtWidgets.QGraphicsDropShadowEffect()
        shadowObj.setColor(QtGui.QColor(0, 0, 0))
        shadowObj.setBlurRadius(blur)
        shadowObj.setXOffset(xOff)
        shadowObj.setYOffset(yOff)
        return shadowObj

    def get_roboto_regular_font(self):
        robotoFontFamily = QtGui.QFontDatabase.applicationFontFamilies(
            QtGui.QFontDatabase.addApplicationFont("Fonts/Roboto-Regular.ttf"))

        return QFont(robotoFontFamily[0])

    def get_roboto_medium_font(self):
        robotoFontFamily = QtGui.QFontDatabase.applicationFontFamilies(
            QtGui.QFontDatabase.addApplicationFont("Fonts/Roboto-Medium.ttf"))

        return QFont(robotoFontFamily[0])

    def get_roboto_bold_font(self):
        robotoFontFamily = QtGui.QFontDatabase.applicationFontFamilies(
            QtGui.QFontDatabase.addApplicationFont("Fonts/Roboto-BoldCondensed.ttf"))

        return QFont(robotoFontFamily[0])

    def get_roboto_italic_font(self):
        robotoFontFamily = QtGui.QFontDatabase.applicationFontFamilies(
            QtGui.QFontDatabase.addApplicationFont("Fonts/Roboto-MediumItalic.ttf"))

        return QFont(robotoFontFamily[0])



    def dupa(self):
        return