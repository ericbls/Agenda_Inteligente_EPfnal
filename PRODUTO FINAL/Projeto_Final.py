import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from CustomPyQt import *
from BarOptions import *
from copy import *
from Compromissos import *
import simplejson, urllib
from random import choice
googleGeocodeUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'
#____________________________________________________________________________________________________________________________________

class Dia(QWidget):
    def __init__(self):
        super(Dia, self).__init__()
        self.currentDay = QPushButton()
        self.currentDay.setDisabled(True)
        today = QDate.currentDate()
        self.currentDay.setText('{0} {1}/{2}/{3}'.format(QDate.longDayName(today.dayOfWeek()).upper(), today.day(), today.month(), today.year()))
        self.nextDay = QPushButton('-->')
        self.dayBefore = QPushButton('<--')
        
        self.compromissosButton = QPushButton('Compromissos')
        self.compromissosButton.setStyleSheet('color: black')
        self.compromissosButton.setDisabled(True)
        
        self.mostraCompromissos = QScrollArea()
        self.mostraCompromissos.setWidgetResizable(True)
        self.mostraCompromissosBackGround = QWidget()
        self.mostraCompromissosBackGround.setStyleSheet('background-color: light gray')
        self.mostraCompromissos.setWidget(self.mostraCompromissosBackGround)
        self.layoutMostraCompromissosBackGround = QGridLayout(self.mostraCompromissosBackGround)
        self.layoutMostraCompromissosBackGround.addWidget(QWidget(), 1000,0,1,1)
        
        self.timeLineMain = QScrollArea()
        self.timeLineMain.setFixedWidth(620)
        self.timeLineMain.setWidgetResizable(True)
        
        self.timeLineBox = QGraphicsView()
        self.timeLineBox.setFixedWidth(502)
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0,0,500,1441)
        for linha in range(50):
            self.scene.addLine(QLineF( QLine( QPoint(0,(linha*29)+10),QPoint(725,(linha*29)+10) ) ) )
        self.timeLineBox.setScene(self.scene)
        
        self.timeLineBackGround = QWidget()
        self.timeLineBackGround.setStyleSheet('background-color: light gray')
        self.before23h30 = QPushButton('23h30')
        self.next0h00 = QPushButton('0h00')
        self.before23h30.setDisabled(True)
        self.next0h00.setDisabled(True)
        
        layout_BackGround = QGridLayout(self.timeLineBackGround)
        layout_BackGround.addWidget(self.before23h30, 0,0,1,1)
        layout_BackGround.addWidget(self.next0h00, 49,0,1,1)
        layout_BackGround.addWidget(self.timeLineBox, 0,1,50,12)
        
        for i in range(0,48,2):
            setattr(self, 'today{0}h00'.format(i//2), QPushButton('{0}h00'.format(i//2)))
            getattr(self, 'today{0}h00'.format(i//2)).setDisabled(True)
            getattr(self, 'today{0}h00'.format(i//2)).setStyleSheet('color: black')
            layout_BackGround.addWidget(getattr(self, 'today{0}h00'.format(i//2)), i+1,0,1,1)
        for i in range(1,49,2):
            setattr(self, 'today{0}h30'.format(i//2), QPushButton('{0}h30'.format(i//2)))
            getattr(self, 'today{0}h30'.format(i//2)).setDisabled(True)
            getattr(self, 'today{0}h30'.format(i//2)).setStyleSheet('color: black')
            layout_BackGround.addWidget(getattr(self, 'today{0}h30'.format(i//2)), i+1,0,1,1)
        
        self.timeLineMain.setWidget(self.timeLineBackGround)
        
        
        layout_main = QGridLayout(self)
        layout_main.addWidget(self.dayBefore, 0,0,1,1)
        layout_main.addWidget(self.currentDay, 0,1,1,1)
        layout_main.addWidget(self.nextDay, 0,2,1,1)
        layout_main.addWidget(self.timeLineMain, 2,0,1,3)
        layout_main.addWidget(self.compromissosButton, 0,3,1,1)
        layout_main.addWidget(self.mostraCompromissos, 2,3,1,1)

class Semana(QWidget):
    def __init__(self):
        super(Semana, self).__init__()
        self.createLayoutWeek()
    
    def createLayoutWeek(self):
        layout_Semana = QGridLayout(self)
        
        today = QDate.currentDate()
        
        if today.dayOfWeek() <= 6:
            begin = today.addDays( -today.dayOfWeek())
        else:
            begin = today
        
        self.buttonSetData = QPushButton('{0}'.format(QDate.longMonthName(today.month()).upper()))
        self.buttonNextWeek = QPushButton('-->')
        self.buttonWeekBefore = QPushButton('<--')
        
        self.spinDays = QSpinBox()
        self.spinDays.setRange(1,31)
        self.spinDays.setValue(today.day())
        
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
        self.spinYears.setValue(today.year())
        
        self.buttonToday = QPushButton('Hoje')
        self.buttonSet_OK = QPushButton('Ok')
        self.showYear = QPushButton('{0}'.format(today.year()))
        
        self.showYear.setDisabled(True)
        self.showYear.setStyleSheet('color: black')
        
        layout_Semana.addWidget(self.buttonSetData, 0,0,1,7)
        layout_Semana.addWidget(self.spinDays, 0,1,1,1)
        layout_Semana.addWidget(self.comboBoxMonths, 0,2,1,1)
        layout_Semana.addWidget(self.spinYears, 0,3,1,1)
        layout_Semana.addWidget(self.buttonToday, 0,4,1,1)
        layout_Semana.addWidget(self.buttonSet_OK, 0,5,1,1)
        
        layout_Semana.addWidget(self.buttonWeekBefore, 1,0,1,3)
        layout_Semana.addWidget(self.showYear, 1,3,1,1)
        layout_Semana.addWidget(self.buttonNextWeek, 1,4,1,3)
        
        # esconde elementos do layout que serão posteriormente chamados
        self.spinDays.hide()
        self.comboBoxMonths.hide()
        self.spinYears.hide()
        self.buttonToday.hide()
        self.buttonSet_OK.hide()
        
        for i in range(1,8):
            setattr(self,'list{0}'.format(i),CustomListView())
            getattr(self,'list{0}'.format(i)).setAtributos(begin)
            getattr(self,'list{0}'.format(i)).setFunc("self.win.tabs.setCurrentIndex(2)\ntoday = QDate.currentDate()\nself.win.dia = today.daysTo(self.data)\nself.win.tabs.dia.currentDay.setText('{0} {1}/{2}/{3}'.format(QDate.longDayName(self.data.dayOfWeek()).upper(),self.data.day(),self.data.month(),self.data.year()))\nself.win.checkCompromissos()")
            setattr(self,'buttonDay{0}'.format(i), QPushButton('{0} {1}'.format(QDate.shortDayName(begin.dayOfWeek()).upper(),begin.day())))
            getattr(self,'buttonDay{0}'.format(i)).setDisabled(True)
            layout_Semana.addWidget(getattr(self,'buttonDay{0}'.format(i)), 2,i-1,1,1)
            layout_Semana.addWidget(getattr(self,'list{0}'.format(i)), 3,i-1,1,1)
            
            if begin.month() != today.month():
                getattr(self,'buttonDay{0}'.format(i)).setStyleSheet('color: gray')
            else:
                getattr(self,'buttonDay{0}'.format(i)).setStyleSheet('color: black')
            
            begin = begin.addDays(1)

class Mes(QWidget):
    def __init__(self):
        super(Mes, self).__init__() # cria uma area principal que irá conter todos os elementos do calendário
        self.createLayoutMes() # cria os botões do calendário e adiciona os retângulos dos dias
        
    def createLayoutMes(self):
        layout_Mes = QGridLayout(self) # cria um layout de grade para a area com fundo cinza
        
        today = QDate.currentDate() # cria um objeto da classe QDate com a data do dia atual
        first = today.addDays( -(today.day()-1) ) # calcula o primeiro dia do mês atual
        
        # calcula quantos dias do mês anterior irão aparecer no calendário
        if first.dayOfWeek() <= 6:
            begin = first.addDays( -first.dayOfWeek() )
        else:
            begin = first.addDays(-7)
        
        
        self.buttonSetMonth = QPushButton('{0}'.format(QDate.longMonthName(first.month()).upper())) # cria botão que, quando clicado, abre um interface para plotar manualmente o mês e o ano desejados
        self.buttonNextMonth = QPushButton('-->') # cria botão que plota no calendário o mês seguinte
        self.buttonMonthBefore = QPushButton('<--') # cria botão que plota no calendário o mês anterior
        
        # cria um combo box com as opções de mês para plotar manualmente
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
        
        # cria um spin box para plotar o ano manualmente
        self.spinYears = QSpinBox()
        self.spinYears.setRange(1500,2500) # define o mínimo e o máximo para o spin box
        self.spinYears.setValue(first.year()) # define um valor inicial para o spin box quando chamado
        
        self.buttonToday = QPushButton('Hoje') # cria botão que, quando clicado, plota no calendário o mês atual
        self.buttonSet_OK = QPushButton('Ok') # cria botão que, quando clicado, plota as configurações definidas no combo box e no spin box
        
        self.showYear = QPushButton('{0}'.format(first.year())) # cria botão para mostrar o ano exibido
        
        # cria botões para exibir os dias da semana
        self.showSeg = QPushButton('Seg')
        self.showTer = QPushButton('Ter')
        self.showQua = QPushButton('Qua')
        self.showQui = QPushButton('Qui')
        self.showSex = QPushButton('Sex')
        self.showSab = QPushButton('Sab')
        self.showDom = QPushButton('Dom')
        
        # torna os botões no clicáveis
        self.showYear.setDisabled(True)
        self.showYear.setStyleSheet('color: black')
        self.showSeg.setDisabled(True)
        self.showSeg.setStyleSheet('color: black')
        self.showTer.setDisabled(True)
        self.showTer.setStyleSheet('color: black')
        self.showQua.setDisabled(True)
        self.showQua.setStyleSheet('color: black')
        self.showQui.setDisabled(True)
        self.showQui.setStyleSheet('color: black')
        self.showSex.setDisabled(True)
        self.showSex.setStyleSheet('color: black')
        self.showSab.setDisabled(True)
        self.showSab.setStyleSheet('color: black')
        self.showDom.setDisabled(True)
        self.showDom.setStyleSheet('color: black')
        
        # define as posições relativas de cada elemento no layout da area com fundo cinza
        # (posição de cada elemento em relação aos outros no layout)
        layout_Mes.addWidget(self.buttonSetMonth, 0,0,1,7)
        layout_Mes.addWidget(self.comboBoxMonths, 0,2,1,1)
        layout_Mes.addWidget(self.buttonToday, 0,3,1,1)
        layout_Mes.addWidget(self.spinYears, 0,4,1,1)
        
        layout_Mes.addWidget(self.buttonMonthBefore, 1,0,1,3)
        layout_Mes.addWidget(self.buttonSet_OK, 1,3,1,1)
        layout_Mes.addWidget(self.showYear, 1,3,1,1)
        layout_Mes.addWidget(self.buttonNextMonth, 1,4,1,3)
        
        layout_Mes.addWidget(self.showDom, 2,0,1,1)
        layout_Mes.addWidget(self.showSeg, 2,1,1,1)
        layout_Mes.addWidget(self.showTer, 2,2,1,1)
        layout_Mes.addWidget(self.showQua, 2,3,1,1)
        layout_Mes.addWidget(self.showQui, 2,4,1,1)
        layout_Mes.addWidget(self.showSex, 2,5,1,1)
        layout_Mes.addWidget(self.showSab, 2,6,1,1)
        
        # esconde elementos do layout que serão posteriormente chamados
        self.comboBoxMonths.hide()
        self.spinYears.hide()
        self.buttonToday.hide()
        self.buttonSet_OK.hide()
        
        
        for i in range(1,43):
            setattr(self,'graphic{0}'.format(i),CustomGraphicsView())
            getattr(self,'graphic{0}'.format(i)).resize(90,50) 
            setattr(self,'label{0}'.format(i),CustomLabel(' {0}'.format(begin.day() )+ '\n'*4 ))
            getattr(self,'label{0}'.format(i)).setAtributos(begin)
            getattr(self,'label{0}'.format(i)).setFunc("self.win.tabs.setCurrentIndex(2)\ntoday = QDate.currentDate()\nself.win.dia = today.daysTo(self.data)\nself.win.tabs.dia.currentDay.setText('{0} {1}/{2}/{3}'.format(QDate.longDayName(self.data.dayOfWeek()).upper(),self.data.day(),self.data.month(),self.data.year()))\nself.win.checkCompromissos()")
            
            # determina as cores dos números dos dias no calendário
            if begin.month() != today.month():
                getattr(self,'label{0}'.format(i)).setStyleSheet('color: gray') # dias que não pertençam ao mês exibido ficam com o número cinza
            else:
                getattr(self,'label{0}'.format(i)).setStyleSheet('color: black')
            
            
            # plota os retângulos dos dias e os números dos dias nas suas posições relativas no layout da area de fundo cinza
            if i <= 7:
                layout_Mes.addWidget(getattr(self,'graphic{0}'.format(i)), 3,i-1,1,1)
                layout_Mes.addWidget(getattr(self,'label{0}'.format(i)), 3,i-1,1,1)
            elif i > 7 and i <= 14:
                layout_Mes.addWidget(getattr(self,'graphic{0}'.format(i)), 4,(i-8),1,1)
                layout_Mes.addWidget(getattr(self,'label{0}'.format(i)), 4,(i-8),1,3)
            elif i > 14 and i <= 21:
                layout_Mes.addWidget(getattr(self,'graphic{0}'.format(i)), 5,(i-15),1,1)
                layout_Mes.addWidget(getattr(self,'label{0}'.format(i)), 5,(i-15),1,3)
            elif i > 21 and i <= 28:
                layout_Mes.addWidget(getattr(self,'graphic{0}'.format(i)), 6,(i-22),1,1)
                layout_Mes.addWidget(getattr(self,'label{0}'.format(i)), 6,(i-22),1,3)
            elif i > 28 and i <= 35:
                layout_Mes.addWidget(getattr(self,'graphic{0}'.format(i)), 7,(i-29),1,1)
                layout_Mes.addWidget(getattr(self,'label{0}'.format(i)), 7,(i-29),1,3)
            elif i > 35 and i <= 42:
                layout_Mes.addWidget(getattr(self,'graphic{0}'.format(i)), 8, (i-36),1,1)
                layout_Mes.addWidget(getattr(self,'label{0}'.format(i)), 8,(i-36),1,3)
            begin = begin.addDays(1)

        

class Tabs(QTabWidget):
    def __init__(self):
        super(Tabs, self).__init__() # cria area principal, capaz de receber abas
        self.setFixedSize(850,600) # define dimensões fixas para a area principal
        
        # cria tres abas 
        self.tab1 = QWidget(self)
        self.tab2 = QWidget(self)
        self.tab3 = QWidget(self)
        self.tab4 = QWidget(self)
        
        stylesheet = \
            ".QWidget {\n" \
            + "border: 0px solid black;\n" \
            + "border-radius: 0px;\n" \
            + "background-color: rgb(200, 200, 200);\n" \
            + "}"
        self.tab1.setStyleSheet(stylesheet)
        self.tab2.setStyleSheet(stylesheet)
        self.tab3.setStyleSheet(stylesheet)
        self.tab4.setStyleSheet(stylesheet)
        
        self.calendario_Mes = Mes() # cria um objeto da classe Mes()
        layout_tab1 = QVBoxLayout(self.tab1) # cria layout para a aba tab1
        layout_tab1.addWidget(self.calendario_Mes) # adiciona o calendário ao layout da aba tab1
        
        self.semana = Semana()
        layout_tab2 = QVBoxLayout(self.tab2)
        layout_tab2.addWidget(self.semana)
        
        self.dia = Dia()
        layout_tab3 = QVBoxLayout(self.tab3)
        layout_tab3.addWidget(self.dia)
        
        
        self.descricaoCompromisso = QListView()
        self.descricaoCompromissoModel = QStandardItemModel()
        self.descricaoCompromisso.setModel(self.descricaoCompromissoModel)
        self.editarCompromisso = QPushButton('Editar')
        self.delCompromisso = QPushButton('Deletar Compromisso')
        self.certeza = CustomPushButton('Certeza?')
        self.certeza.setFunc('DELETE')
        self.nao = QPushButton('Não')
        
        
        
        layout_tab4 = QGridLayout(self.tab4)
        layout_tab4.addWidget(self.editarCompromisso, 0,0,1,1)
        layout_tab4.addWidget(self.delCompromisso, 0,8,1,2)
        layout_tab4.addWidget(self.certeza, 0,8,1,1)
        layout_tab4.addWidget(self.nao, 0,9,1,1)
        layout_tab4.addWidget(self.descricaoCompromisso, 1,0,1,10)
        
        self.certeza.hide()
        self.nao.hide()
        
        
        self.addTab(self.tab1, 'Mês')
        self.addTab(self.tab2, 'Semana')
        self.addTab(self.tab3, 'Dia')
        self.addTab(self.tab4, 'Compromisso')
        
        self.delCompromisso.clicked.connect(self.checkTrue)
        self.nao.clicked.connect(self.setReturn)
    
    def checkTrue(self):
        self.delCompromisso.hide()
        
        self.certeza.show()
        self.nao.show()
    
    def setReturn(self):
        self.nao.hide()
        self.certeza.hide()
        
        self.delCompromisso.show()
        
        
#_____________________________________________________________________________________________________________________________


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__() # cria a janela do aplicativo
        self.setWindowTitle('Agenda inteligente') # define o título da janela
        
        self.tabs = Tabs() # gera o conjunto de abas
        self.buttons = BarOptions() # gera a barra de opções
        self.mes = 0 # define uma referência para os mêses exibidos
        today = QDate.currentDate()
        if today.dayOfWeek() <= 6:
            self.semana = 0
        else:
            self.semana = 1
        self.dia = 0
        self.settedCompromissos = {}
        self.idxHistorico = 0
        
        
        layout_main_sub1 = QGridLayout() # cria layout para depositar a barra de opções
        layout_main_sub2 = QVBoxLayout() # cria layout para depositar o conjunto de abas
        layout_main = QGridLayout(self) # cria layout para a janela do aplicativo
        
        # adiciona ao layout da barra de opções os seus elementos
        layout_main_sub1.addWidget(self.buttons.main_buttonIN, 0,0,1,8)
        layout_main_sub1.addWidget(self.buttons.main_buttonOUT, 0,0,1,8)
        layout_main_sub1.addWidget(self.buttons.Title, 1,0,1,8)
        layout_main_sub1.addWidget(self.buttons.separator1, 1,0,1,8)
        layout_main_sub1.addWidget(self.buttons.endereco, 2,0,1,8)
        layout_main_sub1.addWidget(self.buttons.optionFlexivel, 3,0,1,2)
        layout_main_sub1.addWidget(self.buttons.optionFixo, 3,2,1,6)
        
        
        layout_main_sub1.addWidget(self.buttons.repetirLabel, 4,0,1,1)
        layout_main_sub1.addWidget(self.buttons.repetir, 4,1,1,7)
        layout_main_sub1.addWidget(self.buttons.transporteLabel, 5,0,1,1)
        layout_main_sub1.addWidget(self.buttons.transporte, 5,1,1,7)
        layout_main_sub1.addWidget(self.buttons.inicioLabel, 6,0,1,8)
        layout_main_sub1.addWidget(self.buttons.inicioDate, 7,0,1,2)
        layout_main_sub1.addWidget(self.buttons.inicioTime, 7,2,1,6)
        layout_main_sub1.addWidget(self.buttons.terminoLabel, 8,0,1,8)
        layout_main_sub1.addWidget(self.buttons.terminoDate, 9,0,1,2)
        layout_main_sub1.addWidget(self.buttons.terminoTime, 9,2,1,6)
        layout_main_sub1.addWidget(self.buttons.allDay, 10,0,1,8)
        
        layout_main_sub1.addWidget(self.buttons.spinDuracaoLabel, 4,0,1,1)
        layout_main_sub1.addWidget(self.buttons.spinDuracao, 4,1,1,7)
        layout_main_sub1.addWidget(self.buttons.prioridadeLabel, 5,0,1,1)
        layout_main_sub1.addWidget(self.buttons.prioridade, 5,1,1,7)
        layout_main_sub1.addWidget(self.buttons.dataLimiteCheck, 6,0,1,1)
        layout_main_sub1.addWidget(self.buttons.dataLimite, 6,1,1,7)
        layout_main_sub1.addWidget(self.buttons.restricaoTimeCheck, 7,0,1,8)
        layout_main_sub1.addWidget(self.buttons.restricaoTimeDasLabel, 8,0,1,1)
        layout_main_sub1.addWidget(self.buttons.restricaoTimeDas, 8,1,1,7)
        layout_main_sub1.addWidget(self.buttons.restricaoTimeAteLabel, 9,0,1,1)
        layout_main_sub1.addWidget(self.buttons.restricaoTimeAte, 9,1,1,7)
        layout_main_sub1.addWidget(self.buttons.restricaoDayOfWeekCheck, 10,0,1,8)
        layout_main_sub1.addWidget(self.buttons.restricaoDom, 11,1,1,1)
        layout_main_sub1.addWidget(self.buttons.restricaoSeg, 11,2,1,1)
        layout_main_sub1.addWidget(self.buttons.restricaoTer, 11,3,1,1)
        layout_main_sub1.addWidget(self.buttons.restricaoQua, 11,4,1,1)
        layout_main_sub1.addWidget(self.buttons.restricaoQui, 11,5,1,1)
        layout_main_sub1.addWidget(self.buttons.restricaoSex, 11,6,1,1)
        layout_main_sub1.addWidget(self.buttons.restricaoSab, 11,7,1,1)
        
        
        layout_main_sub1.addWidget(self.buttons.Descricao, 12,0,1,8)
        layout_main_sub1.addWidget(self.buttons.buttonSetOK, 13,0,1,8)
        layout_main_sub1.addWidget(self.buttons.buttonConfig, 14,0,1,8)
        layout_main_sub1.addWidget(self.buttons.separator2, 15,0,1,8)
        
        layout_main_sub2.addWidget(self.tabs)
        
        layout_main.addLayout(layout_main_sub1, 0,0,1,1)
        layout_main.addLayout(layout_main_sub2, 0,1,1,1)
        
        # esconde os elementos que serão posteriormente chamados
        self.buttons.main_buttonOUT.hide()
        self.buttons.Title.hide()
        self.buttons.endereco.hide()
        self.buttons.optionFixo.hide()
        self.buttons.optionFlexivel.hide()
        
        
        self.buttons.repetirLabel.hide()
        self.buttons.repetir.hide()
        self.buttons.transporteLabel.hide()
        self.buttons.transporte.hide()
        self.buttons.inicioLabel.hide()
        self.buttons.inicioDate.hide()
        self.buttons.inicioTime.hide()
        self.buttons.terminoLabel.hide()
        self.buttons.terminoDate.hide()
        self.buttons.terminoTime.hide()
        self.buttons.allDay.hide()
        
        self.buttons.spinDuracaoLabel.hide()
        self.buttons.spinDuracao.hide()
        self.buttons.prioridadeLabel.hide()
        self.buttons.prioridade.hide()
        self.buttons.dataLimiteCheck.hide()
        self.buttons.dataLimite.hide()
        self.buttons.restricaoTimeCheck.hide()
        self.buttons.restricaoTimeDasLabel.hide()
        self.buttons.restricaoTimeDas.hide()
        self.buttons.restricaoTimeAteLabel.hide()
        self.buttons.restricaoTimeAte.hide()
        self.buttons.restricaoDayOfWeekCheck.hide()
        self.buttons.restricaoSeg.hide()
        self.buttons.restricaoTer.hide()
        self.buttons.restricaoQua.hide()
        self.buttons.restricaoQui.hide()
        self.buttons.restricaoSex.hide()
        self.buttons.restricaoSab.hide()
        self.buttons.restricaoDom.hide()
        
        
        self.buttons.Descricao.hide()
        self.buttons.buttonSetOK.hide()
        self.buttons.separator2.hide()
        
        
        
        self.tabs.calendario_Mes.buttonNextMonth.clicked.connect(self.nextMonth)
        self.tabs.calendario_Mes.buttonMonthBefore.clicked.connect(self.monthBefore)
        self.tabs.calendario_Mes.buttonSetMonth.clicked.connect(self.setMonth)
        self.tabs.calendario_Mes.buttonSet_OK.clicked.connect(self.setMonthOK)
        self.tabs.calendario_Mes.buttonToday.clicked.connect(self.setTodayMonth)
        
        self.tabs.semana.buttonNextWeek.clicked.connect(self.nextWeek)
        self.tabs.semana.buttonWeekBefore.clicked.connect(self.weekBefore)
        self.tabs.semana.buttonSetData.clicked.connect(self.setData)
        self.tabs.semana.buttonSet_OK.clicked.connect(self.setWeekOK)
        self.tabs.semana.buttonToday.clicked.connect(self.setTodayWeek)
        
        self.tabs.dia.nextDay.clicked.connect(self.nextDay)
        self.tabs.dia.dayBefore.clicked.connect(self.dayBefore)
        
        self.tabs.editarCompromisso.clicked.connect(self.editarCompromisso)
        self.tabs.certeza.clicked.connect(self.removeCompromisso)
        
        # define as dimensões e a posição iniciais da janela do aplicativo
        self.resize(self.tabs.width(), self.tabs.height())
        self.centerOnScreen()
        
# MÈTODOS______________________________________________________________________________________________________________________________________________________________________    
    # move a janela para o centro da tela do monitor
    def centerOnScreen(self):
        resolution = QDesktopWidget().screenGeometry()
        self.move( ( (resolution.width() / 2 ) - (self.width() / 2 ) )-100 , ( (resolution.height() / 2 ) - ( self.height() / 2 ) )-50 )
    
    def nextMonth(self):
        self.mes += 1
        self.plotMonth('change')
        self.checkCompromissos()
    
    def nextWeek(self):
        self.semana += 1
        self.plotWeek('change')
        self.checkCompromissos()
    
    def nextDay(self):
        self.dia += 1
        
        today = QDate.currentDate()
        currentDate = today.addDays(self.dia)
        self.tabs.dia.currentDay.setText('{0} {1}/{2}/{3}'.format(QDate.longDayName(currentDate.dayOfWeek()).upper(), currentDate.day(), currentDate.month(), currentDate.year()))
        
        self.checkCompromissos()
    
    def monthBefore(self):
        self.mes -= 1
        self.plotMonth('change')
        self.checkCompromissos()
    
    def weekBefore(self):
        self.semana -= 1
        self.plotWeek('change')
        self.checkCompromissos()
    
    def dayBefore(self):
        self.dia -= 1
        
        today = QDate.currentDate()
        currentDate = today.addDays(self.dia)
        self.tabs.dia.currentDay.setText('{0} {1}/{2}/{3}'.format(QDate.longDayName(currentDate.dayOfWeek()).upper(), currentDate.day(), currentDate.month(), currentDate.year()))
        
        self.checkCompromissos()
    
    def setMonth(self):
        self.tabs.calendario_Mes.buttonSetMonth.hide()
        self.tabs.calendario_Mes.showYear.hide()
        
        self.tabs.calendario_Mes.comboBoxMonths.show()
        self.tabs.calendario_Mes.spinYears.show()
        
        self.tabs.calendario_Mes.buttonToday.show()
        self.tabs.calendario_Mes.buttonSet_OK.show()
        
        self.tabs.calendario_Mes.buttonMonthBefore.setDisabled(True)
        self.tabs.calendario_Mes.buttonNextMonth.setDisabled(True)
    
    def setData(self):
        self.tabs.semana.buttonSetData.hide()
        
        self.tabs.semana.spinDays.show()
        self.tabs.semana.comboBoxMonths.show()
        self.tabs.semana.spinYears.show()
        
        self.tabs.semana.comboBoxMonths.currentIndexChanged.connect(self.setRangeSpinDays)
        
        self.tabs.semana.buttonToday.show()
        self.tabs.semana.buttonSet_OK.show()
        
        self.tabs.semana.buttonNextWeek.setDisabled(True)
        self.tabs.semana.buttonWeekBefore.setDisabled(True)
    
    def setRangeSpinDays(self):
        month = 1 + self.tabs.semana.comboBoxMonths.currentIndex()
        year = self.tabs.semana.spinYears.value()
        date = QDate(year,month,1)
        
        self.tabs.semana.spinDays.setRange(1,date.daysInMonth())
        
    def setMonthOK(self):
        year = self.tabs.calendario_Mes.spinYears.value()
        month = self.tabs.calendario_Mes.comboBoxMonths.currentIndex()+1
        self.plotMonth('SET',year,month)
        self.checkCompromissos()
        
        self.tabs.calendario_Mes.comboBoxMonths.hide()
        self.tabs.calendario_Mes.spinYears.hide()
        self.tabs.calendario_Mes.buttonToday.hide()
        self.tabs.calendario_Mes.buttonSet_OK.hide()
        self.tabs.calendario_Mes.buttonSetMonth.show()
        self.tabs.calendario_Mes.showYear.show()
        self.tabs.calendario_Mes.buttonMonthBefore.setDisabled(False)
        self.tabs.calendario_Mes.buttonNextMonth.setDisabled(False)
    
    def setWeekOK(self):
        day = self.tabs.semana.spinDays.value()
        month = self.tabs.semana.comboBoxMonths.currentIndex() + 1
        year = self.tabs.semana.spinYears.value()
        self.plotWeek('SET', year, month, day)
        self.checkCompromissos()
        
        self.tabs.semana.spinDays.hide()
        self.tabs.semana.comboBoxMonths.hide()
        self.tabs.semana.spinYears.hide()
        self.tabs.semana.buttonToday.hide()
        self.tabs.semana.buttonSet_OK.hide()
        self.tabs.semana.buttonSetData.show()
        self.tabs.semana.buttonWeekBefore.setDisabled(False)
        self.tabs.semana.buttonNextWeek.setDisabled(False)
    
    def setTodayMonth(self):
        self.mes = 0
        self.plotMonth('change')
        self.checkCompromissos()
        
        self.tabs.calendario_Mes.comboBoxMonths.hide()
        self.tabs.calendario_Mes.spinYears.hide()
        self.tabs.calendario_Mes.buttonToday.hide()
        self.tabs.calendario_Mes.buttonSet_OK.hide()
        self.tabs.calendario_Mes.buttonSetMonth.show()
        self.tabs.calendario_Mes.showYear.show()
        self.tabs.calendario_Mes.buttonMonthBefore.setDisabled(False)
        self.tabs.calendario_Mes.buttonNextMonth.setDisabled(False)
        
    def setTodayWeek(self):
        self.semana = 0
        self.plotWeek('change')
        self.checkCompromissos()
        
        self.tabs.semana.spinDays.hide()
        self.tabs.semana.comboBoxMonths.hide()
        self.tabs.semana.spinYears.hide()
        self.tabs.semana.buttonToday.hide()
        self.tabs.semana.buttonSet_OK.hide()
        self.tabs.semana.buttonSetData.show()
        self.tabs.semana.buttonWeekBefore.setDisabled(False)
        self.tabs.semana.buttonNextWeek.setDisabled(False)
    
    def plotMonth(self, action, year=1500, month=1):
        today = QDate.currentDate()
        first = today.addDays( -(today.day()-1) )
        
        if action == 'change':
            newFirst = first.addMonths(self.mes)
            self.tabs.calendario_Mes.spinYears.setValue(newFirst.year())
        elif action == 'SET':
            newFirst = QDate(year, month, 1)
            self.mes = ( newFirst.month()-today.month() ) + ( (newFirst.year()-today.year())*12 )
        
        if newFirst.dayOfWeek() <= 6:
            begin = newFirst.addDays( -newFirst.dayOfWeek() )
        else:
            begin = newFirst.addDays(-7)
            
        for i in range(1,43):
            getattr(self.tabs.calendario_Mes,'label{0}'.format(i)).setText(' {0}'.format(begin.day() ) + '\n'*4 )
            getattr(self.tabs.calendario_Mes,'label{0}'.format(i)).setAtributos(begin)
            
            if begin.month() != newFirst.month():
                getattr(self.tabs.calendario_Mes,'label{0}'.format(i)).setStyleSheet('color: gray')
            else:
                getattr(self.tabs.calendario_Mes,'label{0}'.format(i)).setStyleSheet('color: black')
            
            begin = begin.addDays(1)
        
        self.tabs.calendario_Mes.buttonSetMonth.setText('{0}'.format(QDate.longMonthName(newFirst.month()).upper()))
        self.tabs.calendario_Mes.showYear.setText('{0}'.format(newFirst.year()))
    
    def plotWeek(self, action, year=1500, month=1, day=1):
        today = QDate.currentDate()
        
        if action == 'change':
            newFirst = today.addDays(7*self.semana)
            self.tabs.semana.spinYears.setValue(newFirst.year())
        elif action == 'SET':
            newFirst = QDate(year, month, day+1)
            days = today.daysTo(newFirst)
            weeks = days/7
            self.semana = weeks
        
        if newFirst.dayOfWeek() <= 6:
            begin = newFirst.addDays( -newFirst.dayOfWeek() )
        else:
            begin = newFirst.addDays(-7)
        
        for i in range(1,8):
            getattr(self.tabs.semana,'buttonDay{0}'.format(i)).setText('{0} {1}'.format(QDate.shortDayName(begin.dayOfWeek()).upper(),begin.day()))
            getattr(self.tabs.semana,'list{0}'.format(i)).setAtributos(begin)
            if begin.month() != newFirst.month():
                getattr(self.tabs.semana,'buttonDay{0}'.format(i)).setStyleSheet('color: gray')
            else:
                getattr(self.tabs.semana,'buttonDay{0}'.format(i)).setStyleSheet('color: black')
            
            begin = begin.addDays(1)
        
        self.tabs.semana.buttonSetData.setText('{0}'.format(QDate.longMonthName(newFirst.month()).upper()))
        self.tabs.semana.showYear.setText('{0}'.format(newFirst.year()))
    
    def addCompromisso(self):
        self.idxHistorico += 1
        if self.buttons.Title.text() == '':
            pass
        elif self.buttons.optionFixo.isChecked() == False and self.buttons.optionFlexivel.isChecked() == False:
            pass
        elif self.buttons.optionFlexivel.isChecked() == True and self.buttons.spinDuracao.time() == QTime(0,0):
            pass
        else:
            titulo = self.buttons.Title.text()
            descricao = self.buttons.Descricao.toPlainText()
            local = self.buttons.endereco.text()
            if self.buttons.optionFixo.isChecked():
                repetir = self.buttons.repetir.currentText()
                transporte = self.buttons.transporte.currentText()
                inicioDate = self.buttons.inicioDate.date()
                inicioTime = self.buttons.inicioTime.time()
                terminoDate = self.buttons.terminoDate.date()
                terminoTime = self.buttons.terminoTime.time()
                allDay = self.buttons.allDay.isChecked()
                
                if inicioDate.dayOfWeek() <= 6:
                    retangSemanaInicio = inicioDate.dayOfWeek()+1
                else:
                    retangSemanaInicio = 1
                    
                first = inicioDate.addDays( -(inicioDate.day()-1) )
                if first.dayOfWeek() <= 6:
                    beginInicio = first.addDays( -first.dayOfWeek() )
                else:
                    beginInicio = first.addDays(-7)
                    
                retangMesInicio = 0
                while beginInicio != inicioDate.addDays(1):
                    retangMesInicio += 1
                    beginInicio = beginInicio.addDays(1)
                    
                if allDay == False:
                    last = terminoDate.addDays( -(terminoDate.day()-1) )
                    if last.dayOfWeek() <= 6:
                        retangSemanaTermino = terminoDate.dayOfWeek()+1
                        beginTermino = last.addDays( -last.dayOfWeek() )
                    else:
                        retangSemanaTermino = 1
                        beginTermino = last.addDays(-7)
                    retangMesTermino = 0
                    while beginTermino != terminoDate.addDays(1):
                        retangMesTermino += 1
                        beginTermino = beginTermino.addDays(1)
                else:
                    retangSemanaTermino = None
                    retangMesTermino = None
                    inicioTime = None
                    terminoDate = None
                    terminoTime = None
                
                dayOrder = 0
                xInicio = 0
                if self.settedCompromissos == {}:
                    pass
                else:
                    for idx,compromisso in self.settedCompromissos.items():
                        if allDay == True:
                            if compromisso.inicioDate == inicioDate and compromisso.inicioDate == compromisso.terminoDate:
                                compromisso.dayOrder += 1
                            elif compromisso.terminoDate == inicioDate and compromisso.inicioDate != compromisso.terminoDate:
                                dayOrder += 1
                        elif compromisso.allDay == True:
                            dayOrder += 1
                        elif compromisso.inicioDate == inicioDate and compromisso.inicioDate == compromisso.terminoDate:
                            if inicioTime.secsTo(compromisso.inicioTime) < 0:
                                dayOrder += 1
                            else:
                                compromisso.dayOrder += 1
                            
                            if (compromisso.inicioTime < inicioTime < compromisso.terminoTime) or (compromisso.inicioTime < terminoTime < compromisso.terminoTime):
                                if xInicio <= compromisso.xInicio:
                                    xInicio = compromisso.xInicio + 70
                        
                        elif compromisso.inicioDate == inicioDate and compromisso.inicioDate != compromisso.terminoDate:
                            compromisso.dayOrder += 1
                        
                        elif compromisso.terminoDate == inicioDate and compromisso.inicioDate != compromisso.terminoDate:
                            dayOrder += 1
                
                newCompromisso = Compromisso(self.idxHistorico, titulo, descricao, local)
                newCompromisso.setFixo(repetir,transporte, inicioDate, inicioTime, terminoDate, terminoTime, xInicio, retangMesInicio, retangMesTermino, retangSemanaInicio, retangSemanaTermino, allDay, dayOrder)
                
                
            elif self.buttons.optionFlexivel.isChecked():
                prioridade = self.buttons.prioridade.currentText()
                duracao = self.buttons.spinDuracao.time()
                dataLimite = None
                timeDas = None
                timeAte = None
                segunda = 0
                terca = 0
                quarta = 0
                quinta = 0
                sexta = 0
                sabado = 0
                domingo = 0
                
                if self.buttons.dataLimiteCheck.isChecked():
                    dataLimite = self.buttons.dataLimite.date()
                    
                if self.buttons.restricaoTimeCheck.isChecked():
                    timeDas = self.buttons.restricaoTimeDas.time()
                    timeAte = self.buttons.restricaoTimeAte.time()
                        
                if self.buttons.restricaoDayOfWeekCheck.isChecked():
                    segunda = self.buttons.restricaoSeg.idx
                    terca = self.buttons.restricaoTer.idx
                    quarta = self.buttons.restricaoQua.idx
                    quinta = self.buttons.restricaoQui.idx
                    sexta = self.buttons.restricaoSex.idx
                    sabado = self.buttons.restricaoSab.idx
                    domingo = self.buttons.restricaoDom.idx
                
                middle = [segunda, terca, quarta, quinta, sexta, sabado, domingo]
                diasDaSemana = []
                for dia in range(1,8):
                    if middle[dia-1] == 0:
                        pass
                    else:
                        diasDaSemana += [dia]
                
                
                newCompromisso = Compromisso(self.idxHistorico, titulo, descricao, local)
                newCompromisso.setFlexivel(duracao, prioridade, dataLimite, timeDas, timeAte, diasDaSemana)
                yInicio,yTermino,xInicio,inicioDate,inicioTime,terminoDate,terminoTime,retangMesInicio,retangMesTermino,retangSemanaInicio,retangSemanaTermino,dayOrder,repetir,allDay = self.checkEspacoLivre(newCompromisso)
                newCompromisso.setTempConfig(yInicio, yTermino, xInicio, inicioDate, inicioTime, terminoDate, terminoTime, retangMesInicio, retangMesTermino, retangSemanaInicio, retangSemanaTermino, dayOrder, repetir, allDay)
                
            newCompromisso.setWin(self)
            newCompromisso.setFunc('self.win.tabs.setCurrentIndex(3)\nself.win.tabs.descricaoCompromissoModel.clear()\nnew = copy(self.listDescricao)\nsuper(QStandardItem, new).__init__()\nnew.setText(self.listDescricao.text())\nself.win.tabs.descricaoCompromissoModel.appendRow(new)\nself.win.tabs.certeza.indice = self.indice')
            self.settedCompromissos[self.idxHistorico] = newCompromisso
            self.buttons.hideOptions()
            self.checkCompromissos()
    
    def removeCompromisso(self):
        if self.tabs.certeza.indice == None:
            self.tabs.certeza.hide()
            self.tabs.nao.hide()
            self.tabs.delCompromisso.show()
        else:
            self.tabs.certeza.hide()
            self.tabs.nao.hide()
            self.tabs.delCompromisso.show()
            
            self.settedCompromissos.pop(self.tabs.certeza.indice)
            self.tabs.certeza.indice = None
            self.tabs.descricaoCompromissoModel.clear()
            self.checkCompromissos()
    
    def editarCompromisso(self):
        if self.tabs.certeza.indice != None:
            repetir = ['Nunca','Todo Dia','Toda Semana','Todo Mês']
            transporte = ['A Pé','Bicicleta','Carro','Moto','Metrô','Ônibus']
            self.buttons.hideOptions()
            self.buttons.showOptions()
            if self.settedCompromissos[self.tabs.certeza.indice].tipo == 'FIXO':
                self.buttons.optionFixo.click()
                self.buttons.Title.setText(self.settedCompromissos[self.tabs.certeza.indice].titulo)
                self.buttons.endereco.setText(self.settedCompromissos[self.tabs.certeza.indice].endereco)
                self.buttons.repetir.setCurrentIndex(repetir.index(self.settedCompromissos[self.tabs.certeza.indice].repetir))
                self.buttons.transporte.setCurrentIndex(transporte.index(self.settedCompromissos[self.tabs.certeza.indice].transporte))
                if self.settedCompromissos[self.tabs.certeza.indice].allDay == True:
                    self.buttons.allDay.click()
                    self.buttons.inicioDate.setDate(self.settedCompromissos[self.tabs.certeza.indice].inicioDate)
                else:
                    self.buttons.inicioDate.setDate(self.settedCompromissos[self.tabs.certeza.indice].inicioDate)
                    self.buttons.inicioTime.setTime(self.settedCompromissos[self.tabs.certeza.indice].inicioTime)
                    self.buttons.terminoDate.setDate(self.settedCompromissos[self.tabs.certeza.indice].terminoDate)
                    self.buttons.terminoTime.setTime(self.settedCompromissos[self.tabs.certeza.indice].terminoTime)
                self.buttons.Descricao.setFocus()
                self.buttons.Descricao.setText(self.settedCompromissos[self.tabs.certeza.indice].descricao)
            self.tabs.certeza.click()
    
    def checkCompromissos(self):
        today = QDate.currentDate()
        first = today.addMonths(self.mes)
        first2 = today.addDays(7*self.semana)
        currentDay = today.addDays(self.dia)
        self.model1 = QStandardItemModel()
        self.model2 = QStandardItemModel()
        self.model3 = QStandardItemModel()
        self.model4 = QStandardItemModel()
        self.model5 = QStandardItemModel()
        self.model6 = QStandardItemModel()
        self.model7 = QStandardItemModel()
        
        squaresPerRetang = dict()
        for i in range(1,43):
            squaresPerRetang[i] = 0
        
        daysOfWeek = dict()
        for j in range(1,8):
            daysOfWeek[j] = [None]*50
        
        for k in reversed(range(self.tabs.dia.layoutMostraCompromissosBackGround.count())):
            self.tabs.dia.layoutMostraCompromissosBackGround.itemAt(k).widget().setParent(None)
        self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(QWidget(), 1000,0,1,1)
        
        for k in self.tabs.dia.scene.items():
            self.tabs.dia.scene.removeItem(k)
        
        for linha in range(50):
            self.tabs.dia.scene.addLine(QLineF( QLine( QPoint(0,(linha*29)+10),QPoint(725,(linha*29)+10) ) ) )
# CHECK MÊS_____________________________________________________________________________________________________________________________________________________________________
        for idx,compromisso in self.settedCompromissos.items():
            # PROCESSO PARA MESMO MÊS INICIO_______________________________________________________________________________________________________________________________________________
            if compromisso.inicioDate.month() == first.month() and compromisso.inicioDate.year() == first.year():
                if compromisso.allDay == True:
                    squaresPerRetang[compromisso.retangMesInicio] += 1
                    
                    if compromisso.repetir == 'Nunca': 
                        pass
                    elif compromisso.repetir == 'Todo Dia':
                        for dia in range(1,43):
                            if dia > compromisso.retangMesTermino:
                                squaresPerRetang[dia] += 1
                    elif compromisso.repetir == 'Toda Semana':
                        if compromisso.retangMesInicio == compromisso.retangMesTermino:
                            for dia2 in range(1,43):
                                if dia2 > compromisso.retangMesTermino and (dia2-compromisso.retangMesTermino)%7 == 0:
                                    squaresPerRetang[dia2] += 1
                        else:
                            for dia3 in range(1,43):
                                if (dia3 > compromisso.retangMesTermino and (dia3-compromisso.retangMesTermino)%7 == 0) or (dia3 > compromisso.retangMesInicio and (dia3-compromisso.retangMesInicio)%7 == 0):
                                    squaresPerRetang[dia3] += 1
                    elif compromisso.repetir == 'Todo Mês':
                        pass
                # PROCESSO PARA MESMO MÊS TÉRMINO
                elif compromisso.terminoDate.month() == first.month() and compromisso.terminoDate.year() == first.year():
                    if compromisso.retangMesInicio == compromisso.retangMesTermino:
                        squaresPerRetang[compromisso.retangMesInicio] += 1
                    else:
                        squaresPerRetang[compromisso.retangMesInicio] += 1
                        squaresPerRetang[compromisso.retangMesTermino] += 1
                    
                    if compromisso.repetir == 'Nunca': 
                        pass
                    elif compromisso.repetir == 'Todo Dia':
                        for dia in range(1,43):
                            if dia > compromisso.retangMesTermino:
                                squaresPerRetang[dia] += 1
                    elif compromisso.repetir == 'Toda Semana':
                        if compromisso.retangMesInicio == compromisso.retangMesTermino:
                            for dia2 in range(1,43):
                                if dia2 > compromisso.retangMesTermino and (dia2-compromisso.retangMesTermino)%7 == 0:
                                    squaresPerRetang[dia2] += 1
                        else:
                            for dia3 in range(1,43):
                                if (dia3 > compromisso.retangMesTermino and (dia3-compromisso.retangMesTermino)%7 == 0) or (dia3 > compromisso.retangMesInicio and (dia3-compromisso.retangMesInicio)%7 == 0):
                                    squaresPerRetang[dia3] += 1
                    elif compromisso.repetir == 'Todo Mês':
                        pass
                # PROCESSO PARA MÊS TÉRMINO DIFERENTE___________________________________________________________________________________________________________________________
                elif compromisso.terminoDate.month() != first.month() and compromisso.terminoDate.year() == first.year():
                    pass
# CHECK MES_____________________________________________________________________________________________________________________________________________________________________
         
# CHECK SEMANA__________________________________________________________________________________________________________________________________________________________________
            if compromisso.inicioDate.weekNumber() == first2.weekNumber() and compromisso.inicioDate.month() == first.month() and compromisso.inicioDate.year() == first.year():
                if compromisso.retangSemanaInicio != 1:
                   daysOfWeek[compromisso.retangSemanaInicio][compromisso.dayOrder] = compromisso
                else:
                   getattr(self.tabs.semana, 'list{0}'.format(compromisso.retangSemanaInicio)).setModel(getattr(self, 'model{0}'.format(compromisso.retangSemanaInicio)))
            elif compromisso.inicioDate.weekNumber() != first2.weekNumber() and compromisso.inicioDate.month() == first.month() and compromisso.inicioDate.year() == first.year():
                if getattr(self.tabs.semana, 'list{0}'.format(compromisso.retangSemanaInicio)).data == compromisso.inicioDate:
                   daysOfWeek[compromisso.retangSemanaInicio][compromisso.dayOrder] = compromisso
                else:
                   getattr(self.tabs.semana, 'list{0}'.format(compromisso.retangSemanaInicio)).setModel(getattr(self, 'model{0}'.format(compromisso.retangSemanaInicio)))
# CHECK SEMANA__________________________________________________________________________________________________________________________________________________________________

# CHECK DIA_____________________________________________________________________________________________________________________________________________________________________
            if compromisso.allDay == True:
                if compromisso.inicioDate == currentDay:
                    if compromisso.retangDia in self.tabs.dia.scene.items():
                        self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                    else:
                        self.tabs.dia.scene.addItem(compromisso.retangDia)
                        compromisso.retangDia.setFlag(QGraphicsItem.ItemStacksBehindParent)
                        self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                else:
                    if compromisso.repetir == 'Nunca':
                        if compromisso.retangDia in self.tabs.dia.scene.items():
                            self.tabs.dia.scene.removeItem(compromisso.retangDia)
                    
                    elif compromisso.repetir == 'Todo Dia':
                        if compromisso.retangDia in self.tabs.dia.scene.items():
                            self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                        else:
                            self.tabs.dia.scene.addItem(compromisso.retangDia)
                            self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                    
                    elif compromisso.repetir == 'Toda Semana':
                        if compromisso.inicioDate.dayOfWeek() == currentDay.dayOfWeek():
                            if compromisso.retangDia in self.tabs.dia.scene.items():
                                self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                            else:
                                self.tabs.dia.scene.addItem(compromisso.retangDia)
                                self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                        else:
                            if compromisso.retangDia in self.tabs.dia.scene.items():
                                self.tabs.dia.scene.removeItem(compromisso.retangDia)
                    
                    elif compromisso.repetir == 'Todo Mês':
                        if compromisso.inicioDate.day() == currentDay.day():
                            if compromisso.retangDia in self.tabs.dia.scene.items():
                                self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                            else:
                                self.tabs.dia.scene.addItem(compromisso.retangDia)
                                self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                        else:
                            if compromisso.retangDia in self.tabs.dia.scene.items():
                                self.tabs.dia.scene.removeItem(compromisso.retangDia)
            
            elif compromisso.inicioDate == currentDay and compromisso.terminoDate == currentDay:
                if compromisso.retangDia in self.tabs.dia.scene.items():
                    self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                else:
                    self.tabs.dia.scene.addItem(compromisso.retangDia)
                    self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                
            elif compromisso.inicioDate != currentDay and compromisso.terminoDate == currentDay:
                if compromisso.retangDiaTermino in self.tabs.dia.scene.items():
                    self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrderTermino,0,1,1)
                else:
                    self.tabs.dia.scene.addItem(compromisso.retangDiaTermino)
                    self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrderTermino,0,1,1)
                
                if compromisso.repetir == 'Todo Dia':
                    if compromisso.retangDiaInicio in self.tabs.dia.scene.items():
                        pass
                    else:
                        self.tabs.dia.scene.addItem(compromisso.retangDiaInicio)
                else:
                    if compromisso.retangDiaInicio in self.tabs.dia.scene.items():
                        self.tabs.dia.scene.removeItem(compromisso.retangDiaInicio)
            
            elif compromisso.inicioDate == currentDay and compromisso.terminoDate != currentDay:
                if compromisso.retangDiaInicio in self.tabs.dia.scene.items():
                    self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                else:
                    self.tabs.dia.scene.addItem(compromisso.retangDiaInicio)
                    self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                
                if compromisso.repetir == 'Todo Dia':
                    if compromisso.retangDiaTermino in self.tabs.dia.scene.items():
                        pass
                    else:
                        self.tabs.dia.scene.addItem(compromisso.retangDiaTermino)
                else:
                    if compromisso.retangDiaTermino in self.tabs.dia.scene.items():
                        self.tabs.dia.scene.removeItem(compromisso.retangDiaTermino)
            
            else:
                if compromisso.inicioDate.day() == compromisso.terminoDate.day():
                    if compromisso.repetir == 'Nunca':
                        if compromisso.retangDia in self.tabs.dia.scene.items():
                            self.tabs.dia.scene.removeItem(compromisso.retangDia)
                    
                    elif compromisso.repetir == 'Todo Dia':
                        if compromisso.retangDia in self.tabs.dia.scene.items():
                            self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                        else:
                            self.tabs.dia.scene.addItem(compromisso.retangDia)
                            self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                    
                    elif compromisso.repetir == 'Toda Semana':
                        if compromisso.inicioDate.dayOfWeek() == currentDay.dayOfWeek():
                            if compromisso.retangDia in self.tabs.dia.scene.items():
                                self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                            else:
                                self.tabs.dia.scene.addItem(compromisso.retangDia)
                                self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                        else:
                            if compromisso.retangDia in self.tabs.dia.scene.items():
                                self.tabs.dia.scene.removeItem(compromisso.retangDia)
                    
                    elif compromisso.repetir == 'Todo Mês':
                        if compromisso.inicioDate.day() == currentDay.day():
                            if compromisso.retangDia in self.tabs.dia.scene.items():
                                self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                            else:
                                self.tabs.dia.scene.addItem(compromisso.retangDia)
                                self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                        else:
                            if compromisso.retangDia in self.tabs.dia.scene.items():
                                self.tabs.dia.scene.removeItem(compromisso.retangDia)
                else:
                    if compromisso.repetir == 'Nunca':
                        if compromisso.retangDiaInicio in self.tabs.dia.scene.items():
                            self.tabs.dia.scene.removeItem(compromisso.retangDiaInicio)
                        if compromisso.retangDiaTermino in self.tabs.dia.scene.items():
                            self.tabs.dia.scene.removeItem(compromisso.retangDiaTermino)
                    
                    elif compromisso.repetir == 'Todo Dia':
                        if compromisso.retangDiaInicio in self.tabs.dia.scene.items():
                            self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                            if compromisso.retangDiaTermino in self.tabs.dia.scene.items():
                                pass
                            else:
                                self.tabs.dia.scene.addItem(compromisso.retangDiaTermino)
                        else:
                            self.tabs.dia.scene.addItem(compromisso.retangDiaInicio)
                            self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                            if compromisso.retangDiaTermino in self.tabs.dia.scene.items():
                                pass
                            else:
                                self.tabs.dia.scene.addItem(compromisso.retangDiaTermino)
                                
                    elif compromisso.repetir == 'Toda Semana':
                        if compromisso.inicioDate.dayOfWeek() == currentDay.dayOfWeek() and compromisso.terminoDate.dayOfWeek() != currentDay.dayOfWeek():
                            if compromisso.retangDiaInicio in self.tabs.dia.scene.items():
                                self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                            else:
                                self.tabs.dia.scene.addItem(compromisso.retangDiaInicio)
                                self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                        
                        if compromisso.retangDiaTermino in self.tabs.dia.scene.items():
                            self.tabs.dia.scene.removeItem(compromisso.retangDiaTermino)
                        
                        elif compromisso.inicioDate.dayOfWeek() != currentDay.dayOfWeek() and compromisso.terminoDate.dayOfWeek() == currentDay.dayOfWeek():
                            if compromisso.retangDiaTermino in self.tabs.dia.scene.items():
                                self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                            else:                                        
                                self.tabs.dia.scene.addItem(compromisso.retangDiaTermino)
                                self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                                
                            if compromisso.retangDiaInicio in self.tabs.dia.scene.items():
                                self.tabs.dia.scene.removeItem(compromisso.retangDiaInicio)
                        else:
                            if compromisso.retangDiaInicio in self.tabs.dia.scene.items():
                                self.tabs.dia.scene.removeItem(compromisso.retangDiaInicio)
                            if compromisso.retangDiaTermino in self.tabs.dia.scene.items():
                                self.tabs.dia.scene.removeItem(compromisso.retangDiaTermino)
                    
                    elif compromisso.repetir == 'Todo Mês':
                        if compromisso.inicioDate.day() == currentDay.day():
                            if compromisso.retangDiaInicio in self.tabs.dia.scene.items():
                                self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                            else:
                                self.tabs.dia.scene.addItem(compromisso.retangDiaInicio)
                                self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                        elif compromisso.terminoDate.dayOfWeek() == currentDay.dayOfWeek():
                            if compromisso.retangDiaTermino in self.tabs.dia.scene.items():
                                self.tabs.dia.layoutMostraCompromissosBackGround.addWidget(compromisso.buttonCompromisso, compromisso.dayOrder,0,1,1)
                            else:                                        
                                self.tabs.dia.scene.addItem(compromisso.retangDiaTermino)
                        else:
                            if compromisso.retangDiaInicio in self.tabs.dia.scene.items():
                                self.tabs.dia.scene.removeItem(compromisso.retangDiaInicio)
                            if compromisso.retangDiaTermino in self.tabs.dia.scene.items():
                                self.tabs.dia.scene.removeItem(compromisso.retangDiaTermino)
# CHECK DIA_____________________________________________________________________________________________________________________________________________________________________            
        
        for retang,num in squaresPerRetang.items():
            if num == 0:
                getattr(self.tabs.calendario_Mes,'graphic{0}'.format(retang)).setLayoutMes('remove')
            else:
                getattr(self.tabs.calendario_Mes,'graphic{0}'.format(retang)).setLayoutMes('add',num)
        
        for retang2,listaCompromissos in daysOfWeek.items():
            iterator = iter(listaCompromissos)
            if all(None == rest for rest in iterator) == True:
                getattr(self.tabs.semana, 'list{0}'.format(retang2)).setModel(getattr(self, 'model{0}'.format(retang2)))
            else:
                for compromisso2 in listaCompromissos:
                    if compromisso2 == None:
                        pass
                    else:
                        new = copy(compromisso2.listTabSemana)
                        super(QStandardItem, new).__init__()
                        new.setText(compromisso2.listTabSemana.text())
                        
                        getattr(self, 'model{0}'.format(compromisso2.retangSemanaInicio)).appendRow(new)
                        getattr(self.tabs.semana, 'list{0}'.format(compromisso2.retangSemanaInicio)).setModel(getattr(self, 'model{0}'.format(compromisso2.retangSemanaInicio)))
    
    def checkEspacoLivre(self, newCompromisso):
        today = QDate.currentDate()
        begin = QDate.currentDate()
        blocos = dict()
        lacunas = dict()
        alternativas = dict()
        
        if newCompromisso.dataLimite == None:
            while begin != today.addDays(30):
                if begin.dayOfWeek() in newCompromisso.diasDaSemana:
                    begin = begin.addDays(1)
                else:
                    blocos['{0}/{1}/{2}'.format(begin.day(), begin.month(), begin.year())] = [None]*self.idxHistorico
                    lacunas['{0}/{1}/{2}'.format(begin.day(), begin.month(), begin.year())] = []
                    begin = begin.addDays(1)
        else:
            while begin != newCompromisso.dataLimite:
                if begin.dayOfWeek() in newCompromisso.diasDaSemana:
                    begin = begin.addDays(1)
                else:
                    blocos['{0}/{1}/{2}'.format(begin.day(), begin.month(), begin.year())] = [None]*self.idxHistorico
                    lacunas['{0}/{1}/{2}'.format(begin.day(), begin.month(), begin.year())] = []
                    begin = begin.addDays(1)
                
        for indice,comp in self.settedCompromissos.items():
            if newCompromisso.dataLimite == None:
                if comp.inicioDate.dayOfWeek() not in newCompromisso.diasDaSemana:
                    if comp.allDay == True:
                        pass
                    elif comp.inicioDate == comp.terminoDate:
                        if comp.endereco != None and newCompromisso.endereco != None:
                            if comp.transporte == 'A Pé':
                                tempoViagem = self.calculaTempoViagem(comp.endereco, newCompromisso.endereco, 'walking')
                            elif comp.transporte == 'Bicicleta':
                                tempoViagem = self.calculaTempoViagem(comp.endereco, newCompromisso.endereco, 'bicycle')
                            elif comp.transporte == 'Moto':
                                if abs(comp.inicioTime.secsTo(QTime(12,0))) < 3600:
                                    tempoViagem = self.calculaTempoViagem(comp.endereco, newCompromisso.endereco, 'driving')
                                else:
                                    tempoViagem = self.calculaTempoViagem(comp.endereco, newCompromisso.endereco, 'driving')/2
                            elif comp.transporte in ('Carro','Ônibus'):
                                if abs(comp.inicioTime.secsTo(QTime(12,0))) < 3600:
                                    tempoViagem = self.calculaTempoViagem(comp.endereco, newCompromisso.endereco, 'driving')*2
                                else:
                                    tempoViagem = self.calculaTempoViagem(comp.endereco, newCompromisso.endereco, 'driving')
                            elif comp.transporte == 'Metrô':
                                tempoViagem = self.calculaTempoViagem(comp.endereco, newCompromisso.endereco, 'driving') + 1200
                        else:
                            tempoViagem = 1200
                        
                        if (comp.yInicio-(tempoViagem/62.06896551724138)) > 0 or (comp.yTermino+(tempoViagem/62.06896551724138)) < 1441:
                            blocos['{0}/{1}/{2}'.format(comp.inicioDate.day(), comp.inicioDate.month(), comp.inicioDate.year())][comp.dayOrder] = [(comp.yInicio-(tempoViagem/62.06896551724138)), (comp.yTermino+(tempoViagem/62.06896551724138))]
                        elif (comp.yInicio-(tempoViagem/62.06896551724138)) < 0:
                            dayBefore = comp.inicioDate.addDays(-1)
                            blocos['{0}/{1}/{2}'.format(dayBefore.day(), dayBefore.month(), dayBefore.year())] += [1441-((tempoViagem/62.06896551724138)-comp.yInicio), 1441]
                            blocos['{0}/{1}/{2}'.format(comp.inicioDate.day(), comp.inicioDate.month(), comp.inicioDate.year())][comp.dayOrder] = [0, (comp.yTermino+(tempoViagem/62.06896551724138))]
                        elif (comp.yTermino+(tempoViagem/62.06896551724138)) > 1441:
                            nextDay = comp.inicioDate.addDays(1)
                            blocos['{0}/{1}/{2}'.format(nextDay.day(), nextDay.month(), nextDay.year())] += [0,comp.yTermino + (tempoViagem/62.06896551724138)-1441]
                            blocos['{0}/{1}/{2}'.format(comp.inicioDate.day(), comp.inicioDate.month(), comp.inicioDate.year())][comp.dayOrder] = [(comp.yInicio-(tempoViagem/62.06896551724138)),1441]
                    else:
                        if comp.endereco != None and newCompromisso.endereco != None:
                            tempoViagem = self.calculaTempoViagem(comp.endereco, newCompromisso.endereco)
                        else:
                            tempoViagem = 1200
                        blocos['{0}/{1}/{2}'.format(comp.inicioDate.day(), comp.inicioDate.month(), comp.inicioDate.year())][comp.dayOrder] = [comp.yInicio-(tempoViagem/62.06896551724138), 1441]
                        blocos['{0}/{1}/{2}'.format(comp.terminoDate.day(), comp.terminoDate.month(), comp.terminoDate.year())][comp.dayOrder] = [0, comp.yTermino+(tempoViagem/62.06896551724138)]
            else:
                if comp.inicioDate.daysTo(newCompromisso.dataLimite) > 0:
                    if comp.inicioDate.dayOfWeek not in newCompromisso.diasDaSemana:
                        if comp.allDay == True:
                            pass
                        elif comp.inicioDate == comp.terminoDate:
                            if comp.endereco != None and newCompromisso.endereco != None:
                                if comp.transporte == 'A Pé':
                                    tempoViagem = self.calculaTempoViagem(comp.endereco, newCompromisso.endereco, 'walking')
                                elif comp.transporte == 'Bicicleta':
                                    tempoViagem = self.calculaTempoViagem(comp.endereco, newCompromisso.endereco, 'bicycle')
                                elif comp.transporte == 'Moto':
                                    if abs(comp.inicioTime.secsTo(QTime(12,00))) < 3600:
                                        tempoViagem = self.calculaTempoViagem(comp.endereco, newCompromisso.endereco, 'driving')
                                    else:
                                        tempoViagem = self.calculaTempoViagem(comp.endereco, newCompromisso.endereco, 'driving')/2
                                elif comp.transporte in ('Carro','Ônibus'):
                                    if abs(comp.inicioTime.secsTo(QTime(12,00))) < 3600:
                                        tempoViagem = self.calculaTempoViagem(comp.endereco, newCompromisso.endereco, 'driving')*2
                                    else:
                                        tempoViagem = self.calculaTempoViagem(comp.endereco, newCompromisso.endereco, 'driving')
                                elif comp.transporte == 'Metrô':
                                    tempoViagem = self.calculaTempoViagem(comp.endereco, newCompromisso.endereco, 'driving') + 1200
                            else:
                                tempoViagem = 1200
                            
                            if (comp.yInicio-(tempoViagem/62.06896551724138)) > 0 or (comp.yTermino+(tempoViagem/62.06896551724138)) < 1441:
                                blocos['{0}/{1}/{2}'.format(comp.inicioDate.day(), comp.inicioDate.month(), comp.inicioDate.year())][comp.dayOrder] = [(comp.yInicio-(tempoViagem/62.06896551724138)), (comp.yTermino+(tempoViagem/62.06896551724138))]
                            elif (comp.yInicio-(tempoViagem/62.06896551724138)) < 0:
                                dayBefore = comp.inicioDate.addDays(-1)
                                blocos['{0}/{1}/{2}'.format(dayBefore.day(), dayBefore.month(), dayBefore.year())] += [1441-((tempoViagem/62.06896551724138)-comp.yInicio), 1441]
                                blocos['{0}/{1}/{2}'.format(comp.inicioDate.day(), comp.inicioDate.month(), comp.inicioDate.year())][comp.dayOrder] = [0, (comp.yTermino+(tempoViagem/62.06896551724138))]
                            elif (comp.yTermino+(tempoViagem/62.06896551724138)) > 1441:
                                nextDay = comp.inicioDate.addDays(1)
                                blocos['{0}/{1}/{2}'.format(nextDay.day(), nextDay.month(), nextDay.year())] += [0,comp.yTermino + (tempoViagem/62.06896551724138)-1441]
                                blocos['{0}/{1}/{2}'.format(comp.inicioDate.day(), comp.inicioDate.month(), comp.inicioDate.year())][comp.dayOrder] = [(comp.yInicio-(tempoViagem/62.06896551724138)),1441]
                        else:
                            if comp.endereco != None and newCompromisso.endereco != None:
                                tempoViagem = self.calculaTempoViagem(comp.endereco, newCompromisso.endereco)
                            else:
                                tempoViagem = 1200
                            blocos['{0}/{1}/{2}'.format(comp.inicioDate.day(), comp.inicioDate.month(), comp.inicioDate.year())][comp.dayOrder] = [comp.yInicio-(tempoViagem/62.06896551724138), 1441]
                            blocos['{0}/{1}/{2}'.format(comp.terminoDate.day(), comp.terminoDate.month(), comp.terminoDate.year())][comp.dayOrder] = [0, comp.yTermino+(tempoViagem/62.06896551724138)]
        
        for data,lista in blocos.items():
            yInicio = 0
            yTermino = 0
            for coords in lista:
                if coords == None:
                    yTermino = 1441
                    lacunas[data] += [[yInicio, yTermino]]
                    break
                else:
                    if coords[0] != 0 and coords[1] != 1441:
                        yTermino = coords[0]
                        lacunas[data] += [[yInicio,yTermino]]
                        yInicio = coords[1]
                    elif coords[0] == 0:
                        yInicio = coords[1]
                    elif coords[1] == 1441:
                        yTermino = coords[0]
                        lacunas[data] += [[yInicio,yTermino]]
                        break
        
        for data3,lista3 in lacunas.items():
            alternativas[data3] = []
            for lacuna in lista3:
                if (lacuna[1]-lacuna[0]) > newCompromisso.duracao:
                    alternativas[data3] += [lacuna]
        
        data4 = choice(list(alternativas.keys()))
        lista4 = alternativas[data4]
        lacuna4 = choice(lista4)
        
        yInicio = ((lacuna[1]-lacuna4[0])/2)-(newCompromisso.duracao/2)
        yTermino = yInicio + newCompromisso.duracao
        
        inicioTimeS = (yInicio * 62.06896551724138)
        inicioTimeH = (inicioTimeS-(inicioTimeS%3600))/3600
        inicioTimeM = ((inicioTimeS%3600)-((inicioTimeS%3600)%60))/60
        inicioTime = QTime(inicioTimeH, inicioTimeM)
        
        terminoTimeS = (yTermino * 62.06896551724138)
        terminoTimeH = (terminoTimeS-(terminoTimeS%3600))/3600
        terminoTimeM = ((terminoTimeS%3600)-((terminoTimeS%3600)%60))/60
        terminoTime = QTime(terminoTimeH, terminoTimeM)
        
        data4 = data4.split('/')
        inicioDate = QDate(int(data4[2]), int(data4[1]), int(data4[0]))
        terminoDate = inicioDate
        
        allDay = False
        repetir = 'Nunca'
        
        if inicioDate.dayOfWeek() <= 6:
            retangSemanaInicio = inicioDate.dayOfWeek()+1
        else:
            retangSemanaInicio = 1
            
        first = inicioDate.addDays( -(inicioDate.day()-1) )
        if first.dayOfWeek() <= 6:
            beginInicio = first.addDays( -first.dayOfWeek() )
        else:
            beginInicio = first.addDays(-7)
            
        retangMesInicio = 0
        while beginInicio != inicioDate.addDays(1):
            retangMesInicio += 1
            beginInicio = beginInicio.addDays(1)
            
        if allDay == False:
            last = terminoDate.addDays( -(terminoDate.day()-1) )
            if last.dayOfWeek() <= 6:
                retangSemanaTermino = terminoDate.dayOfWeek()+1
                beginTermino = last.addDays( -last.dayOfWeek() )
            else:
                retangSemanaTermino = 1
                beginTermino = last.addDays(-7)
            retangMesTermino = 0
            while beginTermino != terminoDate.addDays(1):
                retangMesTermino += 1
                beginTermino = beginTermino.addDays(1)
        
        dayOrder = 0
        xInicio = 0
        if self.settedCompromissos == {}:
            pass
        else:
            for idx,compromisso in self.settedCompromissos.items():
                if allDay == True:
                    if compromisso.inicioDate == inicioDate and compromisso.inicioDate == compromisso.terminoDate:
                        compromisso.dayOrder += 1
                    elif compromisso.terminoDate == inicioDate and compromisso.inicioDate != compromisso.terminoDate:
                        dayOrder += 1
                elif compromisso.allDay == True:
                    dayOrder += 1
                elif compromisso.inicioDate == inicioDate and compromisso.inicioDate == compromisso.terminoDate:
                    if inicioTime.secsTo(compromisso.inicioTime) < 0:
                        dayOrder += 1
                    else:
                        compromisso.dayOrder += 1
                    
                    if (compromisso.inicioTime < inicioTime < compromisso.terminoTime) or (compromisso.inicioTime < terminoTime < compromisso.terminoTime):
                        if xInicio <= compromisso.xInicio:
                            xInicio = compromisso.xInicio + 70
                
                elif compromisso.inicioDate == inicioDate and compromisso.inicioDate != compromisso.terminoDate:
                    compromisso.dayOrder += 1
                
                elif compromisso.terminoDate == inicioDate and compromisso.inicioDate != compromisso.terminoDate:
                    dayOrder += 1
        return yInicio, yTermino, xInicio, inicioDate, inicioTime, terminoDate, terminoTime, retangMesInicio, retangMesTermino, retangSemanaInicio, retangSemanaTermino, dayOrder, repetir, allDay
    
    def calculaTempoViagem(self, origem, destino, transporte):
        try:
            orig_lat,orig_lng = self.get_coordinates(origem)
            dest_lat,dest_lng = self.get_coordinates(destino)
            
            url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0},{1}&destinations={2},{3}&mode={4}&language=en-EN&sensor=false".format(orig_lat,orig_lng,dest_lat,dest_lng,transporte)
            result= simplejson.load(urllib.request.urlopen(url))
            for key,value in result.items():
                if value == ['10060 None TO, Italy']:
                    return 1200
            driving_time = result['rows'][0]['elements'][0]['duration']['value']
            return driving_time
        except urllib.error.URLError:
            return 1200
    
    def get_coordinates(self,query, from_sensor=False):
        query = query.encode('utf-8')
        params = {
            'address': query,
            'sensor': "true" if from_sensor else "false"
        }
        url = googleGeocodeUrl + urllib.parse.urlencode(params)
        json_response = urllib.request.urlopen(url)
        response = simplejson.loads(json_response.read())
        if response['results']:
            location = response['results'][0]['geometry']['location']
            latitude, longitude = location['lat'], location['lng']
        else:
            latitude, longitude = None, None
        return latitude, longitude

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    for i in range(1,43):
        getattr(win.tabs.calendario_Mes, 'label{0}'.format(i)).setWin(win)
    for j in range(1,8):
        getattr(win.tabs.semana, 'list{0}'.format(j)).setWin(win)
    win.buttons.win = win
    win.buttons.setWin()
    win.show()
    app.exec_()