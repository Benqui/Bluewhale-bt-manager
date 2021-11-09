from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import btmanag

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet('background: rgb(73,102,140)')
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 130, 55))
        self.pushButton.setStyleSheet('font-size:20px; background: rgb(29,27,40); color: white')
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 0, 130, 55))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet('font-size:20px; background: rgb(29,27,40); color: white')
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 0, 130, 55))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet('font-size:20px; background: rgb(29,27,40); color: white')
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 60, 991, 601))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet('font-size:25px; background: rgb(128,167,191)')
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.pushButton.clicked.connect(self.func_consulta)
        self.pushButton_2.clicked.connect(self.connect_butt)
        self.pushButton_3.clicked.connect(self.pop_up)
        self.listWidget.clicked.connect(self.save_addr)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Buscar"))
        self.pushButton_2.setText(_translate("MainWindow", "Connectar"))
        self.pushButton_3.setText(_translate("MainWindow", "About"))
#Agrega los dispositivos a la lista de la gui
    def addlist(self,dispos):
        print("Entre\n")
        cont = 0
        for addr,name in dispos:
            pal = addr +" "+ name
            self.listWidget.insertItem(cont,pal)
            cont=+1

    def pop_up(self):
        msg = QMessageBox()
        msg.setWindowTitle('Integrantes del equipo')
        msg.setText("Bluewhale fue hecho por:\nTeam Sarosi\nConformado por:\nAngel Yedid Nacif Mena\nAbraham Martinez Zamora\nBenjamin Hoyos Herrera\nTheophil Havet")

        disp=msg.exec_()
#Hace una consulta para ver los disp. cercanos
    def func_consulta(self):
        dispositivos = []
        self.listWidget.clear()
        btmanag.consulta()
        dispositivos=btmanag.getdisps()
        self.addlist(dispositivos)
#guarda la direccion que clickeas 
    def save_addr(self):
        global dir_addr
        dir_addr= self.listWidget.currentItem()
        print(dir_addr.text())
        #print(type(dir_addr))
#Se conecta al dispositivo
    def connect_butt(self):
        global dir_addr
        get_addr=dir_addr.text()
        addr=tuple(get_addr.split(sep=" "))
        print(addr)
        btmanag.conexion(addr)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
