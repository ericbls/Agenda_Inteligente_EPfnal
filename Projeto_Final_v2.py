import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Agenda inteligente')
        
        
        verCompromissos = QAction(QIcon('verCompromisso.png'), '&Ver Compromissos', self)
        #verCompromissos.triggered.connect()
        adicionarCompromisso = QAction(QIcon('verCompromisso.png'), '&Adicionar Compromisso', self)
        #adicionarCompromisso.triggered.connect()
        mes = QAction(QIcon('mes.png'), '&Mês', self)
        #mes.triggered.connect()
        semana = QAction(QIcon('semana.png'), '&Semana', self)
        #semana.triggered.connect()
        dia = QAction(QIcon('dia.png'), '&Dia', self)
        #dia.triggered.connect()
        editarPerfil = QAction(QIcon('editaPerfil.png'), '&Editar Perfil', self)
        #editarPerfil.triggered.connect()
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Página Inicial')
        configMenu = menubar.addMenu('&Configurações')
        fileMenu.addAction(verCompromissos)
        fileMenu.addAction(adicionarCompromisso)
        fileMenu.addSeparator()
        fileMenu.addAction(mes)
        fileMenu.addAction(semana)
        fileMenu.addAction(dia)
        configMenu.addAction(editarPerfil)
        
        self.main = QWidget()
        layout = QVBoxLayout(self.main)
        
        self.setCentralWidget(self.main)
        
        self.resize(720,540)
        self.centerOnScreen()
        
        self.connect(QShortcut(QKeySequence(Qt.Key_Escape),self),SIGNAL('activated()'),self.deleteLater)
    
    def centerOnScreen(self):
        resolution = QDesktopWidget().screenGeometry()
        self.move( ( (resolution.width() / 2 ) - (self.width() / 2 ) )-100 , ( (resolution.height() / 2 ) - ( self.height() / 2 ) )-50 )




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()