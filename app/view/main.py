# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 646)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.sa_inner = QtWidgets.QScrollArea(self.groupBox)
        self.sa_inner.setWidgetResizable(True)
        self.sa_inner.setObjectName("sa_inner")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 308, 256))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.l_inner = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.l_inner.setText("")
        self.l_inner.setObjectName("l_inner")
        self.gridLayout_6.addWidget(self.l_inner, 0, 0, 1, 1)
        self.sa_inner.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.sa_inner, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.sa_result = QtWidgets.QScrollArea(self.groupBox_3)
        self.sa_result.setWidgetResizable(True)
        self.sa_result.setObjectName("sa_result")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 308, 256))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.l_result = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.l_result.setText("")
        self.l_result.setObjectName("l_result")
        self.gridLayout_8.addWidget(self.l_result, 0, 0, 1, 1)
        self.sa_result.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.addWidget(self.sa_result, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.sa_outer = QtWidgets.QScrollArea(self.groupBox_2)
        self.sa_outer.setWidgetResizable(True)
        self.sa_outer.setObjectName("sa_outer")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 308, 256))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.l_outer = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.l_outer.setText("")
        self.l_outer.setObjectName("l_outer")
        self.gridLayout_7.addWidget(self.l_outer, 0, 0, 1, 1)
        self.sa_outer.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.addWidget(self.sa_outer, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pb_save = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_save.sizePolicy().hasHeightForWidth())
        self.pb_save.setSizePolicy(sizePolicy)
        self.pb_save.setObjectName("pb_save")
        self.gridLayout_2.addWidget(self.pb_save, 6, 0, 1, 1)
        self.cb_dark = QtWidgets.QCheckBox(self.groupBox_4)
        self.cb_dark.setObjectName("cb_dark")
        self.gridLayout_2.addWidget(self.cb_dark, 0, 0, 1, 1)
        self.pb_inner = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_inner.sizePolicy().hasHeightForWidth())
        self.pb_inner.setSizePolicy(sizePolicy)
        self.pb_inner.setObjectName("pb_inner")
        self.gridLayout_2.addWidget(self.pb_inner, 2, 0, 1, 1)
        self.pb_outer = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_outer.sizePolicy().hasHeightForWidth())
        self.pb_outer.setSizePolicy(sizePolicy)
        self.pb_outer.setObjectName("pb_outer")
        self.gridLayout_2.addWidget(self.pb_outer, 3, 0, 1, 1)
        self.pb_build = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_build.sizePolicy().hasHeightForWidth())
        self.pb_build.setSizePolicy(sizePolicy)
        self.pb_build.setObjectName("pb_build")
        self.gridLayout_2.addWidget(self.pb_build, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 4, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox_4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.l_alipay = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_alipay.sizePolicy().hasHeightForWidth())
        self.l_alipay.setSizePolicy(sizePolicy)
        self.l_alipay.setMinimumSize(QtCore.QSize(192, 192))
        self.l_alipay.setMaximumSize(QtCore.QSize(192, 192))
        self.l_alipay.setText("")
        self.l_alipay.setObjectName("l_alipay")
        self.gridLayout_9.addWidget(self.l_alipay, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setObjectName("label_3")
        self.gridLayout_9.addWidget(self.label_3, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setObjectName("label_2")
        self.gridLayout_9.addWidget(self.label_2, 2, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.groupBox_5)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_9.addWidget(self.line_4, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setObjectName("label")
        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.groupBox_5)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_9.addWidget(self.line_3, 4, 0, 1, 1)
        self.l_wechat = QtWidgets.QLabel(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_wechat.sizePolicy().hasHeightForWidth())
        self.l_wechat.setSizePolicy(sizePolicy)
        self.l_wechat.setMinimumSize(QtCore.QSize(192, 192))
        self.l_wechat.setMaximumSize(QtCore.QSize(192, 192))
        self.l_wechat.setText("")
        self.l_wechat.setObjectName("l_wechat")
        self.gridLayout_9.addWidget(self.l_wechat, 6, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_5, 0, 2, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "幻影坦克生成器"))
        self.groupBox.setTitle(_translate("MainWindow", "里图"))
        self.groupBox_3.setTitle(_translate("MainWindow", "结果图"))
        self.groupBox_2.setTitle(_translate("MainWindow", "表图"))
        self.groupBox_4.setTitle(_translate("MainWindow", "控制面板"))
        self.pb_save.setText(_translate("MainWindow", "保存结果图"))
        self.cb_dark.setText(_translate("MainWindow", "结果图预览暗色背景"))
        self.pb_inner.setText(_translate("MainWindow", "设置里图"))
        self.pb_outer.setText(_translate("MainWindow", "设置表图"))
        self.pb_build.setText(_translate("MainWindow", "造坦克"))
        self.groupBox_5.setTitle(_translate("MainWindow", "作者信息"))
        self.label_3.setText(_translate("MainWindow", "微信："))
        self.label_2.setText(_translate("MainWindow", "支付宝："))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>本软件由HsOjo制作。</p><p>详情请查看：<a href=\"http://blog.hsojo.com/2018/02/08/PhantomTank/\"><span style=\" text-decoration: underline; color:#0000ff;\">右键点击复制链接</span></a></p><p>如果对你有所帮助，请...你懂的。</p></body></html>"))

