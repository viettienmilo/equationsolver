# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\OneDrive\Documents\Python Programming\EquationSolver\mainui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mWin(object):
    def setupUi(self, mWin):
        mWin.setObjectName("mWin")
        mWin.resize(731, 475)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mWin.sizePolicy().hasHeightForWidth())
        mWin.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(mWin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.lblNr = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblNr.setFont(font)
        self.lblNr.setObjectName("lblNr")
        self.gridLayout_4.addWidget(self.lblNr, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1)
        self.lblNrSteps = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblNrSteps.setFont(font)
        self.lblNrSteps.setObjectName("lblNrSteps")
        self.gridLayout_4.addWidget(self.lblNrSteps, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)
        self.lblSe = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblSe.setFont(font)
        self.lblSe.setObjectName("lblSe")
        self.gridLayout_5.addWidget(self.lblSe, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 1, 0, 1, 1)
        self.lblSeSteps = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblSeSteps.setFont(font)
        self.lblSeSteps.setObjectName("lblSeSteps")
        self.gridLayout_5.addWidget(self.lblSeSteps, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 4, 0, 1, 1)
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy)
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnSolve = QtWidgets.QPushButton(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSolve.sizePolicy().hasHeightForWidth())
        self.btnSolve.setSizePolicy(sizePolicy)
        self.btnSolve.setObjectName("btnSolve")
        self.verticalLayout.addWidget(self.btnSolve)
        self.gridLayout.addWidget(self.frame2, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.lblBi = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblBi.setFont(font)
        self.lblBi.setObjectName("lblBi")
        self.gridLayout_3.addWidget(self.lblBi, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.lblBiSteps = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lblBiSteps.setFont(font)
        self.lblBiSteps.setObjectName("lblBiSteps")
        self.gridLayout_3.addWidget(self.lblBiSteps, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setObjectName("frame1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame1)
        self.gridLayout_2.setContentsMargins(-1, -1, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label1 = QtWidgets.QLabel(self.frame1)
        self.label1.setObjectName("label1")
        self.gridLayout_2.addWidget(self.label1, 0, 0, 1, 1)
        self.txtExpr = QtWidgets.QLineEdit(self.frame1)
        self.txtExpr.setObjectName("txtExpr")
        self.gridLayout_2.addWidget(self.txtExpr, 0, 1, 1, 1)
        self.label2 = QtWidgets.QLabel(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label2.sizePolicy().hasHeightForWidth())
        self.label2.setSizePolicy(sizePolicy)
        self.label2.setObjectName("label2")
        self.gridLayout_2.addWidget(self.label2, 1, 1, 1, 1)
        self.label3 = QtWidgets.QLabel(self.frame1)
        self.label3.setObjectName("label3")
        self.gridLayout_2.addWidget(self.label3, 2, 0, 1, 1)
        self.dsbStart = QtWidgets.QDoubleSpinBox(self.frame1)
        self.dsbStart.setMinimum(-99.99)
        self.dsbStart.setProperty("value", -2.0)
        self.dsbStart.setObjectName("dsbStart")
        self.gridLayout_2.addWidget(self.dsbStart, 2, 1, 1, 1)
        self.label4 = QtWidgets.QLabel(self.frame1)
        self.label4.setObjectName("label4")
        self.gridLayout_2.addWidget(self.label4, 3, 0, 1, 1)
        self.dsbStop = QtWidgets.QDoubleSpinBox(self.frame1)
        self.dsbStop.setMinimum(-99.99)
        self.dsbStop.setProperty("value", 2.0)
        self.dsbStop.setObjectName("dsbStop")
        self.gridLayout_2.addWidget(self.dsbStop, 3, 1, 1, 1)
        self.label5 = QtWidgets.QLabel(self.frame1)
        self.label5.setObjectName("label5")
        self.gridLayout_2.addWidget(self.label5, 4, 0, 1, 1)
        self.sbPrecision = QtWidgets.QSpinBox(self.frame1)
        self.sbPrecision.setProperty("value", 3)
        self.sbPrecision.setObjectName("sbPrecision")
        self.gridLayout_2.addWidget(self.sbPrecision, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.frame1, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.frame3 = QtWidgets.QFrame(self.centralwidget)
        self.frame3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3.setObjectName("frame3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.wgPlot = QtWidgets.QWidget(self.frame3)
        self.wgPlot.setObjectName("wgPlot")
        self.gridLayout_6.addWidget(self.wgPlot, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame3, 0, 1, 6, 1)
        mWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(mWin)
        QtCore.QMetaObject.connectSlotsByName(mWin)

    def retranslateUi(self, mWin):
        _translate = QtCore.QCoreApplication.translate
        mWin.setWindowTitle(_translate("mWin", "Equation Solver - Univariate"))
        self.groupBox_2.setTitle(_translate("mWin", "Newton-Raphson solution"))
        self.label_5.setText(_translate("mWin", "Solution"))
        self.lblNr.setText(_translate("mWin", "--"))
        self.label_7.setText(_translate("mWin", "Steps"))
        self.lblNrSteps.setText(_translate("mWin", "--"))
        self.groupBox_3.setTitle(_translate("mWin", "Secat solution"))
        self.label_9.setText(_translate("mWin", "Solution"))
        self.lblSe.setText(_translate("mWin", "--"))
        self.label_11.setText(_translate("mWin", "Steps"))
        self.lblSeSteps.setText(_translate("mWin", "--"))
        self.btnSolve.setText(_translate("mWin", "Solve"))
        self.groupBox.setTitle(_translate("mWin", "Bisection solution"))
        self.label.setText(_translate("mWin", "Solution"))
        self.lblBi.setText(_translate("mWin", "--"))
        self.label_3.setText(_translate("mWin", "Steps"))
        self.lblBiSteps.setText(_translate("mWin", "--"))
        self.label1.setText(_translate("mWin", "Expression:"))
        self.txtExpr.setText(_translate("mWin", "x**3+x-5"))
        self.label2.setText(_translate("mWin", "(Example: x**3 + x - 1)"))
        self.label3.setText(_translate("mWin", "Start at:"))
        self.label4.setText(_translate("mWin", "Stop at:"))
        self.label5.setText(_translate("mWin", "Precision:"))
