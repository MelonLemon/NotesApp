# basic libraries 
import sys 
import platform
import time
import datetime
import math

# Pyside libraries


from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient, QScreen, QGuiApplication, QStandardItemModel, QStandardItem, QResizeEvent)   
from PySide2.QtWidgets import *


# GUI classes we made
from ui.templates.ui_main import Ui_MainWindow

#DATABADE
from businessLogic import databaseModel
connection = databaseModel.connect()

# Additional
from functools import partial
from businessLogic.cardviewModel import CardViewModel
from businessLogic.cardViewDelegete import CardViewDelegete

from ui.res import icons_svg_rc

class MainWindow(QMainWindow):
    #Class that will show the view, child class of QMainWindow
    # Init the class  
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Notes properties
        self.noteOpenId  = 0
        self.colorsNotes = [QColor(255,171,145), QColor(255, 204, 128), QColor(231, 237, 155), QColor(255,255,222),
                            QColor(129,222,234), QColor(207,148,218), QColor(127,203,195), QColor(244,143,177)]

        self.minNoteWidth = 150
        self.maxNoteWidth = 200
        self.noteHeight = 160

        self.LOGO = QIcon()
        self.LOGO.addFile(u":/svg/logo.svg", QSize(), QIcon.Normal, QIcon.Off)

        self.YES  = QIcon()
        self.YES.addFile(u":/svg/checkYes_icon.svg", QSize(), QIcon.Normal, QIcon.Off)

        self.YESDISABLED = QIcon()
        self.YESDISABLED.addFile(u":/svg/checkYesDisabled_icon.svg", QSize(), QIcon.Normal, QIcon.Off)    

          
        self.setWindowIcon(self.LOGO)
        self.setWindowTitle("Notys")
        
        self.ui.lineEdit_search.setClearButtonEnabled(True)
        self.ui.lineEdit_Title.setClearButtonEnabled(True)
        self.ui.lineEdit_Title_2.setClearButtonEnabled(True)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.editNote(False)
    
        # NAVIGATION THROUGH PAGES
        self.ui.btn_add.clicked.connect(self.changePageToAddNote)
        self.ui.btn_back.clicked.connect(self.backFromNote)
        self.ui.btn_back_2.clicked.connect(self.backFromNewNote)
        
        # Connect signals with slots
        self.ui.lineEdit_search.textChanged.connect(self.searchNotes)
        self.ui.btn_saveChanges.clicked.connect(self.saveEditOfNote)
        self.ui.btn_edit.clicked.connect(partial(self.editNote, True))
        self.ui.btn_save.clicked.connect(self.addNewNote)
        self.ui.btn_delete.clicked.connect(self.deleteNote)
        self.ui.tableView.verticalScrollBar().valueChanged.connect(self.scrollChange)

        # CARDVIEW
        self.notes         = databaseModel.get_all_notes(connection)
        self.notes         = [[n[0], n[1], n[2], n[3], n[4], self.colorsNotes[(self.notes.index(n))%len(self.colorsNotes)]] for n in self.notes]
        self.cardviewModel = CardViewModel(self.notes)
        self.ui.tableView.setModel(self.cardviewModel)
        self.ui.tableView.hideColumn(0)
        self.ui.tableView.horizontalHeader().hide()
        self.ui.tableView.setWordWrap(True) 
        self.ui.tableView.resizeRowsToContents()
        self.ui.tableView.setColumnWidth(1, self.minNoteWidth)
        self.ui.tableView.setColumnWidth(2, self.minNoteWidth)
        self.vercHeader  = self.ui.tableView.verticalHeader()
        self.vercHeader.setSectionResizeMode(QHeaderView.Fixed)
        self.vercHeader.setDefaultSectionSize(self.noteHeight)
        self.ui.tableView.clicked.connect(self.noteClicked)
        self.delegete    = CardViewDelegete()
        self.ui.tableView.setItemDelegateForColumn(1, self.delegete)
        self.ui.tableView.setItemDelegateForColumn(2, self.delegete)
        self.ui.tableView.setShowGrid(False)
        self.startScroll = self.ui.tableView.verticalScrollBar().minimum()
        self.endScroll   = self.ui.tableView.verticalScrollBar().maximum()
        
        screen = QGuiApplication.primaryScreen().geometry()
        self.move(screen.right() - self.minimumWidth()*1.25, 30)
        self.show()
    
    def noteClicked(self, index):
        """
        Change view to Note that was clicked
        by changing Stackwidget page and fill the page 
        """
        idNote = self.cardviewModel.getId(index)
        if idNote != None:
            noteOpen = databaseModel.get_all_notesById(connection, idNote)
            self.ui.stackedWidget.setCurrentWidget(self.ui.notePage)
            self.noteOpenId = noteOpen[0]
            self.fillNote(noteOpen[1], noteOpen[2], noteOpen[3], noteOpen[4])


    def fillNote(self, title, date, update, body):
        self.ui.lineEdit_Title.setText(title)
        dt      = datetime.datetime.strptime(date, '%Y-%m-%d')
        month   = dt.strftime("%b")        
        self.ui.label_date.setText(f"{month} {dt.day}, {dt.year}")
        updt    = datetime.datetime.strptime(update, '%Y-%m-%d')
        monthUp = updt.strftime("%b")
        self.ui.label_dateUpdate.setText(f"Last update: {monthUp} {updt.day}, {updt.year}")
        self.ui.textEdit_bodyNote.setText(body)
    
    def resizeEvent(self, event: QResizeEvent) -> None:
        
        gap = 50
        windowWidth             = self.width()
        heightTable             = self.ui.tableView.height() 
        maxLoader               = self.cardviewModel.getMaxLoader()
        maxColumnNumberModel    = self.cardviewModel.getMaxColumn()
        columnByWindowWidth     = math.floor((windowWidth - gap)/self.minNoteWidth)
        columnNumber            = columnByWindowWidth if columnByWindowWidth < maxColumnNumberModel else maxColumnNumberModel
        newWidth                = int((windowWidth - gap)/(columnNumber)) 
        newHeight               = int((heightTable + gap)/(maxLoader - 2))

        # Resize columns width and colunm Number in Model
        self.cardviewModel.changeColumnsNumber(columnNumber)
        [self.ui.tableView.setColumnWidth(column, newWidth) for column in range(1, columnNumber+1)]
        [self.ui.tableView.setItemDelegateForColumn(column, self.delegete) for column in range(1, columnNumber+1)]
        
        # Resize rows height
        if heightTable + gap > maxLoader*self.ui.tableView.rowHeight(1):
            self.vercHeader.setDefaultSectionSize(newHeight)
        else:
            self.vercHeader.setDefaultSectionSize(self.noteHeight)        
        super().resizeEvent(event)

    def changePageToAddNote(self):
        """
        Change current view(stackedWidget) to page add notes
        """
        self.ui.stackedWidget.setCurrentWidget(self.ui.addNotePage)
    
    def changePageToAllNotes(self):
        """
        Change current view(stackedWidget) to page with all notes
        """
        self.ui.stackedWidget.setCurrentWidget(self.ui.allNotesPage)
        self.cardviewModel.reSet()
        self.ui.tableView.verticalScrollBar().setValue(self.startScroll)

    def searchNotes(self, text):
        """
        Search(filter) notes matching text in search box
        """
        if text !="":
            newData = databaseModel.get_all_notesByText(connection, f"%{text}%", f"%{text}%", f"%{text}%", 
            f"%{text}%", f"%{text}%", f"%{text}%", f"%{text}%", f"%{text}%")
            newData = [[n[0], n[1], n[2], n[3], n[4], self.colorsNotes[(newData.index(n))%len(self.colorsNotes)]] for n in newData]
        else:
            newData = databaseModel.get_all_notes(connection)
            newData = [[n[0], n[1], n[2], n[3], n[4], self.colorsNotes[(newData.index(n))%len(self.colorsNotes)]] for n in newData]
        
        self.cardviewModel.update(newData, self.cardviewModel.columnCount() - 1)    
         

    def editNote(self, enabled: bool):
        """
        Enable edit of Note
        :param: enabled - bool - True to enable and False to disable
        """
        self.ui.lineEdit_Title.setEnabled(enabled)
        self.ui.textEdit_bodyNote.setEnabled(enabled)
        self.ui.btn_saveChanges.setEnabled(enabled)
        icon = self.YES if enabled == True else self.YESDISABLED
        self.ui.btn_saveChanges.setIcon(icon)
    
    def backFromNote(self):
        """
        Back to all notes from display notes page
        """
        self.editNote(False)
        self.changePageToAllNotes()

    def backFromNewNote(self):
        """
        Back to all notes from display notes page
        """
        self.clearNewNote()
        self.changePageToAllNotes()

        
    def clearNewNote(self):
        """
        clear Title and body in add new note page 
        """
        self.ui.lineEdit_Title_2.setText("")
        self.ui.textEdit_bodyNote_2.setText("")
    
    def scrollChange(self, int):
        """
         Set 
        """
        self.endScroll   = self.ui.tableView.verticalScrollBar().maximum()
        self.startScroll = self.ui.tableView.verticalScrollBar().minimum()
        # print(f"Max: {self.endScroll}, Min: {self.startScroll}, value {int}")
        if int == self.endScroll:
            self.cardviewModel.sectionDown()
            if self.cardviewModel.isTheEndOfData() == False:
                self.ui.tableView.verticalScrollBar().setValue(self.endScroll - 1)
        if int == self.startScroll:
            self.cardviewModel.sectionUp()
            if self.cardviewModel.getStartSlice() != 0:
                self.ui.tableView.verticalScrollBar().setValue(self.startScroll + 1)
        

    def saveEditOfNote(self):
        """
        Save changes if note in db
        """
        title      = self.ui.lineEdit_Title.text()
        body       = self.ui.textEdit_bodyNote.toPlainText()
        dateUpdate = datetime.date.today()
        databaseModel.update_note(connection, title, body, dateUpdate, self.noteOpenId)
        self.updateNotesData()
        self.cardviewModel.update(self.notes, self.cardviewModel.columnCount() - 1)
        self.backFromNote()

    def deleteNote(self):
        """
        Delete note from db
        """        
        databaseModel.delete_notes(connection, self.noteOpenId)
        self.updateNotesData()
        self.cardviewModel.update(self.notes, self.cardviewModel.columnCount() - 1)
        self.changePageToAllNotes()
    
    def updateNotesData(self):
        """
        Updates notes db
        """
        self.notes        = databaseModel.get_all_notes(connection)
        self.notes        = [[n[0], n[1], n[2], n[3], n[4], self.colorsNotes[(self.notes.index(n))%len(self.colorsNotes)]] for n in self.notes]

    def addNewNote(self):
        """
        Add new notes to the BD and navigate to all notes
        """
        if self.ui.lineEdit_Title_2.text() != "" or self.ui.textEdit_bodyNote_2.toPlainText() != "":
            self.addNewNoteToDB()
            self.clearNewNote()
            self.changePageToAllNotes()
            self.updateNotesData()
            self.cardviewModel.update(self.notes, self.cardviewModel.columnCount() - 1)        

    def addNewNoteToDB(self):
        """
        Add new not to db
        """
        dateCreate = datetime.date.today()
        dateUpdate = dateCreate
        title = self.ui.lineEdit_Title_2.text()
        body  = self.ui.textEdit_bodyNote_2.toPlainText()
        databaseModel.add_note(connection, title, dateCreate, dateUpdate, body)
    
    def initGeometryWindow(self,  aplhaPosY: float, windowWidth: int, windowHeight: int) -> None:
        """
        Initiate size and location of window 
        """
        screen = QGuiApplication.primaryScreen().geometry()
        self.move(screen.right(), screen.top())
        percentWidth = windowWidth/(screen.width())
        pos_x =  1
        pos_y = (screen.height())*aplhaPosY
        
        # self.setGeometry(pos_x, pos_y, windowWidth, windowHeight)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_()) 