# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from MyGraphicsStuff import MyGraphicsView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1030, 981)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.gView = MyGraphicsView(self.centralwidget)
        self.gView.setObjectName(u"gView")
        self.gView.setMinimumSize(QSize(0, 0))
        self.gView.setFrameShape(QFrame.Box)
        self.gView.setRenderHints(QPainter.Antialiasing|QPainter.HighQualityAntialiasing|QPainter.SmoothPixmapTransform|QPainter.TextAntialiasing)
        self.gView.setCacheMode(QGraphicsView.CacheNone)

        self.verticalLayout.addWidget(self.gView)

        self.scaleSlider = QSlider(self.centralwidget)
        self.scaleSlider.setObjectName(u"scaleSlider")
        self.scaleSlider.setMaximum(200)
        self.scaleSlider.setOrientation(Qt.Horizontal)
        self.scaleSlider.setInvertedAppearance(False)
        self.scaleSlider.setInvertedControls(False)

        self.verticalLayout.addWidget(self.scaleSlider)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.viewSceneRect = QLabel(self.centralwidget)
        self.viewSceneRect.setObjectName(u"viewSceneRect")

        self.gridLayout.addWidget(self.viewSceneRect, 5, 0, 1, 1)

        self.dzoneSize = QLabel(self.centralwidget)
        self.dzoneSize.setObjectName(u"dzoneSize")

        self.gridLayout.addWidget(self.dzoneSize, 4, 3, 1, 1)

        self.l14 = QLabel(self.centralwidget)
        self.l14.setObjectName(u"l14")

        self.gridLayout.addWidget(self.l14, 5, 2, 1, 1)

        self.viewSize = QLabel(self.centralwidget)
        self.viewSize.setObjectName(u"viewSize")

        self.gridLayout.addWidget(self.viewSize, 4, 2, 1, 1)

        self.viewPos = QLabel(self.centralwidget)
        self.viewPos.setObjectName(u"viewPos")

        self.gridLayout.addWidget(self.viewPos, 0, 0, 1, 1)

        self.l5 = QLabel(self.centralwidget)
        self.l5.setObjectName(u"l5")

        self.gridLayout.addWidget(self.l5, 1, 2, 1, 1)

        self.l4 = QLabel(self.centralwidget)
        self.l4.setObjectName(u"l4")

        self.gridLayout.addWidget(self.l4, 1, 0, 1, 1)

        self.l10 = QLabel(self.centralwidget)
        self.l10.setObjectName(u"l10")

        self.gridLayout.addWidget(self.l10, 3, 0, 1, 1)

        self.l12 = QLabel(self.centralwidget)
        self.l12.setObjectName(u"l12")

        self.gridLayout.addWidget(self.l12, 3, 3, 1, 1)

        self.l7 = QLabel(self.centralwidget)
        self.l7.setObjectName(u"l7")

        self.gridLayout.addWidget(self.l7, 2, 0, 1, 1)

        self.sceneSize = QLabel(self.centralwidget)
        self.sceneSize.setObjectName(u"sceneSize")

        self.gridLayout.addWidget(self.sceneSize, 4, 0, 1, 1)

        self.l9 = QLabel(self.centralwidget)
        self.l9.setObjectName(u"l9")

        self.gridLayout.addWidget(self.l9, 2, 3, 1, 1)

        self.l11 = QLabel(self.centralwidget)
        self.l11.setObjectName(u"l11")

        self.gridLayout.addWidget(self.l11, 3, 2, 1, 1)

        self.l8 = QLabel(self.centralwidget)
        self.l8.setObjectName(u"l8")

        self.gridLayout.addWidget(self.l8, 2, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.scenePos = QLabel(self.centralwidget)
        self.scenePos.setObjectName(u"scenePos")

        self.gridLayout.addWidget(self.scenePos, 0, 1, 1, 1)

        self.dzonePos = QLabel(self.centralwidget)
        self.dzonePos.setObjectName(u"dzonePos")

        self.gridLayout.addWidget(self.dzonePos, 0, 2, 1, 1)

        self.puckPos = QLabel(self.centralwidget)
        self.puckPos.setObjectName(u"puckPos")

        self.gridLayout.addWidget(self.puckPos, 0, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1030, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.viewSceneRect.setText(QCoreApplication.translate("MainWindow", u"viewSceneRect", None))
        self.dzoneSize.setText(QCoreApplication.translate("MainWindow", u"dzoneSize", None))
        self.l14.setText("")
        self.viewSize.setText(QCoreApplication.translate("MainWindow", u"viewSize", None))
        self.viewPos.setText(QCoreApplication.translate("MainWindow", u"viewPos", None))
        self.l5.setText("")
        self.l4.setText("")
        self.l10.setText("")
        self.l12.setText("")
        self.l7.setText("")
        self.sceneSize.setText(QCoreApplication.translate("MainWindow", u"sceneSize", None))
        self.l9.setText("")
        self.l11.setText("")
        self.l8.setText("")
        self.label.setText("")
        self.scenePos.setText(QCoreApplication.translate("MainWindow", u"scenePos", None))
        self.dzonePos.setText(QCoreApplication.translate("MainWindow", u"dZonePos", None))
        self.puckPos.setText(QCoreApplication.translate("MainWindow", u"puckPos", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

