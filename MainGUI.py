import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QCompleter, QDesktopWidget
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QFont
from ProductAddGUI import ProductAddGUI
from MealAddGUI import MealAddGUI
from RecordAddGUI import RecordAddGui
from datetime import datetime
from BasicElementGUI import BasicElement
import random

class MainGUI(QWidget):

    def __init__(self, MainWindow):
        super().__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMaximumHeight(1080)
        MainWindow.setMaximumWidth(1920)
        MainWindow.setMinimumHeight(1080)
        MainWindow.setMinimumWidth(1920)
        MainWindow.setWindowTitle('Food Nutrition Manager')

        self.helpItem = BasicElement()
        fontWithSpacing=QtGui.QFont(self.helpItem.get_roboto_bold_font())
        fontWithSpacing.setLetterSpacing(QtGui.QFont.AbsoluteSpacing,2)
        fontRegularWithSpacing=QtGui.QFont(self.helpItem.get_roboto_regular_font())
        fontRegularWithSpacing.setLetterSpacing(QtGui.QFont.AbsoluteSpacing, 7)
        momCakeFont=QtGui.QFont(QtGui.QFontDatabase.applicationFontFamilies(
            QtGui.QFontDatabase.addApplicationFont("Fonts/MomcakeThin-9Y6aZ.otf"))[0])
        momCakeFontBold=QtGui.QFont(QtGui.QFontDatabase.applicationFontFamilies(
            QtGui.QFontDatabase.addApplicationFont("Fonts/LandasansMedium-ALJ6m.otf"))[0])
        fontRegular=QtGui.QFont(self.helpItem.get_roboto_regular_font())

        if QApplication.desktop().screenGeometry().width() == 1920 and QApplication.desktop().screenGeometry().height() == 1080:
            MainWindow.setWindowState(QtCore.Qt.WindowFullScreen)

        self.bgFrame = QtWidgets.QFrame(MainWindow)
        self.bgFrame.resize(1920, 1080)
        self.bgFrame.setStyleSheet("background-color:#22211d;")
        self.bgFrame.move(0, 0)

        self.sidePanel = QtWidgets.QFrame(self.bgFrame)
        self.sidePanel.resize(100, 1080)
        self.sidePanel.setStyleSheet("background-color:#343434;"
                                     "border-right:4px solid black;")

        self.upperPanel = QtWidgets.QFrame(self.bgFrame)
        self.upperPanelMainText = QtWidgets.QLabel(self.upperPanel)
        self.upperPanelMainText.setText("Food Nutrition Manager")
        QtGui.QFontDatabase.applicationFontFamilies(
            QtGui.QFontDatabase.addApplicationFont("Fonts/LandasansUltraLight - qZ080.otf"))

        self.upperPanelMainText.setFont(momCakeFont)

        self.upperPanelMainText.setStyleSheet("color:#fff;font-size:50px;border:none;font-weight:700")
        self.upperPanelMainText.move(20, 10)
        self.upperPanel.resize(1820, 80)
        self.upperPanel.move(100, 0)
        self.upperPanel.setStyleSheet("background-color:#343434;"
                                      "border-bottom:4px solid black;")

        self.sidePanelLogo = QtWidgets.QFrame(self.sidePanel)
        self.sidePanelLogo.resize(100, 80)
        self.sidePanelLogo.setStyleSheet("border-bottom:4px solid black;")

        self.logoLabel = QtWidgets.QLabel(self.sidePanelLogo)
        self.logoLabel.resize(80, 80)
        self.logoLabel.setPixmap(QtGui.QPixmap("graphics/logo.png").scaled(70, 70, QtCore.Qt.KeepAspectRatio))
        self.logoLabel.setStyleSheet("background-color:none;")
        self.logoLabel.move(15, 1)

        self.homeButton = QtWidgets.QPushButton(self.sidePanel)
        self.homeButton.resize(96, 100)
        self.homeButton.move(0, 80)
        self.homeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homeButton.setStyleSheet("QPushButton:hover {    \n"
                                      "    background-color: #8e8e8e;\n"
                                      "}"
                                      "QPushButton {    \n"
                                      "    border:none;"
                                      "    icon:url(\"graphics/005-home.png\");"
                                      "    icon-size:64px;"
                                      "    border-right:8px solid #117182;"
                                      "}"
                                      )

        self.productAddButton = QtWidgets.QPushButton(self.sidePanel)
        self.productAddButton.resize(96, 100)
        self.productAddButton.move(0, 180)
        self.productAddButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.productAddButton.setStyleSheet("QPushButton:hover {    \n"
                                            "    background-color: #8e8e8e;\n"
                                            "}"
                                            "QPushButton {    \n"
                                            "    border:none;"
                                            "    icon:url(\"graphics/002-product.png\");"
                                            "    icon-size:64px;"
                                            "}"
                                            )

        self.mealAddButton = QtWidgets.QPushButton(self.sidePanel)
        self.mealAddButton.resize(96, 100)
        self.mealAddButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mealAddButton.move(0, 280)
        self.mealAddButton.setStyleSheet("QPushButton:hover {    \n"
                                         "    background-color: #8e8e8e;\n"
                                         "}"
                                         "QPushButton {    \n"
                                         "    border:none;"
                                         "    icon:url(\"graphics/008-turkey.png\");"
                                         "    icon-size:64px;"
                                         "}"
                                         )

        self.recordAddButton = QtWidgets.QPushButton(self.sidePanel)
        self.recordAddButton.resize(96, 100)
        self.recordAddButton.move(0, 380)
        self.recordAddButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recordAddButton.setStyleSheet("QPushButton:hover {    \n"
                                           "    background-color: #8e8e8e;\n"
                                           "}"
                                           "QPushButton {    \n"
                                           "    border:none;"
                                           "    icon:url(\"graphics/001-add.png\");"
                                           "    icon-size:64px;"
                                           "}"
                                           )

        self.removeRecordButton = QtWidgets.QPushButton(self.sidePanel)
        self.removeRecordButton.resize(96, 100)
        self.removeRecordButton.move(0, 480)
        self.removeRecordButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.removeRecordButton.setStyleSheet("QPushButton:hover {    \n"
                                              "    background-color: #8e8e8e;\n"
                                              "}"
                                              "QPushButton {    \n"
                                              "    border:none;"
                                              "    icon:url(\"graphics/007-rubbish-bin.png\");"
                                              "    icon-size:64px;"
                                              "}"
                                              )

        self.productRemoveButton = QtWidgets.QPushButton(self.sidePanel)
        self.productRemoveButton.resize(96, 100)
        self.productRemoveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.productRemoveButton.move(0, 580)
        self.productRemoveButton.setStyleSheet("QPushButton:hover {    \n"
                                               "    background-color: #8e8e8e;\n"
                                               "}"
                                               "QPushButton {    \n"
                                               "    border:none;"
                                               "    icon:url(\"graphics/006-no-food.png\");"
                                               "    icon-size:64px;"
                                               "}"
                                               )

        self.settingsButton = QtWidgets.QPushButton(self.sidePanel)
        self.settingsButton.resize(96, 100)
        self.settingsButton.move(0, 680)
        self.settingsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settingsButton.setStyleSheet("QPushButton:hover {    \n"
                                          "    background-color: #8e8e8e;\n"
                                          "}"
                                          "QPushButton {    \n"
                                          "    border:none;"
                                          "    icon:url(\"graphics/003-gear.png\");"
                                          "    icon-size:64px;"
                                          "}"
                                          )

        self.exitButton = QtWidgets.QPushButton(self.sidePanel)
        self.exitButton.resize(96, 100)
        self.exitButton.move(0, 980)
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setStyleSheet("QPushButton:hover {    \n"
                                      "    background-color: #8e8e8e;\n"
                                      "}"
                                      "QPushButton {    \n"
                                      "    border:none;"
                                      "    icon:url(\"graphics/004-power.png\");"
                                      "    icon-size:64px;"
                                      "}"
                                      )


        self.workingSpaceForOtherScreens=QtWidgets.QFrame(self.bgFrame)
        self.workingSpaceForOtherScreens.resize(1820,1000)
        self.workingSpaceForOtherScreens.move(100,80)

        self.workingSpace = QtWidgets.QFrame(self.bgFrame)
        self.workingSpace.resize(1820, 1000)
        self.workingSpace.move(100, 80)


        self.productAddGUI=ProductAddGUI(self.workingSpaceForOtherScreens)
        self.mealAddGUI = MealAddGUI(self.workingSpaceForOtherScreens)
        self.recordAddGUI=RecordAddGui(self.workingSpaceForOtherScreens)


        screenList=[self.productAddGUI,self.workingSpace, self.mealAddGUI,self.recordAddGUI]

        self.firstWidget = QtWidgets.QFrame(self.workingSpace)
        self.firstWidgetBar = QtWidgets.QFrame(self.firstWidget)
        self.firstWidgetBar.resize(480, 40)
        self.firstWidgetBar.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.948864, y1:0.716136, x2:1, y2:0, stop:0.164773 rgba(70,70,70,1), stop:0.988636 rgba(52,52,52,1));")
        self.firstWidgetLabel = QtWidgets.QLabel(self.firstWidgetBar)
        self.firstWidgetLabel.setText("WEEK SUMMARY")
        self.firstWidgetLabel.setStyleSheet("color:#fff;font-size:32px;padding:7px;")
        self.firstWidget.resize(480, 286)
        self.firstWidget.setStyleSheet("background-color:#343434;")
        self.firstWidget.move(50, 30)

        self.weekSummaryList=QtWidgets.QListWidget(self.firstWidget)
        self.weekSummaryList.resize(480,246)
        self.weekSummaryList.move(0,40)
        self.weekSummaryList.setStyleSheet("QListWidget{"
                                           "color:#fff;"
                                           "border:none;"
                                           "padding-top:5px;}"
                                           "QListWidget:item{"
                                           "padding:4px;}"
                                           "QListWidget:item:hover{"
                                           "background-color:#117182;}"
                                           "QListWidget:item:selected{"
                                           "background-color:#42afc2;}"
                                           )
        self.weekSummaryList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.weekSummaryList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        for i in range(7):
            item = QtWidgets.QListWidgetItem("Day: 22.02.2021\tEaten: {} Kcal\tLeft: {} Kcal".format(random.randrange(1500,1800),random.randrange(100,300)), self.weekSummaryList)
            item.setTextAlignment(QtCore.Qt.AlignHCenter)



        self.firstWidget.setGraphicsEffect(self.shadow_make())
        self.firstWidgetBar.setGraphicsEffect(self.shadow_make())
        self.firstWidgetLabel.setFont(momCakeFont)
        self.firstWidgetLabel.resize(480,40)
        self.firstWidgetBar.show()
        self.firstWidgetBar.raise_()


        self.secondWidget = QtWidgets.QFrame(self.workingSpace)
        self.secondWidget.resize(600, 286)
        self.secondWidget.setStyleSheet("background-color:#343434;")
        self.secondWidget.move(580, 30)
        self.secondWidgetBar = QtWidgets.QFrame(self.secondWidget)
        self.secondWidgetBar.resize(600, 40)
        self.secondWidgetBar.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.948864, y1:0.716136, x2:1, y2:0, stop:0.164773 rgba(70,70,70,1), stop:0.988636 rgba(52,52,52,1));")
        self.secondWidgetLabel = QtWidgets.QLabel(self.secondWidgetBar)

        self.secondWidgetLabel.setText("AVERAGE KILOCALORIES INTAKE")
        self.secondWidgetLabel.setStyleSheet("color:#fff;font-size:32px;padding:7px;")
        self.secondWidgetLabel.setFont(momCakeFont)
        self.secondWidgetLabel.resize(600,40)
        self.secondWidget.setGraphicsEffect(self.shadow_make())
        self.secondWidgetBar.setGraphicsEffect(self.shadow_make())

        self.dailyAvgFrame=QtWidgets.QFrame(self.secondWidget)
        self.dailyAvgFrame.resize(255,206)
        self.dailyAvgFrame.move(20,60)

        self.dailyAvgCounter=QtWidgets.QLabel(self.dailyAvgFrame)
        self.dailyAvgCounter.setMinimumWidth(255)
        self.dailyAvgCounter.setText("1789")
        self.dailyAvgCounter.setAlignment(QtCore.Qt.AlignHCenter)
        self.dailyAvgCounter.setStyleSheet("color:#fff;font-size:64px")
        self.dailyAvgCounter.move(0,27)


        self.dailyAvgCounter.setFont(fontWithSpacing)

        self.avgHR=QtWidgets.QLabel(self.dailyAvgFrame)
        self.avgHR.resize(185,2)
        self.avgHR.setStyleSheet("background-color:#fff;border:2px solid #fff")
        self.avgHR.move(40,112)


        self.dailyAvgLabel = QtWidgets.QLabel(self.dailyAvgFrame)
        self.dailyAvgLabel.setMinimumWidth(255)
        self.dailyAvgLabel.setAlignment(QtCore.Qt.AlignHCenter)
        self.dailyAvgLabel.setText("DAILY")
        self.dailyAvgLabel.setStyleSheet("color:#fff;font-size:32px;font-weight:400;")
        self.dailyAvgLabel.setFont(fontRegularWithSpacing)
        self.dailyAvgLabel.move(5,127)

        self.dailyAvgLabelKcalFrame=QtWidgets.QFrame(self.dailyAvgFrame)
        self.dailyAvgLabelKcalFrame.move(195,40)

        self.dailyAvgKcalLab=QtWidgets.QLabel(self.dailyAvgLabelKcalFrame)
        self.dailyAvgKcalLab.setText("KCAL")
        self.dailyAvgKcalLab.setStyleSheet("color:#fff;font-size:20px;")
        self.dailyAvgKcalLab.setFont(self.helpItem.get_roboto_bold_font())
        self.dailyAvgKcalLab.move(2,0)
        self.dailyAvgLabelKcalFrame.setMaximumWidth(50)

        self.dailyAvgKcalProcent=QtWidgets.QLabel(self.dailyAvgLabelKcalFrame)
        self.dailyAvgKcalProcent.move(16,21)
        self.dailyAvgKcalProcent.setText("0.5%")
        self.dailyAvgKcalProcent.setStyleSheet("color:green;font-size:16px;")
        self.dailyAvgKcalProcent.setFont(self.helpItem.get_roboto_bold_font())

        self.procentImg=QtWidgets.QLabel(self.dailyAvgLabelKcalFrame)
        self.procentImg.setPixmap(QtGui.QPixmap("graphics/001-triangle.png").scaled(16, 16, QtCore.Qt.KeepAspectRatio,
                                                                                    QtCore.Qt.SmoothTransformation))
        self.procentImg.move(0,21)

        self.weeklyAvgFrame=QtWidgets.QFrame(self.secondWidget)
        self.weeklyAvgFrame.resize(270,206)
        self.weeklyAvgFrame.move(280,60)



        self.weeklyAvgCounter=QtWidgets.QLabel(self.weeklyAvgFrame)
        self.weeklyAvgCounter.setMinimumWidth(255)
        self.weeklyAvgCounter.setText("12589")
        self.weeklyAvgCounter.setAlignment(QtCore.Qt.AlignHCenter)
        self.weeklyAvgCounter.setStyleSheet("color:#fff;font-size:64px")
        self.weeklyAvgCounter.setFont(fontWithSpacing)
        self.weeklyAvgCounter.move(0, 27)

        self.avgHR2=QtWidgets.QLabel(self.weeklyAvgFrame)
        self.avgHR2.resize(195,2)
        self.avgHR2.setStyleSheet("background-color:#fff;border:2px solid #fff")
        self.avgHR2.move(37,112)

        self.weeklyAvgLabel = QtWidgets.QLabel(self.weeklyAvgFrame)
        self.weeklyAvgLabel.setMinimumWidth(270)
        self.weeklyAvgLabel.setAlignment(QtCore.Qt.AlignHCenter)
        self.weeklyAvgLabel.setText("WEEKLY")
        self.weeklyAvgLabel.setStyleSheet("color:#fff;font-size:32px;")
        self.weeklyAvgLabel.setFont(fontRegularWithSpacing)
        self.weeklyAvgLabel.move(0,127)

        self.weeklyAvgLabelKcalFrame = QtWidgets.QFrame(self.weeklyAvgFrame)
        self.weeklyAvgLabelKcalFrame.move(215, 40)

        self.weeklyAvgKcalLab = QtWidgets.QLabel(self.weeklyAvgLabelKcalFrame)
        self.weeklyAvgKcalLab.setText("KCAL")
        self.weeklyAvgKcalLab.setStyleSheet("color:#fff;font-size:20px;")
        self.weeklyAvgKcalLab.setFont(self.helpItem.get_roboto_bold_font())
        self.weeklyAvgKcalLab.move(2, 0)
        self.weeklyAvgLabelKcalFrame.setMaximumWidth(50)

        self.weeklyAvgKcalProcent = QtWidgets.QLabel(self.weeklyAvgLabelKcalFrame)
        self.weeklyAvgKcalProcent.move(16, 19)
        self.weeklyAvgKcalProcent.setText("0.5%")
        self.weeklyAvgKcalProcent.setStyleSheet("color:rgb(249, 0, 0);font-size:16px;")
        self.weeklyAvgKcalProcent.setFont(self.helpItem.get_roboto_bold_font())

        self.procentImgWeek = QtWidgets.QLabel(self.weeklyAvgLabelKcalFrame)
        self.procentImgWeek.setPixmap(QtGui.QPixmap("graphics/red-arrow.png").scaled(16, 16, QtCore.Qt.KeepAspectRatio,
                                                                                    QtCore.Qt.SmoothTransformation))
        self.procentImgWeek.move(0, 21)


        self.thirdWidget = QtWidgets.QFrame(self.workingSpace)
        self.thirdWidget.resize(480, 286)
        self.thirdWidget.setStyleSheet("background-color:#343434;")
        self.thirdWidget.move(50, 346)
        self.thirdWidgetBar = QtWidgets.QFrame(self.thirdWidget)
        self.thirdWidgetBar.resize(480, 40)
        self.thirdWidgetBar.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.948864, y1:0.716136, x2:1, y2:0, stop:0.164773 rgba(70,70,70,1), stop:0.988636 rgba(52,52,52,1));")
        self.thirdWidgetLabel = QtWidgets.QLabel(self.thirdWidgetBar)
        self.thirdWidgetLabel.setFont(momCakeFont)
        self.thirdWidgetLabel.resize(480,40)
        self.thirdWidgetLabel.setFont(momCakeFont)
        self.thirdWidgetLabel.setText("Third Widget")
        self.thirdWidgetLabel.setStyleSheet("color:#fff;font-size:32px;padding:7px;")
        self.thirdWidget.setGraphicsEffect(self.shadow_make())
        self.thirdWidgetBar.setGraphicsEffect(self.shadow_make())

        self.fourthWidget = QtWidgets.QFrame(self.workingSpace)
        self.fourthWidget.resize(600, 286)
        self.fourthWidget.setStyleSheet("background-color:#343434;")
        self.fourthWidget.move(580, 346)
        self.fourthWidgetBar = QtWidgets.QFrame(self.fourthWidget)
        self.fourthWidgetBar.resize(600, 40)
        self.fourthWidgetBar.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.948864, y1:0.716136, x2:1, y2:0, stop:0.164773 rgba(70,70,70,1), stop:0.988636 rgba(52,52,52,1));")
        self.fourthWidgetLabel = QtWidgets.QLabel(self.fourthWidgetBar)
        self.fourthWidgetLabel.setText("Third Widget")
        self.fourthWidgetLabel.resize(600,40)
        self.fourthWidgetLabel.setFont(momCakeFont)
        self.fourthWidgetLabel.setStyleSheet("color:#fff;font-size:32px;padding:7px;")
        self.fourthWidget.setGraphicsEffect(self.shadow_make())
        self.fourthWidgetBar.setGraphicsEffect(self.shadow_make())

        self.fifthWidget = QtWidgets.QFrame(self.workingSpace)
        self.fifthWidget.resize(540, 602)
        self.fifthWidget.setStyleSheet("background-color:#343434;")
        self.fifthWidget.move(1230, 30)
        self.fifthWidgetBar = QtWidgets.QFrame(self.fifthWidget)
        self.fifthWidgetBar.resize(540, 40)
        self.fifthWidgetBar.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.948864, y1:0.716136, x2:1, y2:0, stop:0.164773 rgba(70,70,70,1), stop:0.988636 rgba(52,52,52,1));")
        self.fifthWidget.setGraphicsEffect(self.shadow_make())

        self.fifthWidgetBar.setGraphicsEffect(self.shadow_make(20))

        self.recipeSearchFrame = QtWidgets.QFrame(self.fifthWidgetBar)
        self.recipeSearchFrame.resize(400, 38)
        self.recipeSearchFrame.move(230, 0)
        self.recipeSearchFrame.setStyleSheet("background-color:none;")

        self.recipeLabel = QtWidgets.QLabel(self.recipeSearchFrame)
        self.recipeLabel.setText("Search: ")
        self.recipeLabel.setFont(momCakeFont)
        self.recipeLabel.setMinimumHeight(40)
        self.recipeLabel.setStyleSheet("color:#fff;font-size:28px;")


        self.recipeInput = QtWidgets.QLineEdit(self.recipeSearchFrame)
        self.recipeInput.resize(200, 30)
        self.recipeInput.move(95, 6)
        self.recipeInput.setStyleSheet(
            "selection-background-color: #117182; background-color:rgba(70,70,70,1); border: 5px solid #343434;color:#fff;")


        self.fifthWidgetLabel = QtWidgets.QLabel(self.fifthWidgetBar)
        self.fifthWidgetLabel.setText("RECIPES")
        self.fifthWidgetLabel.resize(200,40)
        self.fifthWidgetLabel.setFont(momCakeFont)
        self.fifthWidgetLabel.setStyleSheet("color:#fff;font-size:32px;padding:7px;")

        self.recipeSpace = QtWidgets.QFrame(self.fifthWidget)
        self.recipeSpace.resize(540, 532)
        self.recipeSpace.move(0, 65)
        self.recipeTitle = QtWidgets.QLabel(self.recipeSpace)
        self.recipeTitle.setText("Recipe name")
        self.recipeTitle.setStyleSheet("color:#fff;font-size:40px;font-weight:700;font-family:Bahnschrift")
        self.recipeTitle.move(15, 0)
        self.recipeText = QtWidgets.QFrame(self.recipeSpace)
        self.recipeText.setMaximumWidth(600)
        self.recipeText.setMinimumWidth(520)
        self.recipeText.setMinimumHeight(400)
        self.recipeText.move(20, 60)
        self.ingredientsBox = QtWidgets.QTextBrowser(self.recipeText)
        self.ingredientsBox.setMaximumWidth(460)
        self.ingredientsBox.setMaximumHeight(150)
        self.ingredientsBox.setMinimumHeight(100)
        self.ingredientsBox.verticalScrollBar().setVisible(False)
        self.ingredientsBox.setStyleSheet("border:none;color:#fff;font-size:18px;")
        self.ingredientsBox.setText("""<b style='font-size:22px;'>Ingredients</b>
        <ul>
        <li>Sos Boloński Winiary 250g</li>
        <li>Corn 150g</li>
        <li>Lattice 180g</li>
        <li>Pepper 20g</li></ul>""")
        self.ingredientsBox.setFont(fontRegular)
        self.recipeTextBox = QtWidgets.QTextBrowser(self.recipeText)
        self.recipeTextBox.setStyleSheet("color:#fff;border:none;font-size:18px;")
        self.recipeTextBox.setMaximumWidth(460)
        self.recipeTextBox.setMinimumHeight(720)
        self.recipeTextBox.setFont(fontRegular)
        self.recipeTextBox.setText("""<b style='font-size:22px;'>Description</b><br /><br />
            
            Lorem dipsum dolor sit amet, consectetur adipiscing elit. Proin eget ipsum ex. Ut dapibus placerat finibus. In eget consequat metus. Nullam lorem elit, pellentesque et turpis at, faucibus porttitor elit. In imperdiet ullamcorper gravida. Cras id vestibulum odio. Sed blandit pretium pharetra. Donec blandit at orci et luctus. <br /><br />

    Quisque id dolor ut dolor tempus sagittis vitae non augue. Quisque dignissim tempor risus. Morbi in vulputate erat. Mauris ullamcorper volutpat eros, vel semper odio egestas non. Suspendisse potenti. Donec vel quam nec elit commodo sollicitudin quis nec lectus. Curabitur vitae justo ut augue mollis dictum. Fusce lectus ante, accumsan sed pulvinar ut, volutpat nec odio. Nam nec tellus mauris. Donec rutrum commodo sem nec mattis. Cras in ligula ante. In venenatis libero urna, vitae gravida eros ultricies ac. <br /><br />

    Vivamus fringilla felis a erat auctor, lobortis scelerisque est vehicula. Proin in imperdiet mauris, vel ullamcorper felis. In erat est, eleifend id pretium vitae, accumsan eget sem. Integer porta purus ac quam cursus, in eleifend sem vulputate. Duis feugiat, dui nec porta consectetur, magna libero posuere ligula, nec rutrum urna felis vitae lectus. Nullam egestas ullamcorper ipsum id feugiat. Suspendisse eu nisl pellentesque, placerat purus eu, cursus justo.
        """)
        self.recipeTextBox.verticalScrollBar().setVisible(False)

        self.recipeVerticalLayout = QtWidgets.QVBoxLayout(self.recipeText)
        self.recipeVerticalLayout.addWidget(self.ingredientsBox)
        self.recipeVerticalLayout.addWidget(self.recipeTextBox)

        self.recipeScrollArea = QtWidgets.QScrollArea(self.recipeSpace)
        self.recipeScrollArea.setWidget(self.recipeText)
        self.recipeScrollArea.move(20, 75)
        self.recipeScrollArea.horizontalScrollBar().setVisible(False)
        self.recipeScrollArea.setMinimumHeight(500)
        stylesheet = """
         /* --------------------------------------- QScrollBar  -----------------------------------*/
         QScrollBar:vertical
         {
             background-color: #2A2929;
             width: 15px;
             margin: 15px 3px 15px 3px;
             border: 1px transparent qlineargradient(spread:pad, x1:0.948864, y1:0.716136, x2:1, y2:0, stop:0.164773 rgba(70,70,70,1), stop:0.988636 rgba(52,52,52,1));
             border-radius: 4px;
         }

         QScrollBar::handle:vertical
         {
             background-color: rgba(142, 142, 142,0.95);         /* #605F5F; */
             min-height: 5px;
             border-radius: 4px;
         }
         
        QScrollBar::handle:vertical:hover
         {
             background-color: red;         /* #605F5F; */
             min-height: 5px;
             border-radius: 4px;
             width:15px;
         }

         QScrollBar::sub-line:vertical
         {
             margin: 3px 0px 3px 0px;
             border-image: url(:/images/up_arrow_disabled.png);        /* # <-------- */
             height: 10px;
             width: 10px;
             subcontrol-position: top;
             subcontrol-origin: margin;
         }

         QScrollBar::add-line:vertical
         {
             margin: 3px 0px 3px 0px;
             border-image: url(:/g);       /* # <-------- */
             height: 10px;
             width: 10px;
             subcontrol-position: bottom;
             subcontrol-origin: margin;
         }

         QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
         {
             background: none;
         }


         QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
         {
             background: none;
         }
        """
        self.recipeScrollArea.verticalScrollBar().setStyleSheet(stylesheet)
        self.recipeScrollArea.setStyleSheet("border:none;")
        self.sixthWidget = QtWidgets.QFrame(self.workingSpace)
        self.sixthWidget.resize(835, 286)
        self.sixthWidget.setStyleSheet("background-color:#343434;")
        self.sixthWidget.move(50, 662)
        self.sixthWidgetBar = QtWidgets.QFrame(self.sixthWidget)

        self.sixthWidgetBar.resize(835, 40)
        self.sixthWidgetBar.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.948864, y1:0.716136, x2:1, y2:0, stop:0.164773 rgba(70,70,70,1), stop:0.988636 rgba(52,52,52,1));")


        self.dayChoiceFrame = QtWidgets.QFrame(self.sixthWidgetBar)
        self.dayChoiceFrame.resize(400, 32)
        self.dayChoiceFrame.move(660, 4)
        self.dayChoiceFrame.setStyleSheet("background-color:none;")

        self.dayLabel = QtWidgets.QLabel(self.dayChoiceFrame)
        self.dayLabel.setText("{}".format(datetime.today().date().strftime('%d.%m.%Y')))
        self.dayLabel.setFont(momCakeFontBold)
        self.dayLabel.setStyleSheet("color:#fff;font-size:26px;")
        self.dayLabel.setMinimumHeight(32)
        self.dayLabel.move(20,0)

        self.dayCalendarLabel = QtWidgets.QLabel(self.dayChoiceFrame)
        self.dayCalendarLabel.resize(30, 30)
        self.dayCalendarLabel.move(110, 2)
        self.dayCalendarLabel.setStyleSheet(
            "border: none;")

        self.dayCalendarLabel.setPixmap(QtGui.QPixmap("graphics/003-calendar.png").scaled(30, 30, QtCore.Qt.KeepAspectRatio))
        self.dayCalendarLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.sixthWidgetLabel = QtWidgets.QLabel(self.sixthWidgetBar)
        self.sixthWidgetLabel.setText("DAY SUMMARY")
        self.sixthWidgetLabel.resize(300,40)
        self.sixthWidgetLabel.setFont(momCakeFont)
        self.sixthWidgetLabel.setStyleSheet("color:#fff;font-size:32px;padding:7px;")

        self.todayTable=QtWidgets.QTableWidget(8,7,self.sixthWidget)
        self.todayTable.resize(835,246)
        self.todayTable.move(0,40)
        self.sixthWidget.setGraphicsEffect(self.shadow_make())
        self.sixthWidgetBar.setGraphicsEffect(self.shadow_make())
        self.sixthWidgetBar.show()
        self.sixthWidgetBar.raise_()

        self.todayTable.setStyleSheet("QTableWidget{border:none;"
                                      "gridline-color:#117182;"
                                      "color:#fff;"
                                      "font-size:20px;}"
                                      "QTableWidget::Item:selected{"
                                      "background-color:#42afc2;}"
                                      "QTableWidget::Item:hover{"
                                      "background-color:rgba(17,113,130,50);}")
        self.todayTable.setFont(fontRegular)
        self.todayTable.verticalHeader().hide()
        self.todayTable.horizontalHeader().hide()
        self.todayTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.todayTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.todayTable.horizontalHeader().setDefaultSectionSize(94)
        self.todayTable.verticalHeader().setDefaultSectionSize(42)
        self.todayTable.setColumnWidth(0,275)
        alignment = QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter


        columnnNames=["Meal Name","Kcal","Carbo","Sugar","Protein","Fat","Price"]


        for name in columnnNames:
            item=QtWidgets.QTableWidgetItem(name)
            item.setTextAlignment(alignment)
            item.setBackground(QtGui.QColor(17, 113, 130,50))
            self.todayTable.setItem(0,columnnNames.index(name),item)


        self.seventhWidget = QtWidgets.QFrame(self.workingSpace)
        self.seventhWidget.resize(835, 286)
        self.seventhWidget.setStyleSheet("background-color:#343434;")
        self.seventhWidget.move(935, 662)
        self.seventhWidgetBar = QtWidgets.QFrame(self.seventhWidget)
        self.seventhWidgetBar.resize(835, 40)
        self.seventhWidgetBar.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.948864, y1:0.716136, x2:1, y2:0, stop:0.164773 rgba(70,70,70,1), stop:0.988636 rgba(52,52,52,1));")

        self.seventhWidget.setGraphicsEffect(self.shadow_make())
        self.seventhWidgetBar.setGraphicsEffect(self.shadow_make())

        self.seventhWidgetLabel = QtWidgets.QLabel(self.seventhWidgetBar)
        self.seventhWidgetLabel.setText("BASIC STATISTICS")
        self.seventhWidgetLabel.mousePressEvent=self.dosth
        self.seventhWidgetLabel.resize(600,40)
        self.seventhWidgetLabel.setFont(momCakeFont)
        self.seventhWidgetLabel.setStyleSheet("color:#fff;font-size:32px;padding:7px;")
        self.firstProgressBar = QtWidgets.QFrame(self.seventhWidget)
        self.firstProgressBar.resize(236, 236)
        self.firstProgressBar.move(32, 45)
        self.firstProgressBar.setStyleSheet("border-radius:118%")
        self.firstProgressBarProgress = QtWidgets.QFrame(self.firstProgressBar)
        self.firstProgressBarProgress.resize(236, 236)
        self.firstProgressBarProgress.setStyleSheet(
            "border-radius:118%;	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.799 rgba(142, 142, 142,0.95), stop:0.800 #ec008c);")
        self.firstProgressBarInnerBg = QtWidgets.QFrame(self.firstProgressBarProgress)
        self.firstProgressBarInnerBg.resize(206, 206)
        self.firstProgressBarInnerBg.move(15, 15)
        self.firstProgressBarInnerBg.setStyleSheet("background-color: rgba(70,70,70,1);border-radius:103%;")
        self.firstProgressBarTextFrame = QtWidgets.QFrame(self.firstProgressBarInnerBg)
        self.firstProgressBarTextFrame.setStyleSheet("background-color:none;")
        self.firstProgressBarTitle = QtWidgets.QLabel(self.firstProgressBarTextFrame)
        self.firstProgressBarTitle.setText("TODAY")
        self.firstProgressBarTitle.resize(206, 30)
        self.firstProgressBarTitle.move(0, 20)
        self.firstProgressBarTitle.setAlignment(QtCore.Qt.AlignHCenter)
        self.firstProgressBarTitle.setStyleSheet("color:#fff;font-weight:700;font-size:25px;text-align:center;")
        self.firstProgressBarProcent = QtWidgets.QLabel(self.firstProgressBarTextFrame)
        self.firstProgressBarProcent.setText("0<sup>%</sup>")
        self.firstProgressBarProcent.setAlignment(QtCore.Qt.AlignHCenter)
        self.firstProgressBarProcent.resize(206, 90)
        self.firstProgressBarProcent.move(10, 55)
        self.firstProgressBarProcent.setStyleSheet("color:#fff;font-weight:700;font-size:80px;text-align:center;")
        self.firstProgressBarLimitBG = QtWidgets.QFrame(self.firstProgressBarTextFrame)
        self.firstProgressBarLimitBG.resize(120, 35)
        self.firstProgressBarLimitBG.setStyleSheet(
            "background-color:#343434;border-radius:10%;")
        self.firstProgressBarLimitBG.move(43, 150)

        self.firstProgressBarLimit = QtWidgets.QLabel(self.firstProgressBarLimitBG)
        self.firstProgressBarLimit.resize(120, 35)
        self.firstProgressBarLimit.setStyleSheet(
            "background-color:none;color:#fff;text-align:center;font-weight:600;")
        self.firstProgressBarLimit.setAlignment(QtCore.Qt.AlignHCenter)
        self.firstProgressBarLimit.setText('<span style="text-align:center;">Limit: 1800</span>')
        self.firstProgressBarLimit.move(0, 8)

        self.secondProgressBar = QtWidgets.QFrame(self.seventhWidget)
        self.secondProgressBar.resize(236, 236)
        self.secondProgressBar.move(300, 45)
        self.secondProgressBar.setStyleSheet("border-radius:118%")
        self.secondProgressBarProgress = QtWidgets.QFrame(self.secondProgressBar)
        self.secondProgressBarProgress.resize(236, 236)
        self.secondProgressBarProgress.setStyleSheet(
            "border-radius:118%;	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.249 rgba(142, 142, 142,0.95), stop:0.250 #39b54a);")
        self.secondProgressBarInnerBg = QtWidgets.QFrame(self.secondProgressBarProgress)
        self.secondProgressBarInnerBg.resize(206, 206)
        self.secondProgressBarInnerBg.move(15, 15)
        self.secondProgressBarInnerBg.setStyleSheet("background-color: rgba(70,70,70,1);border-radius:103%;")
        self.secondProgressBarTextFrame = QtWidgets.QFrame(self.secondProgressBarInnerBg)
        self.secondProgressBarTextFrame.setStyleSheet("background-color:none;")
        self.secondProgressBarTitle = QtWidgets.QLabel(self.secondProgressBarTextFrame)
        self.secondProgressBarTitle.setText("BMI")
        self.secondProgressBarTitle.resize(206, 30)
        self.secondProgressBarTitle.move(0, 20)
        self.secondProgressBarTitle.setAlignment(QtCore.Qt.AlignHCenter)
        self.secondProgressBarTitle.setStyleSheet("color:#fff;font-weight:700;font-size:25px;text-align:center;")
        self.secondProgressBarProcent = QtWidgets.QLabel(self.secondProgressBarTextFrame)
        self.secondProgressBarProcent.setText("0<sup>%</sup>")
        self.secondProgressBarProcent.setAlignment(QtCore.Qt.AlignHCenter)
        self.secondProgressBarProcent.resize(206, 90)
        self.secondProgressBarProcent.move(10, 55)
        self.secondProgressBarProcent.setStyleSheet("color:#fff;font-weight:700;font-size:80px;text-align:center;")
        self.secondProgressBarLimitBG = QtWidgets.QFrame(self.secondProgressBarTextFrame)
        self.secondProgressBarLimitBG.resize(120, 35)
        self.secondProgressBarLimitBG.setStyleSheet(
            "background-color:#343434;border-radius:10%;")
        self.secondProgressBarLimitBG.move(43, 150)

        self.secondProgressBarLimit = QtWidgets.QLabel(self.secondProgressBarLimitBG)
        self.secondProgressBarLimit.resize(120, 35)
        self.secondProgressBarLimit.setStyleSheet(
            "background-color:none;color:#fff;text-align:center;font-weight:600;")
        self.secondProgressBarLimit.setAlignment(QtCore.Qt.AlignHCenter)
        self.secondProgressBarLimit.setText('<span style="text-align:center;">Goal: xx</span>')
        self.secondProgressBarLimit.move(0, 8)

        self.thirdProgressBar = QtWidgets.QFrame(self.seventhWidget)
        self.thirdProgressBar.resize(236, 236)
        self.thirdProgressBar.move(568, 45)
        self.thirdProgressBar.setStyleSheet("border-radius:118%")
        self.thirdProgressBarProgress = QtWidgets.QFrame(self.thirdProgressBar)
        self.thirdProgressBarProgress.resize(236, 236)
        self.thirdProgressBarProgress.setStyleSheet(
            "border-radius:118%;	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.549 rgba(142, 142, 142,0.95), stop:0.550 #6e41ff);")
        self.thirdProgressBarInnerBg = QtWidgets.QFrame(self.thirdProgressBarProgress)
        self.thirdProgressBarInnerBg.resize(206, 206)
        self.thirdProgressBarInnerBg.move(15, 15)
        self.thirdProgressBarInnerBg.setStyleSheet("background-color: rgba(70,70,70,1);border-radius:103%;")
        self.thirdProgressBarTextFrame = QtWidgets.QFrame(self.thirdProgressBarInnerBg)
        self.thirdProgressBarTextFrame.setStyleSheet("background-color:none;")
        self.thirdProgressBarTitle = QtWidgets.QLabel(self.thirdProgressBarTextFrame)
        self.thirdProgressBarTitle.setText("WEEK")
        self.thirdProgressBarTitle.resize(206, 30)
        self.thirdProgressBarTitle.move(0, 20)
        self.thirdProgressBarTitle.setAlignment(QtCore.Qt.AlignHCenter)
        self.thirdProgressBarTitle.setStyleSheet("color:#fff;font-weight:700;font-size:25px;text-align:center;")
        self.thirdProgressBarProcent = QtWidgets.QLabel(self.thirdProgressBarTextFrame)
        self.thirdProgressBarProcent.setText("0<sup>%</sup>")
        self.thirdProgressBarProcent.setAlignment(QtCore.Qt.AlignHCenter)
        self.thirdProgressBarProcent.resize(206, 90)
        self.thirdProgressBarProcent.move(10, 55)
        self.thirdProgressBarProcent.setStyleSheet("color:#fff;font-weight:700;font-size:80px;text-align:center;")
        self.thirdProgressBarLimitBG = QtWidgets.QFrame(self.thirdProgressBarTextFrame)
        self.thirdProgressBarLimitBG.resize(120, 35)
        self.thirdProgressBarLimitBG.setStyleSheet(
            "background-color:#343434;border-radius:10%;")
        self.thirdProgressBarLimitBG.move(43, 150)

        self.thirdProgressBarLimit = QtWidgets.QLabel(self.thirdProgressBarLimitBG)
        self.thirdProgressBarLimit.resize(120, 35)
        self.thirdProgressBarLimit.setStyleSheet(
            "background-color:none;color:#fff;text-align:center;font-weight:600;")
        self.thirdProgressBarLimit.setAlignment(QtCore.Qt.AlignHCenter)
        self.thirdProgressBarLimit.setText('<span style="text-align:center;">Limit: 12600</span>')
        self.thirdProgressBarLimit.move(0, 8)

        self.mainScreenWidgets = [self.firstWidget, self.secondWidget, self.thirdWidget, self.fourthWidget,
                                  self.fifthWidget, self.sixthWidget, self.seventhWidget]

        self.productAddButton.clicked.connect(lambda: self.product_add_button(screenList))
        self.homeButton.clicked.connect(lambda: self.home_screen_button(screenList))
        self.exitButton.clicked.connect(self.exit_button)
        self.mealAddButton.clicked.connect(lambda: self.meal_add_button(screenList))
        self.productRemoveButton.clicked.connect(self.product_remove_button)
        self.recordAddButton.clicked.connect(lambda: self.record_add_button(screenList))
        self.removeRecordButton.clicked.connect(self.record_remove_button)
        self.settingsButton.clicked.connect(self.settings_button)


    def hide_all_screens(self, screenList):
        for widget in screenList:
            widget.hide()

    def panel_marker_off(self):
        buttons = [self.settingsButton, self.mealAddButton, self.productRemoveButton, self.removeRecordButton,
                   self.productAddButton, self.homeButton, self.recordAddButton]
        for button in buttons:
            button.setStyleSheet("%s QPushButton {border:none;}" % button.styleSheet())

    def home_screen_button(self,screenList):
        self.hide_all_screens(screenList)
        self.workingSpace.show()
        temp = self.homeButton.styleSheet()
        self.panel_marker_off()
        self.homeButton.setStyleSheet("%s QPushButton {border-right:8px solid #117182;}" % temp)

    def meal_add_button(self,screenList):
        self.hide_all_screens(screenList)
        temp = self.mealAddButton.styleSheet()
        self.panel_marker_off()
        self.mealAddButton.setStyleSheet("%s QPushButton {border-right:8px solid #117182;}" % temp)
        self.mealAddGUI.show()

    def product_add_button(self,screenList):
        self.hide_all_screens(screenList)
        temp = self.productAddButton.styleSheet()
        self.panel_marker_off()
        self.productAddButton.setStyleSheet("%s QPushButton {border-right:8px solid #117182;}" % temp)
        self.productAddGUI.show()


    def record_add_button(self,screenList):
        self.hide_all_screens(screenList)
        temp = self.recordAddButton.styleSheet()
        self.panel_marker_off()
        self.recordAddButton.setStyleSheet("%s QPushButton {border-right:8px solid #117182;}" % temp)
        self.recordAddGUI.show()

    def record_remove_button(self):
        self.window_visible(self.mainScreenWidgets, False)
        temp = self.removeRecordButton.styleSheet()
        self.panel_marker_off()
        self.removeRecordButton.setStyleSheet("%s QPushButton {border-right:8px solid #117182;}" % temp)

    def product_remove_button(self):
        self.window_visible(self.mainScreenWidgets, False)
        temp = self.productRemoveButton.styleSheet()
        self.panel_marker_off()
        self.productRemoveButton.setStyleSheet("%s QPushButton {border-right:8px solid #117182;}" % temp)

    def settings_button(self):
        self.window_visible(self.mainScreenWidgets, False)
        temp = self.settingsButton.styleSheet()
        self.panel_marker_off()
        self.settingsButton.setStyleSheet("%s QPushButton {border-right:8px solid #117182;}" % temp)

    def exit_button(self):
        temp = self.exitButton.styleSheet()
        self.panel_marker_off()
        self.exitButton.setStyleSheet("%s QPushButton {border-right:8px solid #117182;}" % temp)
        sys.exit(app.exec_())

    def shadow_make(self, blur=20, xOff=0, yOff=0):
        shadowObj = QtWidgets.QGraphicsDropShadowEffect()
        shadowObj.setColor(QtGui.QColor(0, 0, 0))
        shadowObj.setBlurRadius(blur)
        shadowObj.setXOffset(xOff)
        shadowObj.setYOffset(yOff)
        return shadowObj

    def show(self):
        self.workingSpace.setVisible(True)

    def hide(self):
        self.workingSpace.setVisible(False)

    def dosth(self, event):
            print("test")

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainGUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
