from businessLogic.databaseModel import add_note
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from datetime import datetime
import math


class CardViewModel(QAbstractTableModel):
    """
    Custom Table Model SQLite3 BD of rent, table expensesCategory
    """

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self.notes         = data
        self.minColumns    = 2
        self.maxColumns    = 8 
        self.notesClear    = self.notesCombine(self.notes, self.minColumns)
        self.maxLoader     = 5
        self.allData       = self.notesClear 
        self.startSlice    = 0
        self.endSlice      = self.maxLoader if len(self.allData) > self.maxLoader else len(self.allData)
        self.sectionData   = self.allData[self.startSlice:self.endSlice]
        self.user_data     = self.sectionData
        self.columns       = ["NUMBER", "CardView1", "CardVie2"]
        
        


    def flags(self, index):
        """
        Set roles for columns
        """                
        return  Qt.ItemIsSelectable | Qt.ItemIsEnabled
   
    def rowCount(self, *args, **kwargs):

        return len(self.user_data)
  
    def columnCount(self, *args, **kwargs):

        return len(self.columns)

    def headerData(self, section, orientation, role = Qt.DisplayRole):

        if  orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return  self.columns[section].title()
    
    def isMaxColumn(self):
        """"
        Check if it hits max number of columns
        """
        return (self.maxColumns + 1) == len(self.columns)

    def isMinColumn(self):
        """"
        Check if it hits max number of columns
        """
        return (self.minColumns + 1) == len(self.columns)    

    def notesCombine(self, notes, columnsNumber):         
        rowsCount          = math.ceil(len(notes)/columnsNumber)
        lenOfNotes         = len(notes)
        addNotes           = rowsCount*columnsNumber - lenOfNotes
        addList            = [['', '', '', '', '', ''] for n in range(0, addNotes)]
        notes              = notes if lenOfNotes%columnsNumber == 0 else notes + addList
        newNotes = []
        for row in range(1, rowsCount + 1):
            listRow = [row]
            minus = columnsNumber
            while(minus>0):
                listRow.append(notes[row*columnsNumber - minus])
                minus -= 1            
            newNotes.append(listRow)
        return newNotes    

    def data(self, index, role):
    
        try:
            if role == Qt.DisplayRole:
                cellInfo = self.user_data[index.row()][index.column()]
                
                if cellInfo[1] != "":
                    dt = datetime.strptime(cellInfo[3], '%Y-%m-%d')
                    month = dt.strftime("%b")
                    return f"{cellInfo[1]}\n \n \n{month} {dt.day}, {dt.year}"
                else:
                    return ""
            if role == Qt.FontRole:
                myFont = QFont()
                myFont.setBold(True)
                return myFont
            if role == Qt.TextAlignmentRole:
                return Qt.AlignCenter
        except KeyError: 
            return None
     

    def getCellInfo(self, index):
        """
        return dict: Text: str, Date: str and Color: QColor for cell
        """
        cellInfo = self.user_data[index.row()][index.column()]
        if cellInfo[0] != "":
            text = cellInfo[1]
            dt = datetime.strptime(cellInfo[3], '%Y-%m-%d')
            month = dt.strftime("%b")
            date = f"{month} {dt.day}, {dt.year}"
            color = cellInfo[5]
            cellDict = {'Text': text, 'Date': date, 'Color': color}
            return cellDict
        else:
            return None   

    def addColumn(self):
        if self.isMaxColumn() == False:
            self.columns.append("New Column")
            self.update(self.notes, len(self.columns) - 1)
            

    def removeColumn(self):
        if self.isMinColumn() == False:
            self.columns.pop()
            self.update(self.notes, len(self.columns) - 1)
        
    def changeColumnsNumber(self, columnNumber):
        columnNow  = len(self.columns) - 1
        addColumns = columnNumber - columnNow
        # print(f"columnNow: {columnNow}, We want: {columnNumber}, addColumns: {addColumns}")
        if addColumns > 0:
            addList = ['New Column' for n in range(0, addColumns)]
            self.columns = self.columns + addList
            # print(f"AddList: {len(addList)}, Columns: {len(self.columns) - 1}, {self.columns} ")
            self.update(self.notes, len(self.columns) - 1)
        if  addColumns < 0:
            self.columns =  self.columns[:len(self.columns) + addColumns]
            self.update(self.notes, len(self.columns) - 1) 

    def getStartSlice(self):
        return self.startSlice

    def getEndSlice(self):
        return self.endSlice

    def getId(self, index):
        cellInfo = self.user_data[index.row()][index.column()]
        if cellInfo[0] != "":
            return cellInfo[0]
        else:
            return None

    def isTheEndOfData(self):
        return self.endSlice == len(self.allData)

    def sectionUp(self):
        self.layoutAboutToBeChanged.emit()
        if self.startSlice - 1 >= 0:
            self.startSlice  = self.startSlice - 1
            self.endSlice    = self.endSlice - 1
            self.sectionData = self.allData[self.startSlice:self.endSlice]
            self.user_data   = self.sectionData
        self.layoutChanged.emit()        

    def sectionDown(self):
        self.layoutAboutToBeChanged.emit()
        if self.endSlice + 1 <= len(self.allData):
            self.startSlice  = self.startSlice + 1  
            self.endSlice    = self.endSlice + 1
            self.sectionData = self.allData[self.startSlice:self.endSlice]
            self.user_data = self.sectionData
        self.layoutChanged.emit()        

    def setData(self, index, value, role = Qt.EditRole):
        return False        
    
    def reSet(self):
        self.layoutAboutToBeChanged.emit()
        self.startSlice  = 0
        self.endSlice    = self.maxLoader if len(self.allData) > self.maxLoader else len(self.allData)
        self.sectionData = self.allData[self.startSlice:self.endSlice]
        self.user_data   = self.sectionData
        self.layoutChanged.emit()

    def update(self, data, columnNumber):
        self.layoutAboutToBeChanged.emit()
        self.notes       = data
        self.allData     = self.notesCombine(self.notes, columnNumber)
        self.startSlice  = 0
        self.endSlice    = self.maxLoader if len(self.allData) >= self.maxLoader else len(self.allData)
        self.sectionData = self.allData[self.startSlice:self.endSlice]
        self.user_data = self.sectionData
        self.layoutChanged.emit()

    def setMaxLoader(self, maxValue: int):
        self.maxLoader = maxValue   

    def getMaxLoader(self):
        return self.maxLoader 
    
    def getMaxColumn(self):
        return self.maxColumns