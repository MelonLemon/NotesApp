# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import icons_svg_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(406, 548)
        MainWindow.setMinimumSize(QSize(350, 270))
        MainWindow.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"color: rgb(248, 248, 248);\n"
"\n"
"")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton#btn_delete, #btn_search, #btn_back,\n"
" #btn_saveChanges, #btn_edit, #btn_back_2, #btn_save {\n"
"   background-color: rgb(58, 58, 58);\n"
"   border: 0px;\n"
"   border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#btn_delete:hover {\n"
"	border: 1px solid rgb(255, 70, 95);\n"
"}\n"
"QPushButton#btn_delete:pressed {\n"
"   background-color: rgb(255, 70, 95);\n"
"   border: 0px;\n"
"   border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#btn_add {\n"
"background-color: rgb(48, 48, 48);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton#btn_add:hover, #btn_back:hover, \n"
"#btn_edit:hover, #btn_back_2:hover, #btn_save:hover {\n"
"	border: 3px solid rgb(33, 33, 33);\n"
"}\n"
"QPushButton#btn_add:pressed, #btn_back:hover, \n"
"#btn_edit:hover, #btn_back_2:hover, #btn_save:hover {\n"
"   background-color: rgb(33, 33, 33);\n"
"}\n"
"\n"
"QTextEdit#textEdit_bodyNote, #lineEdit_Title {\n"
"border: 0xp;\n"
"}\n"
"\n"
"QPushButton#btn_saveChanges:hover {\n"
"	border: 1px solid rgb(231, 237, 155);\n"
"}\n"
"QPushButto"
                        "n#btn_saveChanges:pressed {\n"
"   background-color: rgb(207, 212, 144);\n"
"   border: 1px solid rgb(207, 212, 144);\n"
"}\n"
"\n"
"QTableView {\n"
"	background-color: rgb(37, 37, 37);\n"
"    border: 0xp;\n"
"}\n"
"QScrollArea {\n"
"	background-color: rgb(37, 37, 37);\n"
"    border: 0xp;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"     background: rgb(37, 37, 37);\n"
"     width: 20px;\n"
"     margin: 19px 0 19px 0;\n"
"     border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color:  rgb(48, 48, 48);\n"
"    min-height: 30px;\n"
"    border-radius: 5px;\n"
"  }\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"      background-color: rgb(255,255,222);\n"
"  }\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"      background-color: rgb(33, 33, 33);\n"
" }\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"      height: 0px;\n"
" }\n"
"\n"
" QScrollBar::add-line:vertical {\n"
"       height: 0px;\n"
" }\n"
"\n"
"\n"
"\n"
"/* RESET ARROW  vvvvvvvvvvvvvvvvvvvvvvvv"
                        "vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv       */\n"
