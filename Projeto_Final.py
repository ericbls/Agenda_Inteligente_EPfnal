import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Dia():
    def __init__(self):
        self.tabDayContent = QGraphicsView() #cria retângulo do dia na aba do mês
        self.tabWeekContent = QListView() #cria retângulo do dia na aba da semana
        self.tabMonthContent = QGraphicsView() #cria retângulo do dia na aba do dia
        
        
    def setCompromissoLayoutMes(self, action, num_compromissos=0):
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
            self.tabMonthContent.setScene(content)
        elif action == 'remove':
            content = QGraphicsScene()
            content.setSceneRect(QRectF(0,0,85,45) )
            self.tabMonthContent.setScene(content)
    def teste(self):
        print('Clicked')

class Semana():
    pass    

class Mes(QAbstractScrollArea):
    def __init__(self):
        super(Mes, self).__init__() # cria uma area principal que irá conter todos os elementos do calendário
        self.setDefault() # cria uma area menor com fundo cinza
        self.createLayoutMes() # cria os botões do calendário e adiciona os retângulos dos dias
        
    def createLayoutMes(self):
        layout_Mes = QGridLayout(self.main_widget) # cria um layout de grade para a area com fundo cinza
        
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
        
<<<<<<< HEAD
        self.showYear = QPushButton('{0}'.format(first.year()))
        self.showDom = QPushButton('Dom')
=======
        self.showYear = QPushButton('{0}'.format(first.year())) # cria botão para mostrar o ano exibido
        
        # cria botões para exibir os dias da semana
>>>>>>> origin/master
        self.showSeg = QPushButton('Seg')
        self.showTer = QPushButton('Ter')
        self.showQua = QPushButton('Qua')
        self.showQui = QPushButton('Qui')
        self.showSex = QPushButton('Sex')
        self.showSab = QPushButton('Sab')
<<<<<<< HEAD
=======
        self.showDom = QPushButton('Dom')
        
        # torna os botões no clicáveis
>>>>>>> origin/master
        self.showYear.setDisabled(True)
        self.showSeg.setDisabled(True)
        self.showTer.setDisabled(True)
        self.showQua.setDisabled(True)
        self.showQui.setDisabled(True)
        self.showSex.setDisabled(True)
        self.showSab.setDisabled(True)
        self.showDom.setDisabled(True)
        
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
        
        self.shownDays = dict() # cria dicionário para guardar as posições dos retângulos dos dias
        self.shownLabels = dict() # cria dicionário para guardar as posições das labels como os números dos dias
        
        for i in range(1,43):
            self.shownDays['{0}'.format(i)] = Dia() # cria um item cuja chave é o número do termo na grade e o valor é um objeto da classe Dia
            self.shownDays['{0}'.format(i)].tabMonthContent.resize(90,50) # redimensiona o retângulo do dia na aba do mês 
            self.shownLabels['{0}'.format(i)] = QLabel(' {0}'.format(begin.day() ) + '\n'*4 ) # cria um item cuja chave é o número do termo na grade e o valor é uma label com o número do dia
            
            # determina as cores dos números dos dias no calendário
            if begin.month() != today.month():
                self.shownLabels['{0}'.format(i)].setStyleSheet('color: gray') # dias que não pertençam ao mês exibido ficam com o número cinza
            else:
                self.shownLabels['{0}'.format(i)].setStyleSheet('color: black')
            
            
            # plota os retângulos dos dias e os números dos dias nas suas posições relativas no layout da area de fundo cinza
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
    
    def setDefault(self):
        self.main_widget = QWidget() # cria a area menor
        
        layout_ScrollArea = QVBoxLayout(self) # cria layout para a area principal
        layout_ScrollArea.addWidget(self.main_widget) # adiciona a area menor ao layout da area principal
        
        # define a cor do fundo da area menor como cinza
        stylesheet = \
            ".QWidget {\n" \
            + "border: 0px solid black;\n" \
            + "border-radius: 10px;\n" \
            + "background-color: rgb(200, 200, 200);\n" \
            + "}"
        self.main_widget.setStyleSheet(stylesheet)

        

class Tabs(QTabWidget):
    def __init__(self):
        super(Tabs, self).__init__() # cria area principal, capaz de receber abas
        self.setFixedSize(850,600) # define dimensões fixas para a area principal
        
        # cria tres abas 
        self.tab1 = QWidget(self)
        self.tab2 = QWidget(self)
        self.tab3 = QWidget(self)
        
        self.calendario_Mes = Mes() # cria um objeto da classe Mes()
        layout_tab1 = QVBoxLayout(self.tab1) # cria layout para a aba tab1
        layout_tab1.addWidget(self.calendario_Mes) # adiciona o calendário ao layout da aba tab1
        
        # adiciona as três abas à area principal
        self.addTab(self.tab1, 'Mês')
        self.addTab(self.tab2, 'Semana')
        self.addTab(self.tab3, 'Dia')

