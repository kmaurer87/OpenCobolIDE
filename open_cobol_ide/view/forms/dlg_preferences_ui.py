# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/Dev/OpenCobolIDE/forms/dlg_preferences.ui'
#
# Created: Sat Aug 30 19:39:04 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from pyqode.core.qt import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(714, 630)
        icon = QtGui.QIcon.fromTheme("preferences-system")
        Dialog.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QGridLayout(self.widget)
        self.widget_2.setSpacing(0)
        self.widget_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Reset|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabEditor = QtWidgets.QWidget()
        self.tabEditor.setObjectName("tabEditor")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabEditor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tabEditor)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName("formLayout_4")
        self.checkBoxViewLineNumber = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBoxViewLineNumber.setChecked(True)
        self.checkBoxViewLineNumber.setObjectName("checkBoxViewLineNumber")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBoxViewLineNumber)
        self.checkBoxHighlightCurrentLine = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBoxHighlightCurrentLine.setChecked(True)
        self.checkBoxHighlightCurrentLine.setObjectName("checkBoxHighlightCurrentLine")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBoxHighlightCurrentLine)
        self.checkBoxHighlightWhitespaces = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBoxHighlightWhitespaces.setChecked(True)
        self.checkBoxHighlightWhitespaces.setObjectName("checkBoxHighlightWhitespaces")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkBoxHighlightWhitespaces)
        self.checkBoxShowErrors = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBoxShowErrors.setObjectName("checkBoxShowErrors")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.checkBoxShowErrors)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tabEditor)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBoxEditorTabLen = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBoxEditorTabLen.setMaximum(99)
        self.spinBoxEditorTabLen.setProperty("value", 4)
        self.spinBoxEditorTabLen.setObjectName("spinBoxEditorTabLen")
        self.horizontalLayout.addWidget(self.spinBoxEditorTabLen)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.checkBoxEditorAutoIndent = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBoxEditorAutoIndent.setChecked(True)
        self.checkBoxEditorAutoIndent.setObjectName("checkBoxEditorAutoIndent")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBoxEditorAutoIndent)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tabEditor)
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout_5 = QtWidgets.QFormLayout(self.groupBox_4)
        self.formLayout_5.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setObjectName("formLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spinBoxEditorCCTriggerLen = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBoxEditorCCTriggerLen.setProperty("value", 1)
        self.spinBoxEditorCCTriggerLen.setObjectName("spinBoxEditorCCTriggerLen")
        self.horizontalLayout_2.addWidget(self.spinBoxEditorCCTriggerLen)
        self.formLayout_5.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout.addWidget(self.groupBox_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ide-icons/rc/cobol-mimetype.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabEditor, icon, "")
        self.tabStyle = QtWidgets.QWidget()
        self.tabStyle.setObjectName("tabStyle")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabStyle)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tabStyle)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.radioButtonColorWhite = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButtonColorWhite.setChecked(True)
        self.radioButtonColorWhite.setObjectName("radioButtonColorWhite")
        self.horizontalLayout_3.addWidget(self.radioButtonColorWhite)
        self.radioButtonColorDark = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButtonColorDark.setObjectName("radioButtonColorDark")
        self.horizontalLayout_3.addWidget(self.radioButtonColorDark)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.layoutIconTheme = QtWidgets.QFormLayout()
        self.layoutIconTheme.setContentsMargins(-1, 0, -1, -1)
        self.layoutIconTheme.setObjectName("layoutIconTheme")
        self.lblIconTheme = QtWidgets.QLabel(self.groupBox_5)
        self.lblIconTheme.setObjectName("lblIconTheme")
        self.layoutIconTheme.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblIconTheme)
        self.comboBoxIconTheme = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBoxIconTheme.setObjectName("comboBoxIconTheme")
        self.layoutIconTheme.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxIconTheme)
        self.verticalLayout_2.addLayout(self.layoutIconTheme)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tabStyle)
        self.groupBox_6.setObjectName("groupBox_6")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_6)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.fontComboBox = QtWidgets.QFontComboBox(self.groupBox_6)
        self.fontComboBox.setFontFilters(QtWidgets.QFontComboBox.MonospacedFonts)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.fontComboBox.setCurrentFont(font)
        self.fontComboBox.setObjectName("fontComboBox")
        self.horizontalLayout_4.addWidget(self.fontComboBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.spinBoxFontSize = QtWidgets.QSpinBox(self.groupBox_6)
        self.spinBoxFontSize.setProperty("value", 10)
        self.spinBoxFontSize.setObjectName("spinBoxFontSize")
        self.horizontalLayout_5.addWidget(self.spinBoxFontSize)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tabStyle)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.listWidgetColorSchemes = QtWidgets.QListWidget(self.groupBox_7)
        self.listWidgetColorSchemes.setObjectName("listWidgetColorSchemes")
        self.gridLayout_4.addWidget(self.listWidgetColorSchemes, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_7)
        icon = QtGui.QIcon.fromTheme("applications-graphics")
        self.tabWidget.addTab(self.tabStyle, icon, "")
        self.tabBuildAndRun = QtWidgets.QWidget()
        self.tabBuildAndRun.setObjectName("tabBuildAndRun")
        self.formLayout_6 = QtWidgets.QFormLayout(self.tabBuildAndRun)
        self.formLayout_6.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setObjectName("formLayout_6")
        self.checkBoxRunExtTerm = QtWidgets.QCheckBox(self.tabBuildAndRun)
        self.checkBoxRunExtTerm.setObjectName("checkBoxRunExtTerm")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkBoxRunExtTerm)
        self.lineEditRunTerm = QtWidgets.QLineEdit(self.tabBuildAndRun)
        self.lineEditRunTerm.setObjectName("lineEditRunTerm")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditRunTerm)
        self.checkBoxCustomPath = QtWidgets.QCheckBox(self.tabBuildAndRun)
        self.checkBoxCustomPath.setObjectName("checkBoxCustomPath")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.checkBoxCustomPath)
        self.lineEditCompilerPath = QtWidgets.QLineEdit(self.tabBuildAndRun)
        self.lineEditCompilerPath.setObjectName("lineEditCompilerPath")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditCompilerPath)
        icon = QtGui.QIcon.fromTheme("exec")
        self.tabWidget.addTab(self.tabBuildAndRun, icon, "")
        self.tab_Cobol = QtWidgets.QWidget()
        self.tab_Cobol.setObjectName("tab_Cobol")
        self.formLayout_7 = QtWidgets.QFormLayout(self.tab_Cobol)
        self.formLayout_7.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_7.setObjectName("formLayout_7")
        self.label_8 = QtWidgets.QLabel(self.tab_Cobol)
        self.label_8.setObjectName("label_8")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comboBoxStandard = QtWidgets.QComboBox(self.tab_Cobol)
        self.comboBoxStandard.setObjectName("comboBoxStandard")
        self.comboBoxStandard.addItem("")
        self.comboBoxStandard.addItem("")
        self.comboBoxStandard.addItem("")
        self.comboBoxStandard.addItem("")
        self.comboBoxStandard.addItem("")
        self.comboBoxStandard.addItem("")
        self.comboBoxStandard.addItem("")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBoxStandard)
        self.label_7 = QtWidgets.QLabel(self.tab_Cobol)
        self.label_7.setObjectName("label_7")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEditCommentIndicator = QtWidgets.QLineEdit(self.tab_Cobol)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.lineEditCommentIndicator.setFont(font)
        self.lineEditCommentIndicator.setObjectName("lineEditCommentIndicator")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditCommentIndicator)
        self.checkBoxFreeFormat = QtWidgets.QCheckBox(self.tab_Cobol)
        self.checkBoxFreeFormat.setObjectName("checkBoxFreeFormat")
        self.formLayout_7.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.checkBoxFreeFormat)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ide-icons/rc/silex-64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_Cobol, icon1, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Preferences"))
        self.widget.setAccessibleName(_translate("Dialog", "widget", "widget"))
        self.groupBox_3.setTitle(_translate("Dialog", "View"))
        self.checkBoxViewLineNumber.setToolTip(_translate("Dialog", "Show/Hide line numbers"))
        self.checkBoxViewLineNumber.setStatusTip(_translate("Dialog", "Show/Hide line numbers"))
        self.checkBoxViewLineNumber.setText(_translate("Dialog", "Display line numbers"))
        self.checkBoxHighlightCurrentLine.setToolTip(_translate("Dialog", "Highlight caret line"))
        self.checkBoxHighlightCurrentLine.setStatusTip(_translate("Dialog", "Highlight caret line"))
        self.checkBoxHighlightCurrentLine.setText(_translate("Dialog", "Highlight current line"))
        self.checkBoxHighlightWhitespaces.setToolTip(_translate("Dialog", "Show visual whitespaces"))
        self.checkBoxHighlightWhitespaces.setStatusTip(_translate("Dialog", "Show visual whitespaces"))
        self.checkBoxHighlightWhitespaces.setText(_translate("Dialog", "Highlight whitespaces"))
        self.checkBoxShowErrors.setToolTip(_translate("Dialog", "Compile your code on the fly and show errors while you\'re typing"))
        self.checkBoxShowErrors.setText(_translate("Dialog", "Show errors"))
        self.groupBox_2.setTitle(_translate("Dialog", "Indentation"))
        self.spinBoxEditorTabLen.setToolTip(_translate("Dialog", "Tab length (number of spaces)"))
        self.spinBoxEditorTabLen.setStatusTip(_translate("Dialog", "Tab length (number of spaces)"))
        self.checkBoxEditorAutoIndent.setToolTip(_translate("Dialog", "Enable/Disable automatic indentation"))
        self.checkBoxEditorAutoIndent.setStatusTip(_translate("Dialog", "Enable/Disable automatic indentation"))
        self.checkBoxEditorAutoIndent.setText(_translate("Dialog", "Enable automatic indentation"))
        self.label.setText(_translate("Dialog", "Tab width (number of spaces):"))
        self.groupBox_4.setTitle(_translate("Dialog", "Code completion"))
        self.spinBoxEditorCCTriggerLen.setToolTip(_translate("Dialog", "Number of characters needed to trigger auto completion"))
        self.spinBoxEditorCCTriggerLen.setStatusTip(_translate("Dialog", "Number of characters needed to trigger auto completion"))
        self.label_2.setText(_translate("Dialog", "Trigger length:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEditor), _translate("Dialog", "Editor"))
        self.groupBox_5.setTitle(_translate("Dialog", "Global style"))
        self.radioButtonColorWhite.setToolTip(_translate("Dialog", "Use native style"))
        self.radioButtonColorWhite.setStatusTip(_translate("Dialog", "Use native style"))
        self.radioButtonColorWhite.setText(_translate("Dialog", "Native"))
        self.radioButtonColorDark.setToolTip(_translate("Dialog", "Use a global dark style (using QDarkStyleSheet)"))
        self.radioButtonColorDark.setStatusTip(_translate("Dialog", "Use a global dark style (using QDarkStyleSheet)"))
        self.radioButtonColorDark.setText(_translate("Dialog", "Dark"))
        self.lblIconTheme.setText(_translate("Dialog", "Icon theme"))
        self.groupBox_6.setTitle(_translate("Dialog", "Font"))
        self.label_3.setText(_translate("Dialog", "Editor font"))
        self.label_4.setText(_translate("Dialog", "Font size:"))
        self.fontComboBox.setToolTip(_translate("Dialog", "Change editor font"))
        self.fontComboBox.setStatusTip(_translate("Dialog", "Change editor font"))
        self.spinBoxFontSize.setToolTip(_translate("Dialog", "Change editor font size"))
        self.spinBoxFontSize.setStatusTip(_translate("Dialog", "Change editor font size"))
        self.groupBox_7.setTitle(_translate("Dialog", "Color scheme"))
        self.listWidgetColorSchemes.setToolTip(_translate("Dialog", "Pygments color schemes."))
        self.listWidgetColorSchemes.setStatusTip(_translate("Dialog", "Pygments color schemes."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStyle), _translate("Dialog", "Style"))
        self.checkBoxRunExtTerm.setToolTip(_translate("Dialog", "Enable/Disable running program in an external terminal"))
        self.checkBoxRunExtTerm.setStatusTip(_translate("Dialog", "Enable/Disable running program in an external terminal"))
        self.checkBoxRunExtTerm.setText(_translate("Dialog", "Run in external terminal"))
        self.lineEditRunTerm.setToolTip(_translate("Dialog", "External terminal command (filename is appended at the end of the command)"))
        self.lineEditRunTerm.setStatusTip(_translate("Dialog", "External terminal command"))
        self.checkBoxCustomPath.setToolTip(_translate("Dialog", "Enable/Disable custom compiler path"))
        self.checkBoxCustomPath.setStatusTip(_translate("Dialog", "Enable/Disable custom compiler path"))
        self.checkBoxCustomPath.setText(_translate("Dialog", "Custom compiler path"))
        self.lineEditCompilerPath.setToolTip(_translate("Dialog", "Path to the compiler (should not include the executable name, only the directory path)"))
        self.lineEditCompilerPath.setStatusTip(_translate("Dialog", "Path to the compiler (should not include the executable name, only the directory path)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabBuildAndRun), _translate("Dialog", "Build && Run"))
        self.label_8.setText(_translate("Dialog", "Standard"))
        self.comboBoxStandard.setItemText(0, _translate("Dialog", "default"))
        self.comboBoxStandard.setItemText(1, _translate("Dialog", "cobol2002"))
        self.comboBoxStandard.setItemText(2, _translate("Dialog", "cobol85"))
        self.comboBoxStandard.setItemText(3, _translate("Dialog", "ibm"))
        self.comboBoxStandard.setItemText(4, _translate("Dialog", "mvs"))
        self.comboBoxStandard.setItemText(5, _translate("Dialog", "bs2000"))
        self.comboBoxStandard.setItemText(6, _translate("Dialog", "mf"))
        self.label_7.setText(_translate("Dialog", "Comment indicator:"))
        self.lineEditCommentIndicator.setText(_translate("Dialog", "*>"))
        self.checkBoxFreeFormat.setToolTip(_translate("Dialog", "Code and compile with free format support"))
        self.checkBoxFreeFormat.setText(_translate("Dialog", "Free format"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Cobol), _translate("Dialog", "Cobol"))

from . import ide_rc