"            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"                background: none;\n"
"            }\n"
"            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"                background: none;\n"
"            }\n"
"/* ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^       *")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.allNotesPage = QWidget()
        self.allNotesPage.setObjectName(u"allNotesPage")
        self.verticalLayout = QVBoxLayout(self.allNotesPage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.header_allNotes = QFrame(self.allNotesPage)
        self.header_allNotes.setObjectName(u"header_allNotes")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_allNotes.sizePolicy().hasHeightForWidth())
        self.header_allNotes.setSizePolicy(sizePolicy)
        self.header_allNotes.setMinimumSize(QSize(0, 45))
        self.header_allNotes.setMaximumSize(QSize(16777215, 45))
        self.header_allNotes.setFrameShape(QFrame.StyledPanel)
        self.header_allNotes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_allNotes)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_Notes = QLabel(self.header_allNotes)
        self.label_Notes.setObjectName(u"label_Notes")
        font = QFont()
        font.setFamilies([u"Segoe UI Symbol"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.label_Notes.setFont(font)
        self.label_Notes.setStyleSheet(u"font: 14pt \"Segoe UI Symbol\";")

        self.horizontalLayout.addWidget(self.label_Notes)

        self.lineEdit_search = QLineEdit(self.header_allNotes)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setStyleSheet(u"border: 1px solid rgb(233, 233, 233);\n"
"border-top-color: rgb(37, 37, 37);\n"
"border-right-color: rgb(37, 37, 37);\n"
"border-left-color: rgb(37, 37, 37);\n"
"")

        self.horizontalLayout.addWidget(self.lineEdit_search)

        self.btn_search = QPushButton(self.header_allNotes)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(27, 27))
        self.btn_search.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/svg/search_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_search)


        self.verticalLayout.addWidget(self.header_allNotes)

        self.allNotes = QFrame(self.allNotesPage)
        self.allNotes.setObjectName(u"allNotes")
        self.allNotes.setFrameShape(QFrame.StyledPanel)
        self.allNotes.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.allNotes)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.allNotes)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 80, 87))
        self.scrollAreaWidgetContents.setStyleSheet(u"border: 0px;\n"
"border-radius: 15px;")
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(self.scrollAreaWidgetContents)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"")
        self.tableView.setDragEnabled(True)
        self.tableView.setTextElideMode(Qt.ElideLeft)

        self.gridLayout_3.addWidget(self.tableView, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.allNotes)

        self.frame = QFrame(self.allNotesPage)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 46))
        self.frame.setStyleSheet(u"border-radius: 20px;\n"
"")
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.btn_add = QPushButton(self.frame)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMinimumSize(QSize(40, 40))
        self.btn_add.setMaximumSize(QSize(60, 40))
        self.btn_add.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/svg/plus_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add.setIcon(icon1)
        self.btn_add.setIconSize(QSize(18, 18))

        self.horizontalLayout_5.addWidget(self.btn_add)


        self.verticalLayout.addWidget(self.frame)

        self.stackedWidget.addWidget(self.allNotesPage)
        self.notePage = QWidget()
        self.notePage.setObjectName(u"notePage")
        self.verticalLayout_2 = QVBoxLayout(self.notePage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(18, -1, -1, -1)
        self.header_notes = QFrame(self.notePage)
        self.header_notes.setObjectName(u"header_notes")
        sizePolicy.setHeightForWidth(self.header_notes.sizePolicy().hasHeightForWidth())
        self.header_notes.setSizePolicy(sizePolicy)
        self.header_notes.setMinimumSize(QSize(0, 45))
        self.header_notes.setMaximumSize(QSize(16777215, 45))
        self.header_notes.setFrameShape(QFrame.StyledPanel)
        self.header_notes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_notes)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.btn_back = QPushButton(self.header_notes)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setMinimumSize(QSize(27, 27))
        self.btn_back.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/svg/back_arrow_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btn_back, 0, Qt.AlignLeft)

        self.btns_forEdit = QFrame(self.header_notes)
        self.btns_forEdit.setObjectName(u"btns_forEdit")
        self.btns_forEdit.setFrameShape(QFrame.StyledPanel)
        self.btns_forEdit.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.btns_forEdit)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_saveChanges = QPushButton(self.btns_forEdit)
        self.btn_saveChanges.setObjectName(u"btn_saveChanges")
        self.btn_saveChanges.setMinimumSize(QSize(27, 27))
        self.btn_saveChanges.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/svg/checkYesDisabled_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_saveChanges.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.btn_saveChanges)

        self.btn_edit = QPushButton(self.btns_forEdit)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setMinimumSize(QSize(27, 27))
        self.btn_edit.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/svg/edit_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit.setIcon(icon4)

        self.horizontalLayout_4.addWidget(self.btn_edit)


        self.horizontalLayout_2.addWidget(self.btns_forEdit, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.header_notes)

        self.lineEdit_Title = QLineEdit(self.notePage)
        self.lineEdit_Title.setObjectName(u"lineEdit_Title")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.lineEdit_Title.setFont(font1)
        self.lineEdit_Title.setStyleSheet(u"color: rgb(253, 253, 253);")

        self.verticalLayout_2.addWidget(self.lineEdit_Title)

        self.label_date = QLabel(self.notePage)
        self.label_date.setObjectName(u"label_date")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Symbol"])
        self.label_date.setFont(font2)
        self.label_date.setStyleSheet(u"color: rgb(106, 106, 106);")

        self.verticalLayout_2.addWidget(self.label_date)

        self.label_dateUpdate = QLabel(self.notePage)
        self.label_dateUpdate.setObjectName(u"label_dateUpdate")

        self.verticalLayout_2.addWidget(self.label_dateUpdate)

        self.textEdit_bodyNote = QTextEdit(self.notePage)
        self.textEdit_bodyNote.setObjectName(u"textEdit_bodyNote")

        self.verticalLayout_2.addWidget(self.textEdit_bodyNote)

        self.btn_delete = QPushButton(self.notePage)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMinimumSize(QSize(65, 30))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Semibold"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.btn_delete.setFont(font3)
        self.btn_delete.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.btn_delete, 0, Qt.AlignRight)

        self.stackedWidget.addWidget(self.notePage)
        self.addNotePage = QWidget()
        self.addNotePage.setObjectName(u"addNotePage")
        self.verticalLayout_3 = QVBoxLayout(self.addNotePage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.header_notes_2 = QFrame(self.addNotePage)
        self.header_notes_2.setObjectName(u"header_notes_2")
        sizePolicy.setHeightForWidth(self.header_notes_2.sizePolicy().hasHeightForWidth())
        self.header_notes_2.setSizePolicy(sizePolicy)
        self.header_notes_2.setMinimumSize(QSize(0, 45))
        self.header_notes_2.setMaximumSize(QSize(16777215, 45))
        self.header_notes_2.setFrameShape(QFrame.StyledPanel)
        self.header_notes_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_notes_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_back_2 = QPushButton(self.header_notes_2)
        self.btn_back_2.setObjectName(u"btn_back_2")
        self.btn_back_2.setMinimumSize(QSize(27, 27))
        self.btn_back_2.setStyleSheet(u"")
        self.btn_back_2.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.btn_back_2, 0, Qt.AlignLeft)

        self.btn_save = QPushButton(self.header_notes_2)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(55, 30))
        self.btn_save.setFont(font3)
        self.btn_save.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.btn_save, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.header_notes_2)

        self.lineEdit_Title_2 = QLineEdit(self.addNotePage)
        self.lineEdit_Title_2.setObjectName(u"lineEdit_Title_2")
        self.lineEdit_Title_2.setFont(font1)
        self.lineEdit_Title_2.setStyleSheet(u"color: rgb(253, 253, 253);")

        self.verticalLayout_3.addWidget(self.lineEdit_Title_2)

        self.textEdit_bodyNote_2 = QTextEdit(self.addNotePage)
        self.textEdit_bodyNote_2.setObjectName(u"textEdit_bodyNote_2")

        self.verticalLayout_3.addWidget(self.textEdit_bodyNote_2)

        self.stackedWidget.addWidget(self.addNotePage)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setMinimumSize(QSize(0, 10))
        self.statusbar.setMaximumSize(QSize(16777215, 10))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439  \u0441\u043f\u0438\u0441\u043e\u043a", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.label_Notes.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.btn_search.setText("")
        self.btn_add.setText("")
        self.btn_back.setText("")
        self.btn_saveChanges.setText("")
        self.btn_edit.setText("")
        self.lineEdit_Title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_dateUpdate.setText(QCoreApplication.translate("MainWindow", u"Last update: ", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.btn_back_2.setText("")
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.lineEdit_Title_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Title", None))
    # retranslateUi

