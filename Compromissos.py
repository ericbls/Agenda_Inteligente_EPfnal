from PyQt4.QtGui import *
from PyQt4.QtCore import *
from copy import *

class Compromisso():
    def __init__(self, idx, titulo, descricao, local):
        self.indice = idx
        self.titulo = titulo
        if descricao == 'Descrição':
            self.descricao = 'Sem descrição'
        else:
            self.descricao = descricao
        
        if local in ('Local.ex.:SP,São Paulo,Rua,n°',None,''):
            self.endereco = None
        else:
            self.endereco = local
        
        self.buttonCompromisso = QPushButton('{0}'.format(self.titulo))
        
        self.buttonCompromisso.clicked.connect(self.execFunc)
        
    def setFixo(self, repetir, transporte, inicioDate, inicioTime, terminoDate, terminoTime, xInicio, retangMesInicio, retangMesTermino, retangSemanaInicio, retangSemanaTermino, allDay, dayOrder):
        self.tipo = 'FIXO'
        self.repetir = repetir
        self.transporte = transporte
        self.inicioDate = inicioDate
        self.terminoDate = terminoDate
        self.inicioTime = inicioTime
        self.terminoTime = terminoTime
        self.retangMesInicio = retangMesInicio
        self.retangMesTermino = retangMesTermino
        self.retangSemanaInicio = retangSemanaInicio
        self.retangSemanaTermino = retangSemanaTermino
        self.allDay = allDay
        
        self.dayOrder = dayOrder
        if self.inicioDate != self.terminoDate:
            self.dayOrderTermino = 0
        
        if self.allDay == False:
            self.xInicio = xInicio
            if inicioDate == terminoDate:
                time = QTime(0,0)
                self.yInicio = 39 + time.secsTo(inicioTime)/62.06896551724138
                self.yTermino = 39 + time.secsTo(terminoTime)/62.06896551724138
                
                tipPolygon = QPolygonF()
                tipPolygon.append(QPointF(self.xInicio,self.yInicio))
                tipPolygon.append(QPointF(self.xInicio,self.yTermino))
                tipPolygon.append(QPointF(500,self.yTermino))
                tipPolygon.append(QPointF(500,self.yInicio))
                
                self.retangDia = QGraphicsPolygonItem(tipPolygon, None, None)
                if self.indice%5 == 0:
                    self.retangDia.setBrush(QBrush(Qt.red))
                    self.buttonCompromisso.setStyleSheet('background-color: red;\n color: yellow')
                elif self.indice%5 == 1:
                    self.retangDia.setBrush(QBrush(Qt.green))
                    self.buttonCompromisso.setStyleSheet('background-color: green;\n color: cyan')
                elif self.indice%5 == 2:
                    self.retangDia.setBrush(QBrush(Qt.yellow))
                    self.buttonCompromisso.setStyleSheet('background-color: yellow;\n color: black')
                elif self.indice%5 == 3:
                    self.retangDia.setBrush(QBrush(Qt.blue))
                    self.buttonCompromisso.setStyleSheet('background-color: blue;\n color: white')
                else:
                    self.retangDia.setBrush(QBrush(Qt.cyan))
                    self.buttonCompromisso.setStyleSheet('background-color: cyan;\n color: black')
                
            else:
                time = QTime(0,0)
                self.yInicio = 39 + time.secsTo(inicioTime)/62.06896551724138
                self.yTermino = 39 + time.secsTo(terminoTime)/62.06896551724138
                
                tipPolygonI = QPolygonF()
                tipPolygonI.append(QPointF(self.xInicio,self.yInicio))
                tipPolygonI.append(QPointF(self.xInicio,1441))
                tipPolygonI.append(QPointF(500,1441))
                tipPolygonI.append(QPointF(500,self.yInicio))
                
                tipPolygonT = QPolygonF()
                tipPolygonT.append(QPointF(self.xInicio,0))
                tipPolygonT.append(QPointF(self.xInicio,self.yTermino))
                tipPolygonT.append(QPointF(500,self.yTermino))
                tipPolygonT.append(QPointF(500,0))
                
                self.retangDiaInicio = QGraphicsPolygonItem(tipPolygonI, None, None)
                self.retangDiaTermino = QGraphicsPolygonItem(tipPolygonT, None, None)
                
                if self.indice%5 == 0:
                    self.retangDiaInicio.setBrush(QBrush(Qt.red))
                    self.retangDiaTermino.setBrush(QBrush(Qt.red))
                    self.buttonCompromisso.setStyleSheet('background-color: red;\n color: yellow')
                elif self.indice%5 == 1:
                    self.retangDiaInicio.setBrush(QBrush(Qt.green))
                    self.retangDiaTermino.setBrush(QBrush(Qt.green))
                    self.buttonCompromisso.setStyleSheet('background-color: green;\n color: cyan')
                elif self.indice%5 == 2:
                    self.retangDiaInicio.setBrush(QBrush(Qt.yellow))
                    self.retangDiaTermino.setBrush(QBrush(Qt.yellow))
                    self.buttonCompromisso.setStyleSheet('background-color: yellow;\n color: black')
                elif self.indice%5 == 3:
                    self.retangDiaInicio.setBrush(QBrush(Qt.blue))
                    self.retangDiaTermino.setBrush(QBrush(Qt.blue))
                    self.buttonCompromisso.setStyleSheet('background-color: blue;\n color: white')
                else:
                    self.retangDiaInicio.setBrush(QBrush(Qt.cyan))
                    self.retangDiaTermino.setBrush(QBrush(Qt.cyan))
                    self.buttonCompromisso.setStyleSheet('background-color: cyan;\n color: black')
        else:
            tipPolygon = QPolygonF()
            tipPolygon.append(QPointF(0,39))
            tipPolygon.append(QPointF(0,1402))
            tipPolygon.append(QPointF(500,1402))
            tipPolygon.append(QPointF(500,39))
            
            self.retangDia = QGraphicsPolygonItem(tipPolygon, None, None)
            if self.indice%5 == 0:
                self.retangDia.setBrush(QBrush(Qt.red))
                self.buttonCompromisso.setStyleSheet('background-color: red;\n color: yellow')
            elif self.indice%5 == 1:
                self.retangDia.setBrush(QBrush(Qt.green))
                self.buttonCompromisso.setStyleSheet('background-color: green;\n color: cyan')
            elif self.indice%5 == 2:
                self.retangDia.setBrush(QBrush(Qt.yellow))
                self.buttonCompromisso.setStyleSheet('background-color: yellow;\n color: black')
            elif self.indice%5 == 3:
                self.retangDia.setBrush(QBrush(Qt.blue))
                self.buttonCompromisso.setStyleSheet('background-color: blue;\n color: white')
            else:
                self.retangDia.setBrush(QBrush(Qt.cyan))
                self.buttonCompromisso.setStyleSheet('background-color: cyan;\n color: black')
        
        self.setListTabSemana()
        self.setListDescricao()
    
    def setFlexivel(self, duracao, prioridade, dataLimite, timeDas, timeAte, diasDaSemana):
        self.tipo = 'FLEXIVEL'
        self.duracao = duracao
        self.prioridade = prioridade
        self.dataLimite = dataLimite
        self.timeDas = timeDas
        self.timeAte = timeAte
        self.diasDaSemana = diasDaSemana
    
    def setTempConfig(self, repetir, yInicio, yTermino, inicioDate, inicioTime, terminoDate, terminoTime, retangMesInicio, retangMesTermino, retangSemanaInicio, retangSemanaTermino, dayOrder, flexOrder):
        self.repetir = repetir
        self.yInicio = yInicio
        self.yTermino = yTermino
        self.inicioDate = inicioDate
        self.inicioTime = inicioTime
        self.terminoDate = terminoDate
        self.terminoTime = terminoTime
        self.dayOrder = dayOrder
        self.flexOrder = flexOrder
        self.setListDescricao()
    
    def setListDescricao(self):
        buffer = ''
        if self.tipo == 'FIXO':
            buffer = 'Título:\n  {0}\n\nLocal:\n  {1}\n\nTrasnporte disponível:\n  {2}\n\n'.format(self.titulo, self.endereco, self.transporte)
            if self.repetir == 'Nunca':
                buffer += 'Repetir: Nunca\n\nInicio:\n  {0} de {1} de {2}\n  '.format(self.inicioDate.day(), QDate.longMonthName(self.inicioDate.month()), self.inicioDate.year())
                if self.inicioTime.minute() < 10:
                    buffer += '{0}h0{1}\n\n'.format(self.inicioTime.hour(), self.inicioTime.minute())
                else:
                    buffer += '{0}h{1}\n\n'.format(self.inicioTime.hour(), self.inicioTime.minute())
                buffer += 'Término:\n  {0} de {1} de {2}\n  '.format(self.terminoDate.day(), QDate.longMonthName(self.terminoDate.month()), self.terminoDate.year())
                if self.terminoTime.minute() < 10:
                    buffer += '{0}h0{1}\n\n'.format(self.terminoTime.hour(), self.terminoTime.minute())
                else:
                    buffer += '{0}h{1}\n\n'.format(self.terminoTime.hour(), self.terminoTime.minute())
                buffer += 'Descrição:\n  {0}'.format(self.descricao)
                
        else:
            pass
        
        self.listDescricao = QStandardItem(buffer)
        self.listDescricao.setEditable(False)
    
    def setListTabSemana(self):
        buffer = ''
        linha = ''
        palavras = self.titulo.split()
        
        for idx,palavra in enumerate(palavras):
            if idx == 0:
                if len(palavras) == 1:
                    buffer = '  ' + palavra
                else:
                    linha = '  ' + palavra + ' '
            elif len(linha + palavra) > 20:
                middle = []
                for letra in linha:
                    middle += [letra]
                middle.pop()
                linha = ''
                idxs = []
                for idx,letra in enumerate(middle):
                    if idx == 0:
                        pass
                    elif letra == ' ':
                        idxs += [idx]
                i = 0
                while len(middle) != 20:
                    middle.insert(idxs[i%len(idxs)], ' ')
                    for indice,j in enumerate(idxs):
                        idxs[indice] += 1
                    i += 1
                for n in middle:
                    linha += n
                buffer += linha + '\n'
                linha = palavra + ' '
            elif len(linha + palavra) == 20:
                buffer += linha + palavra + '\n'
                linha = ''
            else:
                if idx == len(palavras)-1:
                    linha += palavra
                    buffer += linha
                else:
                    linha += palavra + ' '
            
            if self.allDay == True:
                self.listTabSemana = QStandardItem('Dia Todo:\n{0}'.format(buffer))
            else:
                inicioTimeMinutos = '{0}'.format(self.inicioTime.minute())
                terminoTimeMinutos = '{0}'.format(self.terminoTime.minute())
                
                if self.inicioTime.minute() < 10:
                    inicioTimeMinutos = '0' + inicioTimeMinutos
                if self.terminoTime.minute() < 10:
                    terminoTimeMinutos = '0' + terminoTimeMinutos
                
                self.listTabSemana = QStandardItem('{0}h{1} até {2}h{3}:\n{4}'.format(self.inicioTime.hour(),inicioTimeMinutos,self.terminoTime.hour(),terminoTimeMinutos,buffer))
            
            self.listTabSemana.setEditable(False)
    
    def setFunc(self, func):
        self.func = func
    
    def execFunc(self):
        exec(self.func)
        
    def setWin(self, win):
        self.win = win
