# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projetofinal.ui'
#
# Created: Mon Jun  1 08:13:44 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
import sys 

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(919, 472)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAcceptDrops(True)
        MainWindow.setWindowTitle(_fromUtf8("Agenda Inteligente"))
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(170, 20, 581, 411))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.calendarWidget_3 = QtGui.QCalendarWidget(self.tab)
        self.calendarWidget_3.setGeometry(QtCore.QRect(0, 0, 581, 391))
        self.calendarWidget_3.setGridVisible(True)
        self.calendarWidget_3.setVerticalHeaderFormat(QtGui.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_3.setObjectName(_fromUtf8("calendarWidget_3"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.stacked_semanal = QtGui.QStackedWidget(self.tab_2)
        self.stacked_semanal.setGeometry(QtCore.QRect(0, 0, 571, 381))
        self.stacked_semanal.setMouseTracking(True)
        self.stacked_semanal.setAcceptDrops(False)
        self.stacked_semanal.setLineWidth(0)
        self.stacked_semanal.setObjectName(_fromUtf8("stacked_semanal"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.titulo_semana2 = QtGui.QLabel(self.page_3)
        self.titulo_semana2.setGeometry(QtCore.QRect(20, 10, 111, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Imprint MT Shadow"))
        font.setPointSize(16)
        self.titulo_semana2.setFont(font)
        self.titulo_semana2.setObjectName(_fromUtf8("titulo_semana2"))
        self.lista_semana2dia1 = QtGui.QListView(self.page_3)
        self.lista_semana2dia1.setGeometry(QtCore.QRect(30, 40, 101, 341))
        self.lista_semana2dia1.setObjectName(_fromUtf8("lista_semana2dia1"))
        self.lista_semana2dia5 = QtGui.QListView(self.page_3)
        self.lista_semana2dia5.setGeometry(QtCore.QRect(430, 40, 101, 341))
        self.lista_semana2dia5.setObjectName(_fromUtf8("lista_semana2dia5"))
        self.lista_semana2dia3 = QtGui.QListView(self.page_3)
        self.lista_semana2dia3.setGeometry(QtCore.QRect(230, 40, 101, 341))
        self.lista_semana2dia3.setObjectName(_fromUtf8("lista_semana2dia3"))
        self.lista_semana2dia2 = QtGui.QListView(self.page_3)
        self.lista_semana2dia2.setGeometry(QtCore.QRect(130, 40, 101, 341))
        self.lista_semana2dia2.setObjectName(_fromUtf8("lista_semana2dia2"))
        self.lista_semana2dia4 = QtGui.QListView(self.page_3)
        self.lista_semana2dia4.setGeometry(QtCore.QRect(330, 40, 101, 341))
        self.lista_semana2dia4.setObjectName(_fromUtf8("lista_semana2dia4"))
        self.stacked_semanal.addWidget(self.page_3)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.titulo_semana3 = QtGui.QLabel(self.page_6)
        self.titulo_semana3.setGeometry(QtCore.QRect(20, 10, 131, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Imprint MT Shadow"))
        font.setPointSize(16)
        self.titulo_semana3.setFont(font)
        self.titulo_semana3.setObjectName(_fromUtf8("titulo_semana3"))
        self.lista_semana3dia1 = QtGui.QListView(self.page_6)
        self.lista_semana3dia1.setGeometry(QtCore.QRect(30, 40, 101, 341))
        self.lista_semana3dia1.setObjectName(_fromUtf8("lista_semana3dia1"))
        self.lista_semana3dia5 = QtGui.QListView(self.page_6)
        self.lista_semana3dia5.setGeometry(QtCore.QRect(430, 40, 101, 341))
        self.lista_semana3dia5.setObjectName(_fromUtf8("lista_semana3dia5"))
        self.lista_semana3dia3 = QtGui.QListView(self.page_6)
        self.lista_semana3dia3.setGeometry(QtCore.QRect(230, 40, 101, 341))
        self.lista_semana3dia3.setObjectName(_fromUtf8("lista_semana3dia3"))
        self.lista_semana3dia2 = QtGui.QListView(self.page_6)
        self.lista_semana3dia2.setGeometry(QtCore.QRect(130, 40, 101, 341))
        self.lista_semana3dia2.setObjectName(_fromUtf8("lista_semana3dia2"))
        self.lista_semana3dia4 = QtGui.QListView(self.page_6)
        self.lista_semana3dia4.setGeometry(QtCore.QRect(330, 40, 101, 341))
        self.lista_semana3dia4.setObjectName(_fromUtf8("lista_semana3dia4"))
        self.stacked_semanal.addWidget(self.page_6)
        self.page_7 = QtGui.QWidget()
        self.page_7.setObjectName(_fromUtf8("page_7"))
        self.titulo_semana4 = QtGui.QLabel(self.page_7)
        self.titulo_semana4.setGeometry(QtCore.QRect(20, 10, 111, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Imprint MT Shadow"))
        font.setPointSize(16)
        self.titulo_semana4.setFont(font)
        self.titulo_semana4.setObjectName(_fromUtf8("titulo_semana4"))
        self.lista_semana4dia1 = QtGui.QListView(self.page_7)
        self.lista_semana4dia1.setGeometry(QtCore.QRect(30, 40, 101, 341))
        self.lista_semana4dia1.setObjectName(_fromUtf8("lista_semana4dia1"))
        self.lista_semana4dia5 = QtGui.QListView(self.page_7)
        self.lista_semana4dia5.setGeometry(QtCore.QRect(430, 40, 101, 341))
        self.lista_semana4dia5.setObjectName(_fromUtf8("lista_semana4dia5"))
        self.lista_semana4dia3 = QtGui.QListView(self.page_7)
        self.lista_semana4dia3.setGeometry(QtCore.QRect(230, 40, 101, 341))
        self.lista_semana4dia3.setObjectName(_fromUtf8("lista_semana4dia3"))
        self.lista_semana4dia2 = QtGui.QListView(self.page_7)
        self.lista_semana4dia2.setGeometry(QtCore.QRect(130, 40, 101, 341))
        self.lista_semana4dia2.setObjectName(_fromUtf8("lista_semana4dia2"))
        self.lista_semana4dia4 = QtGui.QListView(self.page_7)
        self.lista_semana4dia4.setGeometry(QtCore.QRect(330, 40, 101, 341))
        self.lista_semana4dia4.setObjectName(_fromUtf8("lista_semana4dia4"))
        self.stacked_semanal.addWidget(self.page_7)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.titulo_semana1 = QtGui.QLabel(self.page_4)
        self.titulo_semana1.setGeometry(QtCore.QRect(20, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Imprint MT Shadow"))
        font.setPointSize(16)
        self.titulo_semana1.setFont(font)
        self.titulo_semana1.setObjectName(_fromUtf8("titulo_semana1"))
        self.lista_semana1dia1 = QtGui.QListView(self.page_4)
        self.lista_semana1dia1.setGeometry(QtCore.QRect(20, 40, 101, 341))
        self.lista_semana1dia1.setObjectName(_fromUtf8("lista_semana1dia1"))
        self.lista_semana1dia2 = QtGui.QListView(self.page_4)
        self.lista_semana1dia2.setGeometry(QtCore.QRect(120, 40, 101, 341))
        self.lista_semana1dia2.setObjectName(_fromUtf8("lista_semana1dia2"))
        self.lista_semana1dia3 = QtGui.QListView(self.page_4)
        self.lista_semana1dia3.setGeometry(QtCore.QRect(220, 40, 101, 341))
        self.lista_semana1dia3.setObjectName(_fromUtf8("lista_semana1dia3"))
        self.lista_semana1dia4 = QtGui.QListView(self.page_4)
        self.lista_semana1dia4.setGeometry(QtCore.QRect(320, 40, 101, 341))
        self.lista_semana1dia4.setObjectName(_fromUtf8("lista_semana1dia4"))
        self.lista_semana1dia5 = QtGui.QListView(self.page_4)
        self.lista_semana1dia5.setGeometry(QtCore.QRect(420, 40, 101, 341))
        self.lista_semana1dia5.setObjectName(_fromUtf8("lista_semana1dia5"))
        self.stacked_semanal.addWidget(self.page_4)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.coluna_diario = QtGui.QColumnView(self.tab_3)
        self.coluna_diario.setGeometry(QtCore.QRect(20, 10, 441, 271))
        self.coluna_diario.setObjectName(_fromUtf8("coluna_diario"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.lista_compromissos = QtGui.QListView(self.tab_4)
        self.lista_compromissos.setGeometry(QtCore.QRect(70, 20, 321, 271))
        self.lista_compromissos.setFrameShape(QtGui.QFrame.VLine)
        self.lista_compromissos.setFrameShadow(QtGui.QFrame.Raised)
        self.lista_compromissos.setMovement(QtGui.QListView.Static)
        self.lista_compromissos.setObjectName(_fromUtf8("lista_compromissos"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 131, 411))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.informacoes = QtGui.QToolBox(self.verticalLayoutWidget)
        self.informacoes.setObjectName(_fromUtf8("informacoes"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 129, 328))
        self.page.setObjectName(_fromUtf8("page"))
        self.botao_okcancel_compromisso = QtGui.QDialogButtonBox(self.page)
        self.botao_okcancel_compromisso.setGeometry(QtCore.QRect(20, 310, 91, 20))
        self.botao_okcancel_compromisso.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.botao_okcancel_compromisso.setCenterButtons(True)
        self.botao_okcancel_compromisso.setObjectName(_fromUtf8("botao_okcancel_compromisso"))
        self.combobox_repetir = QtGui.QComboBox(self.page)
        self.combobox_repetir.setGeometry(QtCore.QRect(10, 120, 111, 20))
        self.combobox_repetir.setObjectName(_fromUtf8("combobox_repetir"))
        self.combobox_repetir.addItem(_fromUtf8(""))
        self.combobox_repetir.addItem(_fromUtf8(""))
        self.combobox_repetir.addItem(_fromUtf8(""))
        self.combobox_repetir.addItem(_fromUtf8(""))
        self.combobox_repetir.addItem(_fromUtf8(""))
        self.combobox_repetir.addItem(_fromUtf8(""))
        self.combobox_repetir.setItemText(5, _fromUtf8(""))
        self.toolbox_flexivel = QtGui.QRadioButton(self.page)
        self.toolbox_flexivel.setGeometry(QtCore.QRect(30, 70, 61, 17))
        self.toolbox_flexivel.setObjectName(_fromUtf8("toolbox_flexivel"))
        self.descricao_compromisso = QtGui.QTextEdit(self.page)
        self.descricao_compromisso.setGeometry(QtCore.QRect(10, 20, 111, 41))
        self.descricao_compromisso.setObjectName(_fromUtf8("descricao_compromisso"))
        self.nome_compromisso = QtGui.QLineEdit(self.page)
        self.nome_compromisso.setGeometry(QtCore.QRect(10, 0, 111, 20))
        self.nome_compromisso.setReadOnly(False)
        self.nome_compromisso.setObjectName(_fromUtf8("nome_compromisso"))
        self.dateTme_inicio = QtGui.QDateTimeEdit(self.page)
        self.dateTme_inicio.setGeometry(QtCore.QRect(10, 230, 111, 22))
        self.dateTme_inicio.setObjectName(_fromUtf8("dateTme_inicio"))
        self.dateTime_termino = QtGui.QDateTimeEdit(self.page)
        self.dateTime_termino.setGeometry(QtCore.QRect(10, 280, 111, 22))
        self.dateTime_termino.setObjectName(_fromUtf8("dateTime_termino"))
        self.titulo_horarioinicio = QtGui.QLabel(self.page)
        self.titulo_horarioinicio.setGeometry(QtCore.QRect(20, 210, 81, 16))
        self.titulo_horarioinicio.setObjectName(_fromUtf8("titulo_horarioinicio"))
        self.titulo_horariotermino = QtGui.QLabel(self.page)
        self.titulo_horariotermino.setGeometry(QtCore.QRect(20, 260, 101, 16))
        self.titulo_horariotermino.setObjectName(_fromUtf8("titulo_horariotermino"))
        self.combobox_prioridade = QtGui.QComboBox(self.page)
        self.combobox_prioridade.setGeometry(QtCore.QRect(10, 150, 111, 20))
        self.combobox_prioridade.setObjectName(_fromUtf8("combobox_prioridade"))
        self.combobox_prioridade.addItem(_fromUtf8(""))
        self.combobox_prioridade.addItem(_fromUtf8(""))
        self.combobox_prioridade.addItem(_fromUtf8(""))
        self.combobox_prioridade.addItem(_fromUtf8(""))
        self.combobox_prioridade.addItem(_fromUtf8(""))
        self.combobox_prioridade.setItemText(4, _fromUtf8(""))
        self.combobox_transporte = QtGui.QComboBox(self.page)
        self.combobox_transporte.setGeometry(QtCore.QRect(10, 180, 111, 20))
        self.combobox_transporte.setObjectName(_fromUtf8("combobox_transporte"))
        self.combobox_transporte.addItem(_fromUtf8(""))
        self.combobox_transporte.addItem(_fromUtf8(""))
        self.combobox_transporte.addItem(_fromUtf8(""))
        self.combobox_transporte.addItem(_fromUtf8(""))
        self.combobox_transporte.addItem(_fromUtf8(""))
        self.combobox_transporte.addItem(_fromUtf8(""))
        self.combobox_transporte.addItem(_fromUtf8(""))
        self.endereco_compromisso = QtGui.QLineEdit(self.page)
        self.endereco_compromisso.setGeometry(QtCore.QRect(10, 90, 111, 20))
        self.endereco_compromisso.setReadOnly(False)
        self.endereco_compromisso.setObjectName(_fromUtf8("endereco_compromisso"))
        self.informacoes.addItem(self.page, _fromUtf8(""))
        self.page_5 = QtGui.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 129, 328))
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.botao_save_perfil = QtGui.QDialogButtonBox(self.page_5)
        self.botao_save_perfil.setGeometry(QtCore.QRect(30, 300, 91, 23))
        self.botao_save_perfil.setStandardButtons(QtGui.QDialogButtonBox.Save)
        self.botao_save_perfil.setCenterButtons(True)
        self.botao_save_perfil.setObjectName(_fromUtf8("botao_save_perfil"))
        self.progressBar_perfil_completo = QtGui.QProgressBar(self.page_5)
        self.progressBar_perfil_completo.setGeometry(QtCore.QRect(20, 130, 101, 20))
        self.progressBar_perfil_completo.setProperty("value", 24)
        self.progressBar_perfil_completo.setObjectName(_fromUtf8("progressBar_perfil_completo"))
        self.input_nome = QtGui.QLineEdit(self.page_5)
        self.input_nome.setGeometry(QtCore.QRect(0, 0, 131, 20))
        self.input_nome.setObjectName(_fromUtf8("input_nome"))
        self.input_endereco_residencial = QtGui.QLineEdit(self.page_5)
        self.input_endereco_residencial.setGeometry(QtCore.QRect(0, 20, 131, 20))
        self.input_endereco_residencial.setObjectName(_fromUtf8("input_endereco_residencial"))
        self.input_endereco_comercial = QtGui.QLineEdit(self.page_5)
        self.input_endereco_comercial.setGeometry(QtCore.QRect(0, 40, 131, 20))
        self.input_endereco_comercial.setObjectName(_fromUtf8("input_endereco_comercial"))
        self.input_transporte = QtGui.QLineEdit(self.page_5)
        self.input_transporte.setGeometry(QtCore.QRect(0, 60, 131, 20))
        self.input_transporte.setObjectName(_fromUtf8("input_transporte"))
        self.input_placa = QtGui.QLineEdit(self.page_5)
        self.input_placa.setGeometry(QtCore.QRect(0, 80, 131, 20))
        self.input_placa.setObjectName(_fromUtf8("input_placa"))
        self.informacoes.addItem(self.page_5, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 129, 328))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.b = QtGui.QDialogButtonBox(self.page_2)
        self.b.setGeometry(QtCore.QRect(30, 300, 81, 23))
        self.b.setStandardButtons(QtGui.QDialogButtonBox.Save)
        self.b.setCenterButtons(True)
        self.b.setObjectName(_fromUtf8("b"))
        self.config_mostra_feriados = QtGui.QRadioButton(self.page_2)
        self.config_mostra_feriados.setGeometry(QtCore.QRect(10, 70, 111, 17))
        self.config_mostra_feriados.setObjectName(_fromUtf8("config_mostra_feriados"))
        self.informacoes.addItem(self.page_2, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.informacoes)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 919, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuP_gina_Inicial = QtGui.QMenu(self.menuBar)
        self.menuP_gina_Inicial.setObjectName(_fromUtf8("menuP_gina_Inicial"))
        self.menuConfigura_es = QtGui.QMenu(self.menuBar)
        self.menuConfigura_es.setObjectName(_fromUtf8("menuConfigura_es"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionVer_Compromissos = QtGui.QAction(MainWindow)
        self.actionVer_Compromissos.setObjectName(_fromUtf8("actionVer_Compromissos"))
        self.actionAdicionar_Compromissos = QtGui.QAction(MainWindow)
        self.actionAdicionar_Compromissos.setObjectName(_fromUtf8("actionAdicionar_Compromissos"))
        self.actionM_s = QtGui.QAction(MainWindow)
        self.actionM_s.setObjectName(_fromUtf8("actionM_s"))
        self.actionSemana = QtGui.QAction(MainWindow)
        self.actionSemana.setObjectName(_fromUtf8("actionSemana"))
        self.actionDia = QtGui.QAction(MainWindow)
        self.actionDia.setObjectName(_fromUtf8("actionDia"))
        self.actionEditar_seu_perfil = QtGui.QAction(MainWindow)
        self.actionEditar_seu_perfil.setObjectName(_fromUtf8("actionEditar_seu_perfil"))
        self.menuP_gina_Inicial.addAction(self.actionVer_Compromissos)
        self.menuP_gina_Inicial.addAction(self.actionAdicionar_Compromissos)
        self.menuP_gina_Inicial.addSeparator()
        self.menuP_gina_Inicial.addAction(self.actionM_s)
        self.menuP_gina_Inicial.addAction(self.actionSemana)
        self.menuP_gina_Inicial.addAction(self.actionDia)
        self.menuConfigura_es.addAction(self.actionEditar_seu_perfil)
        self.menuBar.addAction(self.menuP_gina_Inicial.menuAction())
        self.menuBar.addAction(self.menuConfigura_es.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.stacked_semanal.setCurrentIndex(3)
        self.informacoes.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Calendário Mensal", None))
        self.titulo_semana2.setText(_translate("MainWindow", "Semana 2", None))
        self.titulo_semana3.setText(_translate("MainWindow", "Semana 3", None))
        self.titulo_semana4.setText(_translate("MainWindow", "Semana 4", None))
        self.titulo_semana1.setText(_translate("MainWindow", "Semana 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Semanal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Diário", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Compromissos", None))
        self.combobox_repetir.setItemText(0, _translate("MainWindow", "Ou repetir?", None))
        self.combobox_repetir.setItemText(1, _translate("MainWindow", "Nunca", None))
        self.combobox_repetir.setItemText(2, _translate("MainWindow", "Todo Dia", None))
        self.combobox_repetir.setItemText(3, _translate("MainWindow", "Toda Semana", None))
        self.combobox_repetir.setItemText(4, _translate("MainWindow", "Todo Mês", None))
        self.toolbox_flexivel.setText(_translate("MainWindow", "Flexível", None))
        self.descricao_compromisso.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Descrição</p></body></html>", None))
        self.nome_compromisso.setText(_translate("MainWindow", "Título", None))
        self.titulo_horarioinicio.setText(_translate("MainWindow", "Horário de Início", None))
        self.titulo_horariotermino.setText(_translate("MainWindow", "Horário de Término", None))
        self.combobox_prioridade.setItemText(0, _translate("MainWindow", "Prioridade", None))
        self.combobox_prioridade.setItemText(1, _translate("MainWindow", "Baixa", None))
        self.combobox_prioridade.setItemText(2, _translate("MainWindow", "Média", None))
        self.combobox_prioridade.setItemText(3, _translate("MainWindow", "Alta", None))
        self.combobox_transporte.setItemText(0, _translate("MainWindow", "Transporte", None))
        self.combobox_transporte.setItemText(1, _translate("MainWindow", "A Pé", None))
        self.combobox_transporte.setItemText(2, _translate("MainWindow", "Bicicleta", None))
        self.combobox_transporte.setItemText(3, _translate("MainWindow", "Carro", None))
        self.combobox_transporte.setItemText(4, _translate("MainWindow", "Moto", None))
        self.combobox_transporte.setItemText(5, _translate("MainWindow", "Metrô", None))
        self.combobox_transporte.setItemText(6, _translate("MainWindow", "Ônibus", None))
        self.endereco_compromisso.setText(_translate("MainWindow", "Endereço", None))
        self.informacoes.setItemText(self.informacoes.indexOf(self.page), _translate("MainWindow", "Novo Compromisso", None))
        self.input_nome.setText(_translate("MainWindow", "Nome", None))
        self.input_endereco_residencial.setText(_translate("MainWindow", "Endereço Residencial", None))
        self.input_endereco_comercial.setText(_translate("MainWindow", "Endereço Comercial", None))
        self.input_transporte.setText(_translate("MainWindow", "Transporte Usado", None))
        self.input_placa.setText(_translate("MainWindow", "Final da Placa", None))
        self.informacoes.setItemText(self.informacoes.indexOf(self.page_5), _translate("MainWindow", "Meu Perfil", None))
        self.config_mostra_feriados.setText(_translate("MainWindow", "Mostrar Feriados", None))
        self.informacoes.setItemText(self.informacoes.indexOf(self.page_2), _translate("MainWindow", "Configurações", None))
        self.menuP_gina_Inicial.setTitle(_translate("MainWindow", "Página Inicial", None))
        self.menuConfigura_es.setTitle(_translate("MainWindow", "Configurações", None))
        self.actionVer_Compromissos.setText(_translate("MainWindow", "Ver Compromissos", None))
        self.actionAdicionar_Compromissos.setText(_translate("MainWindow", "Adicionar Compromissos", None))
        self.actionM_s.setText(_translate("MainWindow", "Mês", None))
        self.actionSemana.setText(_translate("MainWindow", "Semana", None))
        self.actionDia.setText(_translate("MainWindow", "Dia", None))
        self.actionEditar_seu_perfil.setText(_translate("MainWindow", "Editar seu perfil", None))
        self.printMainWindow_btn.clicked.connect(self.printMainWindow)

    def printMainWindow(self):
        print ("MainWindow")
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())
    