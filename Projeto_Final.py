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
        
        self.comboBoxMonths = QComboBox()
        self.comboBoxMonths.addItems(['JANEIRO',
                                     'FEVEREIRO',
                                     'MARÇO',
                                     'ABRIL',
                                     'MAIO',
                                     'JUNHO',
                                     'JULHO',
                                     'AGOSTO',
                                     'SETEMBRO',
                                     'OUTUBRO',
                                     'NOVEMBRO',
                                     'DEZEMBRO'])
        self.spinYears = QSpinBox()
        self.spinYears.setRange(1500,2500)
        self.spinYears.setValue(first.year())
        self.buttonSet_OK = QPushButton('Ok')
        
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
        layout_Mes.addWidget(self.comboBoxMonths, 0,2,1,1)
        layout_Mes.addWidget(self.spinYears, 0,4,1,1)
        
        layout_Mes.addWidget(self.buttonMonthBefore, 1,0,1,3)
        layout_Mes.addWidget(self.buttonSet_OK, 1,3,1,1)
        layout_Mes.addWidget(self.showYear, 1,3,1,1)
        layout_Mes.addWidget(self.buttonNextMonth, 1,4,1,3)
        
        layout_Mes.addWidget(self.showSeg, 2,0,1,1)
        layout_Mes.addWidget(self.showTer, 2,1,1,1)
        layout_Mes.addWidget(self.showQua, 2,2,1,1)
        layout_Mes.addWidget(self.showQui, 2,3,1,1)
        layout_Mes.addWidget(self.showSex, 2,4,1,1)
        layout_Mes.addWidget(self.showSab, 2,5,1,1)
        layout_Mes.addWidget(self.showDom, 2,6,1,1)
        
        self.comboBoxMonths.hide()
        self.spinYears.hide()
        self.buttonSet_OK.hide()
        
        self.shownDays = dict()
        self.shownLabels = dict()
        for i in range(1,43):
            self.shownDays['{0}'.format(i)] = Dia()
            self.shownDays['{0}'.format(i)].tabMonthContent.resize(50,50)
            self.shownLabels['{0}'.format(i)] = QLabel(' {0}'.format(begin.day() ) + '\n'*3 )
            
            
            
            if i <= 7:
                layout_Mes.addWidget(self.shownDays['{0}'.format(i)].tabMonthContent, 3,i-1,1,1)
                layout_Mes.addWidget(self.shownLabels['{0}'.format(i)], 3,i-1,1,1)
            elif i > 7 and i <= 14:
                layout_Mes.addWidget(self.shownDays['{0}'.format(i)].tabMonthContent, 4,(i-8),1,1)
                layout_Mes.addWidget(self.shownLabels['{0}'.format(i)], 4,(i-8),1,3)
            elif i > 14 and i <= 21:
                layout_Mes.addWidget(self.shownDays['{0}'.format(i)].tabMonthContent, 5,(i-15),1,1)
                layout_Mes.addWidget(self.shownLabels['{0}'.format(i)], 5,(i-15),1,3)
            elif i > 21 and i <= 28:
                layout_Mes.addWidget(self.shownDays['{0}'.format(i)].tabMonthContent, 6,(i-22),1,1)
                layout_Mes.addWidget(self.shownLabels['{0}'.format(i)], 6,(i-22),1,3)
            elif i > 28 and i <= 35:
                layout_Mes.addWidget(self.shownDays['{0}'.format(i)].tabMonthContent, 7,(i-29),1,1)
                layout_Mes.addWidget(self.shownLabels['{0}'.format(i)], 7,(i-29),1,3)
            elif i > 35 and i <= 42:
                layout_Mes.addWidget(self.shownDays['{0}'.format(i)].tabMonthContent, 8, (i-36),1,1)
                layout_Mes.addWidget(self.shownLabels['{0}'.format(i)], 8,(i-36),1,3)
            begin = begin.addDays(1)
        self.main_widget.setLayout(layout_Mes)
        print(self.shownDays)
    
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
        self.buttonPersonalInfo = QPushButton('Informações\n Pessoais')
        self.buttonConfig = QPushButton('Configurações')
        self.separator1 = QWidget()
        
        self.buttonDiario = QPushButton('Diário')
        
        self.buttonSemanal = QPushButton('Semanal')
        
        self.buttonMensal = QPushButton('Mensal')
        
        self.buttonUnico = QPushButton('Único')
        self.buttonUnico_OUT = QPushButton('Voltar')
        self.buttonUnico_OK = QPushButton('Ok')
        
        self.buttonFlexivel = QPushButton('Flexível')
        
        
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
        self.tabs.calendario.buttonSetMonth.clicked.connect(self.setMonth)
        self.tabs.calendario.buttonSet_OK.clicked.connect(self.setMonthOK)
        
        
        
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
        
        if nextFirst.dayOfWeek() <= 6:
            nextBegin = nextFirst.addDays( -nextFirst.dayOfWeek() )
        else:
            nextBegin = nextFirst.addDays(-7)
            
        for i in range(1,43):
            self.tabs.calendario.shownLabels['{0}'.format(i)].setText(' {0}'.format(nextBegin.day() ) + '\n'*3 )
            nextBegin = nextBegin.addDays(1)
        
        self.tabs.calendario.buttonSetMonth.setText('{0}'.format(QDate.longMonthName(nextFirst.month()).upper()))
        self.tabs.calendario.showYear.setText('{0}'.format(nextFirst.year()))
    
    def monthBefore(self):
        self.mes -= 1
        
        today = QDate.currentDate()
        first = today.addDays( -(today.day()-1) )
        firstBefore = first.addMonths(self.mes)
        
        if firstBefore.dayOfWeek() <= 6:
            beginBefore = firstBefore.addDays( -firstBefore.dayOfWeek() )
        else:
            beginBefore = firstBefore.addDays(-7)
            
        for i in range(1,43):
            self.tabs.calendario.shownLabels['{0}'.format(i)].setText(' {0}'.format(beginBefore.day() ) + '\n'*3 )
            beginBefore = beginBefore.addDays(1)
        
        self.tabs.calendario.buttonSetMonth.setText('{0}'.format(QDate.longMonthName(firstBefore.month()).upper()))
        self.tabs.calendario.showYear.setText('{0}'.format(firstBefore.year()))
    
    def setMonth(self):
        self.tabs.calendario.buttonSetMonth.hide()
        self.tabs.calendario.showYear.hide()
        self.tabs.calendario.comboBoxMonths.show()
        self.tabs.calendario.spinYears.show()
        self.tabs.calendario.buttonSet_OK.show()
    
    def setMonthOK(self):
        year = self.tabs.calendario.spinYears.value()
        month = self.tabs.calendario.comboBoxMonths.currentIndex()+1
        nextFirst = QDate( year, month, 1 )
        
        self.tabs.calendario.comboBoxMonths.hide()
        self.tabs.calendario.spinYears.hide()
        self.tabs.calendario.buttonSet_OK.hide()
        self.tabs.calendario.buttonSetMonth.show()
        self.tabs.calendario.showYear.show()
        
        if nextFirst.dayOfWeek() <= 6:
            nextBegin = nextFirst.addDays( -nextFirst.dayOfWeek() )
        else:
            nextBegin = nextFirst.addDays(-7)
            
        for i in range(1,43):
            self.tabs.calendario.shownLabels['{0}'.format(i)].setText(' {0}'.format(nextBegin.day() ) + '\n'*3 )
            nextBegin = nextBegin.addDays(1)
        
        self.tabs.calendario.buttonSetMonth.setText('{0}'.format(QDate.longMonthName(nextFirst.month()).upper()))
        self.tabs.calendario.showYear.setText('{0}'.format(nextFirst.year()))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()