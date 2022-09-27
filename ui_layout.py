# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Python Projects\Github\python_contas\layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 865)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_resumo = QtWidgets.QLabel(self.centralwidget)
        self.label_resumo.setMaximumSize(QtCore.QSize(10000, 400))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_resumo.setFont(font)
        self.label_resumo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_resumo.setObjectName("label_resumo")
        self.verticalLayout.addWidget(self.label_resumo)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bt_novo = QtWidgets.QPushButton(self.centralwidget)
        self.bt_novo.setObjectName("bt_novo")
        self.horizontalLayout_6.addWidget(self.bt_novo)
        self.bt_pagar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_pagar.setObjectName("bt_pagar")
        self.horizontalLayout_6.addWidget(self.bt_pagar)
        self.bt_receber = QtWidgets.QPushButton(self.centralwidget)
        self.bt_receber.setObjectName("bt_receber")
        self.horizontalLayout_6.addWidget(self.bt_receber)
        self.bt_inicio = QtWidgets.QPushButton(self.centralwidget)
        self.bt_inicio.setObjectName("bt_inicio")
        self.horizontalLayout_6.addWidget(self.bt_inicio)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.frame_cadastro = QtWidgets.QFrame(self.centralwidget)
        self.frame_cadastro.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_cadastro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cadastro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cadastro.setObjectName("frame_cadastro")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_cadastro)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_11.setMinimumSize(QtCore.QSize(150, 0))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_cadastro)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_cadastro)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.ed_conta = QtWidgets.QLineEdit(self.frame_cadastro)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ed_conta.setFont(font)
        self.ed_conta.setObjectName("ed_conta")
        self.horizontalLayout.addWidget(self.ed_conta)
        self.label_3 = QtWidgets.QLabel(self.frame_cadastro)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.ed_valor = QtWidgets.QLineEdit(self.frame_cadastro)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ed_valor.setFont(font)
        self.ed_valor.setObjectName("ed_valor")
        self.horizontalLayout.addWidget(self.ed_valor)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_cadastro)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.ed_parcela = QtWidgets.QLineEdit(self.frame_cadastro)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ed_parcela.setFont(font)
        self.ed_parcela.setObjectName("ed_parcela")
        self.horizontalLayout_3.addWidget(self.ed_parcela)
        self.label_6 = QtWidgets.QLabel(self.frame_cadastro)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.ed_dia = QtWidgets.QLineEdit(self.frame_cadastro)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ed_dia.setFont(font)
        self.ed_dia.setObjectName("ed_dia")
        self.horizontalLayout_3.addWidget(self.ed_dia)
        self.label_7 = QtWidgets.QLabel(self.frame_cadastro)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.ed_mes = QtWidgets.QLineEdit(self.frame_cadastro)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ed_mes.setFont(font)
        self.ed_mes.setObjectName("ed_mes")
        self.horizontalLayout_3.addWidget(self.ed_mes)
        self.label_5 = QtWidgets.QLabel(self.frame_cadastro)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.ed_ano = QtWidgets.QLineEdit(self.frame_cadastro)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ed_ano.setFont(font)
        self.ed_ano.setObjectName("ed_ano")
        self.horizontalLayout_3.addWidget(self.ed_ano)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.frame_cadastro)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.cb_situacao = QtWidgets.QComboBox(self.frame_cadastro)
        self.cb_situacao.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_situacao.setFont(font)
        self.cb_situacao.setObjectName("cb_situacao")
        self.horizontalLayout_2.addWidget(self.cb_situacao)
        self.label_9 = QtWidgets.QLabel(self.frame_cadastro)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.cb_tipo = QtWidgets.QComboBox(self.frame_cadastro)
        self.cb_tipo.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_tipo.setFont(font)
        self.cb_tipo.setObjectName("cb_tipo")
        self.horizontalLayout_2.addWidget(self.cb_tipo)
        self.label_10 = QtWidgets.QLabel(self.frame_cadastro)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.cb_categoria = QtWidgets.QComboBox(self.frame_cadastro)
        self.cb_categoria.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_categoria.setFont(font)
        self.cb_categoria.setObjectName("cb_categoria")
        self.horizontalLayout_2.addWidget(self.cb_categoria)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bt_deletar = QtWidgets.QPushButton(self.frame_cadastro)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.bt_deletar.setFont(font)
        self.bt_deletar.setObjectName("bt_deletar")
        self.horizontalLayout_4.addWidget(self.bt_deletar)
        self.label_id = QtWidgets.QLabel(self.frame_cadastro)
        self.label_id.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_id.setText("")
        self.label_id.setObjectName("label_id")
        self.horizontalLayout_4.addWidget(self.label_id)
        self.bt_salvar = QtWidgets.QPushButton(self.frame_cadastro)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.bt_salvar.setFont(font)
        self.bt_salvar.setObjectName("bt_salvar")
        self.horizontalLayout_4.addWidget(self.bt_salvar)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.label_19 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_19.setMinimumSize(QtCore.QSize(150, 0))
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_10.addWidget(self.label_19)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_cadastro)
        self.frame_listagem = QtWidgets.QFrame(self.centralwidget)
        self.frame_listagem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_listagem.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_listagem.setObjectName("frame_listagem")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_listagem)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_14 = QtWidgets.QLabel(self.frame_listagem)
        self.label_14.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.cb_tipo_pesquisa = QtWidgets.QComboBox(self.frame_listagem)
        self.cb_tipo_pesquisa.setMinimumSize(QtCore.QSize(200, 0))
        self.cb_tipo_pesquisa.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cb_tipo_pesquisa.setFont(font)
        self.cb_tipo_pesquisa.setObjectName("cb_tipo_pesquisa")
        self.horizontalLayout_7.addWidget(self.cb_tipo_pesquisa)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_15 = QtWidgets.QLabel(self.frame_listagem)
        self.label_15.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_8.addWidget(self.label_15)
        self.cb_mes = QtWidgets.QComboBox(self.frame_listagem)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_mes.setFont(font)
        self.cb_mes.setObjectName("cb_mes")
        self.horizontalLayout_8.addWidget(self.cb_mes)
        self.label_16 = QtWidgets.QLabel(self.frame_listagem)
        self.label_16.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_8.addWidget(self.label_16)
        self.cb_ano = QtWidgets.QComboBox(self.frame_listagem)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_ano.setFont(font)
        self.cb_ano.setObjectName("cb_ano")
        self.horizontalLayout_8.addWidget(self.cb_ano)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.frame_listagem)
        self.label_12.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        self.bt_buscar = QtWidgets.QPushButton(self.frame_listagem)
        self.bt_buscar.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bt_buscar.setFont(font)
        self.bt_buscar.setObjectName("bt_buscar")
        self.horizontalLayout_5.addWidget(self.bt_buscar)
        self.label_13 = QtWidgets.QLabel(self.frame_listagem)
        self.label_13.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.frame_listagem)
        self.label_17.setMinimumSize(QtCore.QSize(400, 0))
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.frame_listagem)
        self.label_18.setMinimumSize(QtCore.QSize(400, 0))
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 0, 2, 1, 1)
        self.list_item = QtWidgets.QListWidget(self.frame_listagem)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.list_item.setFont(font)
        self.list_item.setObjectName("list_item")
        self.gridLayout.addWidget(self.list_item, 1, 0, 1, 3)
        self.verticalLayout.addWidget(self.frame_listagem)
        self.gridLayout_3.addLayout(self.verticalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionResumo = QtWidgets.QAction(MainWindow)
        self.actionResumo.setObjectName("actionResumo")
        self.actionCadastrar = QtWidgets.QAction(MainWindow)
        self.actionCadastrar.setObjectName("actionCadastrar")
        self.actionPagar = QtWidgets.QAction(MainWindow)
        self.actionPagar.setObjectName("actionPagar")
        self.actionReceber = QtWidgets.QAction(MainWindow)
        self.actionReceber.setObjectName("actionReceber")
        self.menuMenu.addAction(self.actionResumo)
        self.menuMenu.addAction(self.actionCadastrar)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionPagar)
        self.menuMenu.addAction(self.actionReceber)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_resumo.setText(_translate("MainWindow", "resumo"))
        self.bt_novo.setText(_translate("MainWindow", "NOVO"))
        self.bt_pagar.setText(_translate("MainWindow", "PAGAR"))
        self.bt_receber.setText(_translate("MainWindow", "RECEBER"))
        self.bt_inicio.setText(_translate("MainWindow", "INICIO"))
        self.label.setText(_translate("MainWindow", "Cadastrar Conta"))
        self.label_2.setText(_translate("MainWindow", "Conta"))
        self.label_3.setText(_translate("MainWindow", "Valor"))
        self.label_4.setText(_translate("MainWindow", "Parcela"))
        self.label_6.setText(_translate("MainWindow", "Dia"))
        self.label_7.setText(_translate("MainWindow", "Mes"))
        self.label_5.setText(_translate("MainWindow", "Ano"))
        self.label_8.setText(_translate("MainWindow", "Situação"))
        self.label_9.setText(_translate("MainWindow", "Tipo"))
        self.label_10.setText(_translate("MainWindow", "Categoria"))
        self.bt_deletar.setText(_translate("MainWindow", "Deletar"))
        self.bt_salvar.setText(_translate("MainWindow", "Salvar"))
        self.label_14.setText(_translate("MainWindow", "TIPO"))
        self.label_15.setText(_translate("MainWindow", "MES"))
        self.label_16.setText(_translate("MainWindow", "Ano"))
        self.bt_buscar.setText(_translate("MainWindow", "BUSCAR"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionResumo.setText(_translate("MainWindow", "Resumo"))
        self.actionCadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.actionPagar.setText(_translate("MainWindow", "Pagar"))
        self.actionReceber.setText(_translate("MainWindow", "Receber"))
