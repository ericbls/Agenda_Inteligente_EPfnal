import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Dia():
    def __init__(self):
        self.tabDayContent = QGraphicsView()
        self.tabWeekContent = QListView()
        self.tabMonthContent = QGraphicsView()
        
    def addCompromisso(self):
        content = QGraphicsScene()
        content.setSceneRect(QRectF(0,0, self.tabMonthContent.width(), self.tabMonthContent.height() ) )
         
        tipPolygon = QPolygonF()
        tipPolygon.append(QPointF(10,10))
        tipPolygon.append(QPointF(20,10))
        tipPolygon.append(QPointF(20,20))
        tipPolygon.append(QPointF(10,20))
        
        tip = QGraphicsPolygonItem(tipPolygon, None, None)
        tip.setPos(0,0)
        
        
        content.addItem(tip)
        
        self.tabMonthContent.setScene(content)

class Semana():
    print()

class Calendario(QAbstractScrollArea):
    def __init__(self):
        super(Calendario, self).__init__()
        self.setDefault()
        self.createLayoutMes()
        
    def createLayoutMes(self):
        layout_Mes = QGridLayout(self)
        
        today = QDate.currentDate()
        first = today.addDays( -(today.day()-1) )
        if first.dayOfWeek() <= 6:
            begin = first.addDays( -first.dayOfWeek() )
        else:
            begin = first.addDays(-7)
        
        
        self.buttonSetMonth = QPushButton('{0}'.format(QDate.longMonthName(first.month()).upper()))
        self.buttonNextMonth = QPushButton('-->')
        self.buttonMonthBefore = QPushButton('<--')
        
        self.showYear = QPushButton('{0}'.format(first.year()))
        self.showSeg = QPushButton('Seg')
        self.showTer = QPushButton('Ter')
        self.showQua = QPushButton('Qua')
        self.showQui = QPushButton('Qui')
        self.showSex = QPushButton('Sex')
        self.showSab = QPushButton('Sab')
        self.showDom = QPushButton('Dom')
        self.showYear.setDisabled(True)
        self.showSeg.setDisabled(True)
        self.showTer.setDisabled(True)
        self.showQua.setDisabled(True)
        self.showQui.setDisabled(True)
        self.showSex.setDisabled(True)
        self.showSab.setDisabled(True)
        self.showDom.setDisabled(True)
        
        layout_Mes.addWidget(self.buttonSetMonth, 0,0,1,7)
        layout_Mes.addWidget(self.buttonMonthBefore, 1,0,1,3)
        layout_Mes.addWidget(self.showYear, 1,3,1,1)
        layout_Mes.addWidget(self.buttonNextMonth, 1,4,1,3)
        layout_Mes.addWidget(self.showSeg, 2,0,1,1)
        layout_Mes.addWidget(self.showTer, 2,1,1,1)
        layout_Mes.addWidget(self.showQua, 2,2,1,1)
        layout_Mes.addWidget(self.showQui, 2,3,1,1)
        layout_Mes.addWidget(self.showSex, 2,4,1,1)
        layout_Mes.addWidget(self.showSab, 2,5,1,1)
        layout_Mes.addWidget(self.showDom, 2,6,1,1)
        
        self.shownDays = dict()
        self.shownLabels = dict()
        for i in range(42):
            self.shownDays['{0}'.format(begin.getDate())] = Dia()
            self.shownDays['{0}'.format(begin.getDate())].tabMonthContent.resize(50,50)
            self.shownLabels['{0}'.format(begin.getDate())] = QLabel(' {0}'.format(begin.day() ) + '\n'*3 )
            
            
            
            if i <= 6:
                layout_Mes.addWidget(self.shownDays['{0}'.format(begin.getDate())].tabMonthContent, 3,i,1,1)
                layout_Mes.addWidget(self.shownLabels['{0}'.format(begin.getDate())], 3,i,1,1)
            elif i > 6 and i <= 13:
                layout_Mes.addWidget(self.shownDays['{0}'.format(begin.getDate())].tabMonthContent, 4,(i-7),1,1)
                layout_Mes.addWidget(self.shownLabels['{0}'.format(begin.getDate())], 4,(i-7),1,3)
            elif i > 13 and i <= 20:
                layout_Mes.addWidget(self.shownDays['{0}'.format(begin.getDate())].tabMonthContent, 5,(i-14),1,1)
                layout_Mes.addWidget(self.shownLabels['{0}'.format(begin.getDate())], 5,(i-14),1,3)
            elif i > 20 and i <= 27:
                layout_Mes.addWidget(self.shownDays['{0}'.format(begin.getDate())].tabMonthContent, 6,(i-21),1,1)
                layout_Mes.addWidget(self.shownLabels['{0}'.format(begin.getDate())], 6,(i-21),1,3)
            elif i > 27 and i <= 34:
                layout_Mes.addWidget(self.shownDays['{0}'.format(begin.getDate())].tabMonthContent, 7,(i-28),1,1)
                layout_Mes.addWidget(self.shownLabels['{0}'.format(begin.getDate())], 7,(i-28),1,3)
            elif i > 34 and i <= 41:
                layout_Mes.addWidget(self.shownDays['{0}'.format(begin.getDate())].tabMonthContent, 8, (i-35),1,1)
                layout_Mes.addWidget(self.shownLabels['{0}'.format(begin.getDate())], 8,(i-35),1,3)
            begin = begin.addDays(1)
        self.main_widget.setLayout(layout_Mes)
    
    def setDefault(self):
        self.main_widget = QWidget()
        
        self.layout_ScrollArea = QVBoxLayout(self)
        self.layout_ScrollArea.addWidget(self.main_widget)
        self.setLayout(self.layout_ScrollArea)
        
        stylesheet = \
            ".QWidget {\n" \
            + "border: 0px solid black;\n" \
            + "border-radius: 5px;\n" \
            + "background-color: rgb(200, 200, 200);\n" \
            + "}"
        self.main_widget.setStyleSheet(stylesheet)

        

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
        self.buttonUnico_OUT = QPushButton('Voltar')
        self.buttonUnico_OK = QPushButton('Ok')
        self.buttonFlexivel = QPushButton('Flexível')
        self.buttonPersonalInfo = QPushButton('Informações\n Pessoais')
        self.buttonConfig = QPushButton('Configurações')
        self.separator1 = QWidget()
        
        
        self.Title = QLineEdit()
        self.Title.setPlaceholderText('Título')
        
        
        self.groupBoxOptions = QGroupBox('Tipo de compromisso')
        self.groupBoxUnico = QGroupBox('Único')
        
        layout_groupBoxOptions = QVBoxLayout()
        layout_groupBoxOptions.addWidget(self.buttonUnico)
        layout_groupBoxOptions.addWidget(self.buttonDiario)
        layout_groupBoxOptions.addWidget(self.buttonSemanal)
        layout_groupBoxOptions.addWidget(self.buttonMensal)
        layout_groupBoxOptions.addWidget(self.buttonFlexivel)
        self.groupBoxOptions.setLayout(layout_groupBoxOptions)
        
        
        
        layout_groupBoxUnico = QGridLayout()
        layout_groupBoxUnico.addWidget(QWidget(), 0,0,1,2)
        layout_groupBoxUnico.addWidget(self.buttonUnico_OUT, 1,0,1,1)
        layout_groupBoxUnico.addWidget(self.buttonUnico_OK, 1,1,1,1)
        self.groupBoxUnico.setLayout(layout_groupBoxUnico)
        
        
        
        

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Agenda inteligente')
        
        self.tabs = Tabs()
        self.buttons = BarOptions()
        self.mes = 0
        
        
        layout_main_sub1 = QGridLayout()
        layout_main_sub2 = QVBoxLayout()
        layout_main = QGridLayout()
        
        layout_main_sub1.addWidget(self.buttons.main_buttonIN, 0,0,1,1)
        layout_main_sub1.addWidget(self.buttons.main_buttonOUT, 0,0,1,1)
        layout_main_sub1.addWidget(self.buttons.Title, 1,0,1,1)
        layout_main_sub1.addWidget(self.buttons.separator1, 1,0,1,1)
        layout_main_sub1.addWidget(self.buttons.groupBoxOptions,2,0,1,1)
        layout_main_sub1.addWidget(self.buttons.groupBoxUnico, 2,0,1,1)
        layout_main_sub1.addWidget(self.buttons.buttonPersonalInfo, 3,0,1,1)
        layout_main_sub1.addWidget(self.buttons.buttonConfig, 4,0,1,1)
        
        
        self.buttons.main_buttonOUT.hide()
        self.buttons.Title.hide()
        self.buttons.groupBoxOptions.hide()
        self.buttons.groupBoxUnico.hide()
        
        layout_main_sub2.addWidget(self.tabs)
        layout_main.addLayout(layout_main_sub1, 0,0,1,1)
        layout_main.addLayout(layout_main_sub2, 0,1,1,1)
        
        self.setLayout(layout_main)
        
        
        
        self.buttons.main_buttonIN.clicked.connect(self.showOptions)
        self.buttons.main_buttonOUT.clicked.connect(self.hideOptions)
        self.buttons.buttonUnico.clicked.connect(self.showUnico)
        self.buttons.buttonUnico_OUT.clicked.connect(self.hideOption)
        self.tabs.calendario.buttonNextMonth.clicked.connect(self.nextMonth)
        self.tabs.calendario.buttonMonthBefore.clicked.connect(self.monthBefore)
        
        
        
        self.resize(self.tabs.width(), self.tabs.height())
        self.centerOnScreen()
        
        
    def centerOnScreen(self):
        resolution = QDesktopWidget().screenGeometry()
        self.move( ( (resolution.width() / 2 ) - (self.width() / 2 ) )-100 , ( (resolution.height() / 2 ) - ( self.height() / 2 ) )-50 )
    
    def showOptions(self):
        self.buttons.main_buttonIN.hide()
        self.buttons.separator1.hide()
        self.buttons.main_buttonOUT.show()
        self.buttons.Title.show()
        self.buttons.groupBoxOptions.show()
    
    def showUnico(self):
        self.buttons.groupBoxOptions.hide()
        self.buttons.groupBoxUnico.show()
    
    def hideOptions(self):
        self.buttons.main_buttonOUT.hide()
        self.buttons.main_buttonIN.show()
        self.buttons.Title.hide()
        self.buttons.groupBoxOptions.hide()
        self.buttons.groupBoxUnico.hide()
    
    def hideOption(self):
        self.buttons.groupBoxUnico.hide()
        self.buttons.groupBoxOptions.show()
    
    def nextMonth(self):
        self.mes += 1
        
        today = QDate.currentDate()
        first = today.addDays( -(today.day()-1) )
        nextFirst = first.addMonths(self.mes)
        
        if first.dayOfWeek() <= 6:
            begin = first.addDays( -first.dayOfWeek() )
        if first.dayOfWeek() > 6:
            begin = first.addDays(-7)
        if nextFirst.dayOfWeek() <= 6:
            nextBegin = nextFirst.addDays( -nextFirst.dayOfWeek() )
        if nextFirst.dayOfWeek() > 6:
            nextBegin = nextFirst.addDays(-7)
            
        for i in range(42):
            self.tabs.calendario.shownLabels['{0}'.format(begin.getDate())].setText(' {0}'.format(nextBegin.day() ) + '\n'*3 )
            begin = begin.addDays(1)
            nextBegin = nextBegin.addDays(1)
        
        self.tabs.calendario.buttonSetMonth.setText('{0}'.format(QDate.longMonthName(nextFirst.month()).upper()))
        self.tabs.calendario.showYear.setText('{0}'.format(nextFirst.year()))
    
    def monthBefore(self):
        self.mes -= 1
        
        today = QDate.currentDate()
        first = today.addDays( -(today.day()-1) )
        firstBefore = first.addMonths(self.mes)
        
        if first.dayOfWeek() <= 6:
            begin = first.addDays( -first.dayOfWeek() )
        if first.dayOfWeek() > 6:
            begin = first.addDays(-7)
        if firstBefore.dayOfWeek() <= 6:
            beginBefore = firstBefore.addDays( -firstBefore.dayOfWeek() )
        if firstBefore.dayOfWeek() > 6:
            beginBefore = firstBefore.addDays(-7)
            
        for i in range(42):
            self.tabs.calendario.shownLabels['{0}'.format(begin.getDate())].setText(' {0}'.format(beginBefore.day() ) + '\n'*3 )
            begin = begin.addDays(1)
            beginBefore = beginBefore.addDays(1)
        
        self.tabs.calendario.buttonSetMonth.setText('{0}'.format(QDate.longMonthName(firstBefore.month()).upper()))
        self.tabs.calendario.showYear.setText('{0}'.format(firstBefore.year()))
        
        
        
        





if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()