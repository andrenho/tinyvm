# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pages.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Pages(object):
    def setupUi(self, Pages):
        Pages.setObjectName("Pages")
        Pages.resize(604, 612)
        Pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(Pages)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(Pages)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Pages)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 2, 1, 1)
        self.page_dir = QtWidgets.QLineEdit(Pages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_dir.sizePolicy().hasHeightForWidth())
        self.page_dir.setSizePolicy(sizePolicy)
        self.page_dir.setMinimumSize(QtCore.QSize(80, 0))
        self.page_dir.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.page_dir.setObjectName("page_dir")
        self.gridLayout_4.addWidget(self.page_dir, 0, 3, 1, 1)
        self.vm_active = QtWidgets.QCheckBox(Pages)
        self.vm_active.setObjectName("vm_active")
        self.gridLayout_4.addWidget(self.vm_active, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        self.vmem = QtWidgets.QLCDNumber(Pages)
        self.vmem.setMinimumSize(QtCore.QSize(0, 30))
        self.vmem.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vmem.setSmallDecimalPoint(False)
        self.vmem.setDigitCount(8)
        self.vmem.setMode(QtWidgets.QLCDNumber.Hex)
        self.vmem.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.vmem.setProperty("intValue", 0)
        self.vmem.setObjectName("vmem")
        self.gridLayout_4.addWidget(self.vmem, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.line = QtWidgets.QFrame(Pages)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Pages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ph_memory = QtWidgets.QTableView(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.ph_memory.setFont(font)
        self.ph_memory.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ph_memory.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ph_memory.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.ph_memory.setGridStyle(QtCore.Qt.SolidLine)
        self.ph_memory.setObjectName("ph_memory")
        self.horizontalLayout_2.addWidget(self.ph_memory)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.unmapped_2 = QtWidgets.QLabel(Pages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unmapped_2.sizePolicy().hasHeightForWidth())
        self.unmapped_2.setSizePolicy(sizePolicy)
        self.unmapped_2.setMinimumSize(QtCore.QSize(10, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.unmapped_2.setPalette(palette)
        self.unmapped_2.setAutoFillBackground(True)
        self.unmapped_2.setFrameShape(QtWidgets.QFrame.Box)
        self.unmapped_2.setText("")
        self.unmapped_2.setObjectName("unmapped_2")
        self.gridLayout_3.addWidget(self.unmapped_2, 0, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(Pages)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 4, 1, 1, 1)
        self.memory_map = QtWidgets.QLabel(Pages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.memory_map.sizePolicy().hasHeightForWidth())
        self.memory_map.setSizePolicy(sizePolicy)
        self.memory_map.setMinimumSize(QtCore.QSize(10, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.memory_map.setPalette(palette)
        self.memory_map.setAutoFillBackground(True)
        self.memory_map.setFrameShape(QtWidgets.QFrame.Box)
        self.memory_map.setText("")
        self.memory_map.setObjectName("memory_map")
        self.gridLayout_3.addWidget(self.memory_map, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(Pages)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 1, 1, 1)
        self.user = QtWidgets.QLabel(Pages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user.sizePolicy().hasHeightForWidth())
        self.user.setSizePolicy(sizePolicy)
        self.user.setMinimumSize(QtCore.QSize(10, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.user.setPalette(palette)
        self.user.setAutoFillBackground(True)
        self.user.setFrameShape(QtWidgets.QFrame.Box)
        self.user.setText("")
        self.user.setObjectName("user")
        self.gridLayout_3.addWidget(self.user, 1, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(Pages)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(Pages)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(Pages)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 2, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(Pages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QtCore.QSize(10, 0))
        self.label_18.setAutoFillBackground(True)
        self.label_18.setFrameShape(QtWidgets.QFrame.Box)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 4, 0, 1, 1)
        self.supervisor = QtWidgets.QLabel(Pages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.supervisor.sizePolicy().hasHeightForWidth())
        self.supervisor.setSizePolicy(sizePolicy)
        self.supervisor.setMinimumSize(QtCore.QSize(10, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.supervisor.setPalette(palette)
        self.supervisor.setAutoFillBackground(True)
        self.supervisor.setFrameShape(QtWidgets.QFrame.Box)
        self.supervisor.setText("")
        self.supervisor.setObjectName("supervisor")
        self.gridLayout_3.addWidget(self.supervisor, 2, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(Pages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMinimumSize(QtCore.QSize(10, 0))
        self.label_20.setAutoFillBackground(True)
        self.label_20.setFrameShape(QtWidgets.QFrame.Box)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 5, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(Pages)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 5, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 1, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(Pages)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 1, 1, 1)
        self.page_table = QtWidgets.QLabel(Pages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_table.sizePolicy().hasHeightForWidth())
        self.page_table.setSizePolicy(sizePolicy)
        self.page_table.setMinimumSize(QtCore.QSize(10, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.page_table.setPalette(palette)
        self.page_table.setAutoFillBackground(True)
        self.page_table.setFrameShape(QtWidgets.QFrame.Box)
        self.page_table.setText("")
        self.page_table.setObjectName("page_table")
        self.gridLayout_2.addWidget(self.page_table, 3, 0, 1, 1)
        self.unmapped = QtWidgets.QLabel(Pages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unmapped.sizePolicy().hasHeightForWidth())
        self.unmapped.setSizePolicy(sizePolicy)
        self.unmapped.setMinimumSize(QtCore.QSize(10, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.unmapped.setPalette(palette)
        self.unmapped.setAutoFillBackground(True)
        self.unmapped.setFrameShape(QtWidgets.QFrame.Box)
        self.unmapped.setText("")
        self.unmapped.setObjectName("unmapped")
        self.gridLayout_2.addWidget(self.unmapped, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(Pages)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Pages)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 1, 1, 1)
        self.page_directory = QtWidgets.QLabel(Pages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_directory.sizePolicy().hasHeightForWidth())
        self.page_directory.setSizePolicy(sizePolicy)
        self.page_directory.setMinimumSize(QtCore.QSize(10, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.page_directory.setPalette(palette)
        self.page_directory.setAutoFillBackground(True)
        self.page_directory.setFrameShape(QtWidgets.QFrame.Box)
        self.page_directory.setText("")
        self.page_directory.setObjectName("page_directory")
        self.gridLayout_2.addWidget(self.page_directory, 2, 0, 1, 1)
        self.mapped = QtWidgets.QLabel(Pages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapped.sizePolicy().hasHeightForWidth())
        self.mapped.setSizePolicy(sizePolicy)
        self.mapped.setMinimumSize(QtCore.QSize(10, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.mapped.setPalette(palette)
        self.mapped.setAutoFillBackground(True)
        self.mapped.setFrameShape(QtWidgets.QFrame.Box)
        self.mapped.setText("")
        self.mapped.setObjectName("mapped")
        self.gridLayout_2.addWidget(self.mapped, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Pages)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem1, 4, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Pages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.vmem_stack = QtWidgets.QStackedWidget(self.groupBox_2)
        self.vmem_stack.setObjectName("vmem_stack")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.vmem_stack.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.v_memory = QtWidgets.QTableView(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.v_memory.setFont(font)
        self.v_memory.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.v_memory.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.v_memory.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.v_memory.setGridStyle(QtCore.Qt.SolidLine)
        self.v_memory.setObjectName("v_memory")
        self.horizontalLayout_4.addWidget(self.v_memory)
        self.vmem_stack.addWidget(self.page_2)
        self.horizontalLayout_3.addWidget(self.vmem_stack)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Pages)
        self.vmem_stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Pages)

    def retranslateUi(self, Pages):
        _translate = QtCore.QCoreApplication.translate
        Pages.setWindowTitle(_translate("Pages", "Frame"))
        self.label.setText(_translate("Pages", "VMEM register"))
        self.label_4.setText(_translate("Pages", "Page directory page number"))
        self.vm_active.setText(_translate("Pages", "Virtual Memory enabled"))
        self.groupBox.setTitle(_translate("Pages", "Physical Memory"))
        self.label_19.setText(_translate("Pages", "Read only"))
        self.label_11.setText(_translate("Pages", "Unmapped"))
        self.label_17.setText(_translate("Pages", "Memory mapped"))
        self.label_13.setText(_translate("Pages", "User"))
        self.label_15.setText(_translate("Pages", "Supervisor"))
        self.label_18.setText(_translate("Pages", "r"))
        self.label_20.setText(_translate("Pages", "x"))
        self.label_21.setText(_translate("Pages", "Executable"))
        self.label_7.setText(_translate("Pages", "Page Directory"))
        self.label_8.setText(_translate("Pages", "Page Table"))
        self.label_5.setText(_translate("Pages", "Mapped"))
        self.label_3.setText(_translate("Pages", "Unmapped"))
        self.groupBox_2.setTitle(_translate("Pages", "Virtual Memory"))
        self.label_2.setText(_translate("Pages", "Virtual Memory is disabled."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pages = QtWidgets.QFrame()
    ui = Ui_Pages()
    ui.setupUi(Pages)
    Pages.show()
    sys.exit(app.exec_())

