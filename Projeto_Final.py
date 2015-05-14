import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Dia():
    def __init__(self):
        self.tabDayContent = QGraphicsView()
        self.tabWeekContent = QListView()
        self.tabMonthContent = QGraphicsView()
        
    def addCompromisso(self):
        print()

class Semana():
    print()

class Calendario(QAbstractScrollArea):
    def __init__(self):
        super(Calendario, self).__init__()
        
        
        self.main_widget = QWidget()
        
        layout_ScrollArea = QVBoxLayout(self)
        layout_ScrollArea.addWidget(self.main_widget)
        self.setLayout(layout_ScrollArea)
        
        stylesheet = \
            ".QWidget {\n" \
            + "border: 0px solid black;\n" \
            + "border-radius: 5px;\n" \
            + "background-color: rgb(200, 200, 200);\n" \
            + "}"
        self.main_widget.setStyleSheet(stylesheet)
        
        self.createLayoutMes()
        
        
    def createLayoutMes(self):
        layout_Mes = QGridLayout(self)
        
        today = QDate.currentDate()
        first = today.addDays( -(today.day()-1) )
        if first.dayOfWeek() <= 6:
            begin = first.addDays( -first.dayOfWeek() )
        else:
            begin = first
        
        
        self.buttonSetMonth = QPushButton('{0}'.format(QDate.longMonthName(today.month()).upper()))
        self.buttonNextMonth = QPushButton('-->')
        self.buttonMonthBefore = QPushButton('<--')
        self.showYear = QPushButton('{0}'.format(today.year()))
        layout_Mes.addWidget(self.buttonSetMonth, 0,0,1,7)
        layout_Mes.addWidget(self.buttonMonthBefore, 1,0,1,3)
        layout_Mes.addWidget(self.showYear, 1,3,1,1)
        layout_Mes.addWidget(self.buttonNextMonth, 1,4,1,3)
        
        self.shownDays = dict()
        for i in range(42):
            self.shownDays['{0}'.format(begin.getDate())] = Dia()
            self.shownDays['{0}'.format(begin.getDate())].tabMonthContent.resize(50,50)
            
            content = QGraphicsScene()
            content.setSceneRect(QRectF(0,0, self.shownDays['{0}'.format(begin.getDate())].tabMonthContent.width(), self.shownDays['{0}'.format(begin.getDate())].tabMonthContent.height() ) )
            
            
            
            self.shownDays['{0}'.format(begin.getDate())].tabMonthContent.setScene(content)
            
            if i <= 6:
                layout_Mes.addWidget(self.shownDays['{0}'.format(begin.getDate())].tabMonthContent, 2,i,1,1)
                layout_Mes.addWidget(QLabel(' {0}'.format(begin.day() ) + '\n'*3 ), 2,i,1,1)
            elif i > 6 and i <= 13:
                layout_Mes.addWidget(self.shownDays['{0}'.format(begin.getDate())].tabMonthContent, 3,(i-7),1,1)
                layout_Mes.addWidget(QLabel(' {0}'.format(begin.day() ) + '\n'*3 ), 3,(i-7),1,3)
            elif i > 13 and i <= 20:
                layout_Mes.addWidget(self.shownDays['{0}'.format(begin.getDate())].tabMonthContent, 4,(i-14),1,1)
                layout_Mes.addWidget(QLabel(' {0}'.format(begin.day() ) + '\n'*3 ), 4,(i-14),1,3)
            elif i > 20 and i <= 27:
                layout_Mes.addWidget(self.shownDays['{0}'.format(begin.getDate())].tabMonthContent, 5,(i-21),1,1)
                layout_Mes.addWidget(QLabel(' {0}'.format(begin.day() ) + '\n'*3 ), 5,(i-21),1,3)
            elif i > 27 and i <= 34:
                layout_Mes.addWidget(self.shownDays['{0}'.format(begin.getDate())].tabMonthContent, 6,(i-28),1,1)
                layout_Mes.addWidget(QLabel(' {0}'.format(begin.day() ) + '\n'*3 ), 6,(i-28),1,3)
            elif i > 34 and i <= 41:
                layout_Mes.addWidget(self.shownDays['{0}'.format(begin.getDate())].tabMonthContent, 7, (i-35),1,1)
                layout_Mes.addWidget(QLabel(' {0}'.format(begin.day() ) + '\n'*3 ), 7,(i-35),1,3)
            begin = begin.addDays(1)
        self.main_widget.setLayout(layout_Mes)

        

class Tabs(QTabWidget):
    def __init__(self):
        super(Tabs, self).__init__()
        self.setFixedSize(720,540)
        
        self.tab1 = QWidget(self)
        self.tab2 = QWidget(self)
        self.tab3 = QWidget(self)
        
        
        self.calendario = Calendario()
        layout_tab1 = QVBoxLayout()
        layout_tab1.addWidget(self.calendario)
        self.tab1.setLayout(layout_tab1)
        
        
        
        self.addTab(self.tab1, 'Mês')
        self.addTab(self.tab2, 'Semana')
        self.addTab(self.tab3, 'Dia')

class BarOptions():
    def __init__(self):
        self.main_buttonIN = QPushButton('Adicionar Compromisso')
        self.main_buttonOUT = QPushButton('Cancelar')
        self.buttonDiario = QPushButton('Diário')
        self.buttonSemanal = QPushButton('Semanal')
        self.buttonMensal = QPushButton('Mensal')
        self.buttonUnico = QPushButton('Único')
        self.buttonFlexivel = QPushButton('Flexível')
        self.buttonPersonalInfo = QPushButton('Informações\n Pessoais')
        
        self.groupBoxOptions = QGroupBox('Tipo de compromisso')
        
        layout_groupBox = QVBoxLayout()
        layout_groupBox.addWidget(self.buttonUnico)
        layout_groupBox.addWidget(self.buttonDiario)
        layout_groupBox.addWidget(self.buttonSemanal)
        layout_groupBox.addWidget(self.buttonMensal)
        layout_groupBox.addWidget(self.buttonFlexivel)
        self.groupBoxOptions.setLayout(layout_groupBox)
        
        

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Agenda inteligente')
        
        self.tabs = Tabs()
        self.buttons = BarOptions()
        
        
        layout_main = QGridLayout()
        layout_main.addWidget(self.buttons.main_buttonIN, 0,0,1,1)
        layout_main.addWidget(self.buttons.main_buttonOUT, 0,0,1,1)
        layout_main.addWidget(self.buttons.groupBoxOptions,1,0,1,1)
        self.buttons.main_buttonOUT.hide()
        self.buttons.groupBoxOptions.hide()
        layout_main.addWidget(self.tabs, 0,1,2,1)
        self.setLayout(layout_main)
        
        
        
        self.buttons.main_buttonIN.clicked.connect(self.showOptions)
        self.buttons.main_buttonOUT.clicked.connect(self.hideOptions)
        
        
        
        
        self.resize(self.tabs.width(), self.tabs.height())
        self.centerOnScreen()
        
        
    def centerOnScreen(self):
        resolution = QDesktopWidget().screenGeometry()
        self.move( ( (resolution.width() / 2 ) - (self.width() / 2 ) )-100 , ( (resolution.height() / 2 ) - ( self.height() / 2 ) )-50 )
    
    def showOptions(self):
        self.buttons.main_buttonIN.hide()
        self.buttons.main_buttonOUT.show()
        self.buttons.groupBoxOptions.show()
    
    def hideOptions(self):
        self.buttons.main_buttonOUT.hide()
        self.buttons.main_buttonIN.show()
        self.buttons.groupBoxOptions.hide()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()