from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *



class CardViewDelegete(QStyledItemDelegate):
    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self, parent)
        self.textFont = QFont()
        self.textFont.setFamily(u"Segoe UI Semibold")
        self.textFont.setPointSize(11) 
        self.dateFont = QFont()
        self.dateFont.setFamily(u"Segoe UI Symbol")
        self.dateFont.setPointSize(9)


    def paint(self,painter,option,index):
        textDisplay = index.data()
        cellInfo       = index.model().getCellInfo(index)
        if cellInfo != None:
            painter.save()
            self.rect = option.rect

            self.card          = QRect(self.rect.x() + self.rect.width()*0.1, 
                                self.rect.y()*0.9 + self.rect.height()*0.1, 
                                self.rect.width()*0.9, 
                                self.rect.height()*0.8)
            self.cardText      = QRect(self.card.x() + self.card.width()*0.15, 
                                self.card.y() + self.card.height()*0.15, 
                                self.card.width()*0.7, 
                                self.card.height()*0.6)
            self.cardDate      = QRect(self.card.x() + self.card.width()*0.15, 
                                self.card.y() + self.card.height()*0.8, 
                                self.card.width()*0.7, 
                                self.card.height()*0.2)
            self.colorBtush = QBrush(cellInfo['Color'])
            painter.setRenderHint(QPainter.Antialiasing)
            path = QPainterPath()
            painter.setBrush(self.colorBtush)
            path.addRoundedRect(self.card, 10, 10)
            painter.setClipPath(path)
            painter.fillPath(path, painter.brush())
            painter.strokePath(path, painter.pen())
            painter.setPen(QColor(37, 37, 37))
            painter.setFont(self.textFont)     
            painter.drawText(self.cardText, Qt.TextWordWrap, cellInfo['Text'])
            painter.setPen(QColor(100, 100, 100))
            painter.setFont(self.dateFont)
            painter.drawText(self.cardDate, Qt.AlignLeft, cellInfo['Date'])
            painter.restore()   

