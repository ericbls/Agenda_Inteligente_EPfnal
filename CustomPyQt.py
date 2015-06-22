from PyQt4.QtGui import *
from PyQt4.QtCore import *

class CustomPushButton(QPushButton):
    def __init__(self, parent=None):
        super(CustomPushButton, self).__init__(parent)
    
    def setDEFAULT(self):
        self.setStyleSheet('color: black; \n background-color: light gray')
        self.idx = 0
    def color(self):
        if self.styleSheet() == 'color: black; \n background-color: light gray':
            self.setStyleSheet('color: white; \n background-color: gray')
            self.idx = 1
        else:
            self.setDEFAULT()
            self.idx = 0
    
    def setFunc(self, func):
        if func == 'SELECT DAY':
            self.setDEFAULT()
            self.setFixedSize(20,25)
            self.clicked.connect(self.color)
            self.idx = 0
        elif func == 'DELETE':
            self.indice = None

class CustomTextEdit(QTextEdit):
    def __init__(self, text):
        super(CustomTextEdit, self).__init__()
        self.setPlainText(text)
        self.setStyleSheet('color: gray')
        self.text = text
        
    def setDefault(self):
        self.clear()
        self.setPlainText(self.text)
        self.setStyleSheet('color: gray')
        
    def focusInEvent(self, event):
        if self.toPlainText() == self.text:
            self.clear()
            self.setStyleSheet('color: black')
            QTextEdit.focusInEvent(self, event)
    
    def focusOutEvent(self, event):
        if self.toPlainText() == '':
            self.setPlainText(self.text)
            self.setStyleSheet('color: gray')
            QTextEdit.focusOutEvent(self, event)

class CustomLabel(QLabel):
    def __init__(self, parent=None):
        super(CustomLabel, self).__init__(parent)
    
    def setAtributos(self, date):
        self.data = date
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            exec(self.func)
    
    def setFunc(self, func):
        self.func = func
    
    def setWin(self, win):
        self.win = win
    
class CustomListView(QListView):
    def __init__(self, parent=None):
        super(CustomListView, self).__init__(parent)
        self.model = QStandardItemModel()
        self.setModel(self.model)
    
    def setAtributos(self, date):
        self.data = date
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            exec(self.func)
    def setFunc(self, func):
        self.func = func
    
    def setWin(self, win):
        self.win = win

class CustomGraphicsView(QGraphicsView):
    def __init__(self):
        super(CustomGraphicsView, self).__init__()
    
    def setLayoutMes(self, action, num_compromissos=0):
        if action == 'add':
            # cria uma tela para desenhar coisas no retângulo do dia na aba do mês
            content = QGraphicsScene()
            content.setSceneRect(QRectF(0,0,85,45))
            
            for i in range(num_compromissos):
                # cria um quadrado
                tipPolygon = QPolygonF()
                tipPolygon.append(QPointF(10,10))
                tipPolygon.append(QPointF(20,10))
                tipPolygon.append(QPointF(20,20))
                tipPolygon.append(QPointF(10,20))
                
                if i <= 4:
                    width = 15*i
                    height = -5
                elif i <= 9:
                    width = 15*(i-5)
                    height = 10
                elif i <= 13:
                    width = 15*(i-10)
                    height = 25
                else:
                    more = QGraphicsTextItem('+{0}'.format(num_compromissos-14))
                    more.setPos(66.5,30)
                    content.addItem(more)
                    break
                
                
                tip = QGraphicsPolygonItem(tipPolygon, None, None)
                tip.setPos(width,height)
                tip.setBrush(QBrush(Qt.red))
                
                # adiciona o quadrado à tela
                content.addItem(tip)
            
            # adiciona a tela ao retângulo do dia na aba do mês
            self.setScene(content)
        elif action == 'remove':
            content = QGraphicsScene()
            content.setSceneRect(QRectF(0,0,85,45) )
            self.setScene(content)