class BarOptions():
    def __init__(self):
        # cria os botões da barra de opções
        self.main_buttonIN = QPushButton('Adicionar Compromisso')
        self.main_buttonOUT = QPushButton('Cancelar')
        self.buttonPersonalInfo = QPushButton('Informações\n Pessoais')
        self.buttonConfig = QPushButton('Configurações')
        self.separator1 = QWidget()

        self.buttonDiario = QPushButton('Diário')
        
        self.buttonSemanal = QPushButton('Semanal')
        
        self.buttonMensal = QPushButton('Mensal')
        
        self.buttonUnico = QPushButton('Único')
        
        self.buttonFlexivel = QPushButton('Flexível')
        
        self.buttonOption_OUT = QPushButton('Voltar')
        self.buttonOption_OK = QPushButton('Ok')
        
        # cria barra para escrever o título do compromisso
        self.Title = QLineEdit()
        self.Title.setPlaceholderText('Título do compromisso')
        
        self.groupBoxOptions = QGroupBox('Tipo de compromisso') # cria uma area contornada para agrupar as opções de tipo de compromisso
        self.groupBoxUnico = QGroupBox('Único') # cria uma area contornada para agrupar os elementos da opção compromisso único
        
        # cria layout para groupBoxOptions e adiciona todas as opções de tipo de compromisso
        layout_groupBoxOptions = QVBoxLayout(self.groupBoxOptions)
        layout_groupBoxOptions.addWidget(self.buttonUnico)
        layout_groupBoxOptions.addWidget(self.buttonDiario)
        layout_groupBoxOptions.addWidget(self.buttonSemanal)
        layout_groupBoxOptions.addWidget(self.buttonMensal)
        layout_groupBoxOptions.addWidget(self.buttonFlexivel)
        
        
        # cria layout para groupBoxUnico e adiciona todos os elementos da opção compromisso único
        layout_groupBoxUnico = QGridLayout(self.groupBoxUnico)
        
        
        
        

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__() # cria a janela do aplicativo
        self.setWindowTitle('Agenda inteligente') # define o título da janela
        
        self.tabs = Tabs() # gera o conjunto de abas
        self.buttons = BarOptions() # gera a barra de opções
        self.mes = 0 # define uma referência para os mêses exibidos
        self.settedCompromissos = dict()
        
        
        layout_main_sub1 = QGridLayout() # cria layout para depositar a barra de opções
        layout_main_sub2 = QVBoxLayout() # cria layout para depositar o conjunto de abas
        layout_main = QGridLayout() # cria layout para a janela do aplicativo
        layout_main_sub1.SetFixedSize
        
        # adiciona ao layout da barra de opções os seus elementos
        layout_main_sub1.addWidget(self.buttons.main_buttonIN, 0,0,1,2)
        layout_main_sub1.addWidget(self.buttons.main_buttonOUT, 0,0,1,2)
        layout_main_sub1.addWidget(self.buttons.Title, 1,0,1,2)
        layout_main_sub1.addWidget(self.buttons.separator1, 1,0,1,2)
        layout_main_sub1.addWidget(self.buttons.groupBoxOptions,2,0,1,2)
        layout_main_sub1.addWidget(self.buttons.groupBoxUnico, 2,0,1,2)
        layout_main_sub1.addWidget(self.buttons.buttonOption_OUT, 3,0,1,1)
        layout_main_sub1.addWidget(self.buttons.buttonOption_OK, 3,1,1,1)
        layout_main_sub1.addWidget(self.buttons.buttonPersonalInfo, 4,0,1,2)
        layout_main_sub1.addWidget(self.buttons.buttonConfig, 5,0,1,2)
        
        # esconde os elementos que serão posteriormente chamados
        self.buttons.main_buttonOUT.hide()
        self.buttons.Title.hide()
        self.buttons.groupBoxOptions.hide()
        self.buttons.groupBoxUnico.hide()
        self.buttons.buttonOption_OUT.hide()
        self.buttons.buttonOption_OK.hide()
        
        
        layout_main_sub2.addWidget(self.tabs) # deposita o conjunto de abas ao seu layout 
        
        # adiciona os dois layouts sub ao layout da janela do aplicativo
        layout_main.addLayout(layout_main_sub1, 0,0,1,1)
        layout_main.addLayout(layout_main_sub2, 0,1,1,1)
        
        self.setLayout(layout_main) # adiciona layout à janela do aplicativo
        
        
        # conecta os botões do aplicativo a suas respectivas ações
        self.buttons.main_buttonIN.clicked.connect(self.showOptions)
        self.buttons.main_buttonOUT.clicked.connect(self.hideOptions)
        self.buttons.buttonUnico.clicked.connect(self.showUnico)
        self.buttons.buttonOption_OUT.clicked.connect(self.hideOption)
        
        self.tabs.calendario_Mes.buttonNextMonth.clicked.connect(self.nextMonth)
        self.tabs.calendario_Mes.buttonMonthBefore.clicked.connect(self.monthBefore)
        self.tabs.calendario_Mes.buttonSetMonth.clicked.connect(self.setMonth)
        self.tabs.calendario_Mes.buttonSet_OK.clicked.connect(self.setMonthOK)
        self.tabs.calendario_Mes.buttonToday.clicked.connect(self.setToday)
        
        
        # define as dimensões e a posição iniciais da janela do aplicativo
        self.resize(self.tabs.width(), self.tabs.height())
        self.centerOnScreen()
        
        
        for i in range(30):
            self.addCompromisso(QDate(2015,5,30))
        
        
    
    # move a janela para o centro da tela do monitor
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
        self.buttons.buttonOption_OUT.show()
        self.buttons.buttonOption_OK.show()
    
    def hideOptions(self):
        self.buttons.main_buttonOUT.hide()
        self.buttons.main_buttonIN.show()
        self.buttons.separator1.show()
        self.buttons.Title.hide()
        self.buttons.groupBoxOptions.hide()
        self.buttons.groupBoxUnico.hide()
        self.buttons.buttonOption_OUT.hide()
        self.buttons.buttonOption_OK.hide()
    
    def hideOption(self):
        self.buttons.groupBoxUnico.hide()
        self.buttons.groupBoxOptions.show()
        self.buttons.buttonOption_OUT.hide()
        self.buttons.buttonOption_OK.hide()
    
    def nextMonth(self):
        self.mes += 1
        self.plotMonth('change')
        self.checkCompromissos()
    
    def monthBefore(self):
        self.mes -= 1
        self.plotMonth('change')
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
    
    def setToday(self):
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
            self.tabs.calendario_Mes.shownLabels['{0}'.format(i)].setText(' {0}'.format(begin.day() ) + '\n'*4 )
            
            if begin.month() != newFirst.month():
                self.tabs.calendario_Mes.shownLabels['{0}'.format(i)].setStyleSheet('color: gray')
            else:
                self.tabs.calendario_Mes.shownLabels['{0}'.format(i)].setStyleSheet('color: black')
            
            begin = begin.addDays(1)
        
        self.tabs.calendario_Mes.buttonSetMonth.setText('{0}'.format(QDate.longMonthName(newFirst.month()).upper()))
        self.tabs.calendario_Mes.showYear.setText('{0}'.format(newFirst.year()))
    
    def addCompromisso(self, data):
        first = data.addDays( -(data.day()-1) )
        
        if first.dayOfWeek() <= 6:
            begin = first.addDays( -first.dayOfWeek() )
        else:
            begin = first.addDays(-7)
        
        retangulo_dia = 0
        while begin != data.addDays(1):
            retangulo_dia += 1
            begin = begin.addDays(1)
        
        if '{0}'.format(retangulo_dia) in self.settedCompromissos:
            self.settedCompromissos['{0}'.format(retangulo_dia)][1] += 1
        else:
            self.settedCompromissos['{0}'.format(retangulo_dia)] = [data,1]
        self.checkCompromissos()
    
    def removeCompromisso(self, data):
        first = data.addDays( -(data.day()-1) )
        
        if first.dayOfWeek() <= 6:
            begin = first.addDays( -first.dayOfWeek() )
        else:
            begin = first.addDays(-7)
        
        retangulo_dia = 0
        while begin != data.addDays(1):
            retangulo_dia += 1
            begin = begin.addDays(1)
        
        if self.settedCompromissos['{0}'.format(retangulo_dia)][1] == 1:
            self.settedCompromissos.pop('{0}'.format(retangulo_dia))
        else:
            self.settedCompromissos['{0}'.format(retangulo_dia)][1] -= 1
        
        self.checkCompromissos()
    
    def checkCompromissos(self):
        today = QDate.currentDate()
        first = today.addMonths(self.mes)
        
        for ret_dia,comp in self.settedCompromissos.items():
            if comp[0].month() == first.month() and comp[0].year() == first.year():
                self.tabs.calendario_Mes.shownDays[ret_dia].setCompromissoLayoutMes('add',comp[1])
            else:
                self.tabs.calendario_Mes.shownDays[ret_dia].setCompromissoLayoutMes('remove')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()