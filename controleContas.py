# compilar usando
# venv\Scripts\pyinstaller.exe -F --console -w --upx-dir=Z:\Christian\Python\GitHub\upx-3.96-win64\upx-3.96-win64 --distpath .\ --ico .\icone.ico --name "Coleção de Moedas 2022" .\colecao_moedas_2022.py

from http.client import GONE
from os import link
from pprint import pprint
import sys
from threading import Thread
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
from layout import *
from functools import partial
from datetime import date, datetime
import requests
import urllib
from funcoes import Contas
from PyQt5.QtWidgets import QMainWindow, QApplication
import os
from matplotlib import pyplot as plt
import numpy as np

prog = Contas('db_contas.db')


class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        # oculta o botao pagar cartao
        self.bt_cartao_2.setVisible(False)

        # alinhamento top no vertical layout
        self.verticalLayout.setAlignment(Qt.AlignTop)

        # cria o banco de dados
        prog.criartabela()

        # captura a data de hoje
        dia, mes, ano = self.dataAtual()
        self.abrePesquisa("PAGAR", mes, ano)

        # exibe o resumo do mes atual
        resumo = prog.exibeResumo(mes, ano)
        self.label_resumo.setText(resumo)

        # preenche as informações nos combobox
        lista_situacao = ['', 'PAGO']
        self.cb_situacao.addItems(lista_situacao)
        lista_mes = ["1", "2", "3", "4", "5",
                     "6", "7", "8", "9", "10", "11", "12"]
        lista_ano = ["2022", "2023", "2024", "2025", "2026"]
        self.cb_mes.addItems(lista_mes)
        self.cb_ano.addItems(lista_ano)
        self.cb_ano.setCurrentText(str(ano))
        self.cb_mes.setCurrentText(str(mes))
        lista_tipo = ["PAGAR", "RECEBER"]
        self.cb_tipo.addItems(lista_tipo)
        lista_categoria = ['CASA', 'CARRO', 'LAZER', 'SAUDE', 'ITAU', 'BRADESCO', 'CAIXA',
                           'NUBANK', 'HYPERCARD', 'PERNANBUCANAS', 'MARISA', 'CEA', 'RIACHUELO', 'OUTROS']
        self.cb_categoria.addItems(lista_categoria)
        self.cb_tipo_pesquisa.addItems(lista_tipo)

        # oculta o frame de cadastro
        self.frame_cadastro.setVisible(False)
        self.frame_listagem.setVisible(False)

        # menu cadastro
        self.actionCadastrar.triggered.connect(self.abreCadastro)
        self.bt_novo.clicked.connect(self.abreCadastro)

        # menu receber
        self.bt_receber.clicked.connect(
            lambda: self.abrePesquisa("RECEBER", int(self.cb_mes.currentText()), int(self.cb_ano.currentText())))
        self.actionReceber.triggered.connect(
            lambda: self.abrePesquisa("RECEBER", int(self.cb_mes.currentText()), int(self.cb_ano.currentText())))

        # menu cartao
        self.bt_cartao.clicked.connect(
            lambda: self.abrePesquisa("PAGAR", int(self.cb_mes.currentText()), int(self.cb_ano.currentText()), cartao=True))

        # botao pagar cartao
        self.bt_cartao_2.clicked.connect(lambda: self.pagarCartao(
            int(self.cb_mes.currentText()), int(self.cb_ano.currentText())))

        # menu pagar
        self.bt_pagar.clicked.connect(
            lambda: self.abrePesquisa("PAGAR", int(self.cb_mes.currentText()), int(self.cb_ano.currentText())))
        self.actionPagar.triggered.connect(
            lambda: self.abrePesquisa("PAGAR", int(self.cb_mes.currentText()), int(self.cb_ano.currentText())))

        # botao proximo mes
        self.bt_prox.clicked.connect(
            lambda: self.abrePesquisa(self.cb_tipo_pesquisa.currentText(), int(self.cb_mes.currentText()), int(self.cb_ano.currentText()), proximo=True))
        # botao anterior mes
        self.bt_ant.clicked.connect(
            lambda: self.abrePesquisa(self.cb_tipo_pesquisa.currentText(), int(self.cb_mes.currentText()), int(self.cb_ano.currentText()), anterior=True))

        # botao salvar conta
        self.bt_salvar.clicked.connect(self.Cadastro)

        # botao buscar contas pagar ou receber
        self.bt_buscar.clicked.connect(lambda: self.abrePesquisa(tipo=str(
            self.cb_tipo_pesquisa.currentText()), mes=str(self.cb_mes.currentText()), ano=str(self.cb_ano.currentText())))

        # duplo clique no item da lista
        self.list_item.itemDoubleClicked.connect(
            lambda: self.abre_item_selecionado(item=self.list_item.currentItem()))

    def dataAtual(self):
        dataHoje = date.today()
        mes = dataHoje.month
        dia = dataHoje.day
        ano = dataHoje.year
        self.cb_mes.setCurrentText(str(mes))
        self.cb_ano.setCurrentText(str(ano))
        return dia, mes, ano

    def pagarCartao(self, mes, ano):
        self.bt_cartao_2.setVisible(False)
        retorno = prog.pagarCartao(mes, ano)
        if retorno:
            QMessageBox.information(
                self, 'Cadastro', f'Cadastro realizado com sucesso!')
        else:
            QMessageBox.warning(
                self, 'Cadastro', f'Houve um erro ao realizar o cadastro!')

    def abre_item_selecionado(self, item):

        try:
            id = str(item.text()).split(':')[1].strip()
            id, conta, valor, parcela, ano, mes, dia, situacao, tipo, categoria = prog.listar_id(
                id)
            self.label.setText('Atualizar Conta')
            self.frame_cadastro.setVisible(True)
            self.ed_conta.setText(conta)
            self.ed_valor.setText(valor)
            self.ed_parcela.setText(parcela)
            self.ed_ano.setText(ano)
            self.ed_mes.setText(mes)
            self.ed_dia.setText(dia)
            self.cb_situacao.setCurrentText(situacao)
            self.cb_tipo.setCurrentText(tipo)
            self.label_id.setText(str(id))
            self.cb_categoria.setCurrentText(categoria)
            self.bt_salvar.setText('Atualizar')
        except:
            self.frame_cadastro.setVisible(False)

    def abrePesquisa(self, tipo, mes=False, ano=False, anterior=False, proximo=False, cartao=False):

        if proximo:
            if int(mes) + 1 == 13:
                mes = str(1)
                ano = str(int(ano)+1)
                self.cb_ano.setCurrentText(ano)
                self.cb_mes.setCurrentText(mes)
            else:
                mes = str(int(mes)+1)
                self.cb_mes.setCurrentText(mes)
        if anterior:
            if int(mes) - 1 == 0:
                mes = str(12)
                ano = str(int(ano)-1)
                self.cb_ano.setCurrentText(ano)
                self.cb_mes.setCurrentText(mes)
            else:
                mes = str(int(mes)-1)
                self.cb_mes.setCurrentText(mes)

        self.frame_listagem.setVisible(True)
        self.frame_cadastro.setVisible(False)

        resumo = prog.exibeResumo(mes, ano)

        pixmap = QPixmap('grafico.png')
        pixmap = pixmap.scaled(460, 380, QtCore.Qt.KeepAspectRatio)
        self.grafico.setPixmap(pixmap)

        self.label_resumo.setText(resumo)

        itens = prog.buscar_tipos(vtipo=tipo, vmes=str(
            mes), vano=str(ano), credito=cartao)
        self.list_item.clear()
        self.cb_tipo_pesquisa.setCurrentText(tipo)

        try:
            for item in itens:
                self.list_item.addItem(item)
                if tipo == "PAGAR":
                    self.list_item.setStyleSheet(
                        "QListWidget {background-color: rgb(255,160,122)}")
                elif tipo == "RECEBER":
                    self.list_item.setStyleSheet(
                        "QListWidget {background-color: rgb(0,255,127)}")
                if cartao:
                    self.bt_cartao_2.setVisible(True)
                    self.list_item.setStyleSheet(
                        "QListWidget {background-color: rgb(240,230,140)}")

                else:
                    self.bt_cartao_2.setVisible(False)

            if self.list_item.count() == 0:
                self.list_item.clear()
                self.list_item.addItem('Nenhum item encontrado')
        except Exception as e:
            print(e)
            self.list_item.clear()
            self.list_item.addItem('Nenhum item encontrado')

    def abreCadastro(self):
        self.label.setText('Cadastrar Conta')
        self.frame_cadastro.setVisible(True)
        self.frame_listagem.setVisible(False)
        self.ed_conta.setText("")
        self.ed_valor.setText("")
        self.ed_parcela.setText("")
        self.ed_ano.setText("")
        self.ed_mes.setText("")
        self.ed_dia.setText("")
        self.cb_situacao.setCurrentText("")
        self.cb_tipo.setCurrentText("")
        self.label_id.setText("")
        self.cb_categoria.setCurrentText("")
        self.bt_salvar.setText("Salvar")

    def Cadastro(self):
        conta = self.ed_conta.text()
        valor = self.ed_valor.text()
        parcela = self.ed_parcela.text()
        ano = self.ed_ano.text()
        mes = self.ed_mes.text()
        dia = self.ed_dia.text()
        situacao = self.cb_situacao.currentText()

        tipo = self.cb_tipo.currentText()
        categoria = self.cb_categoria.currentText()
        retorno = False
        textBotao = self.bt_salvar.text()
        if textBotao == "Salvar":
            retorno = prog.inserir(conta=conta, valor=valor, parcela=parcela, ano=ano,
                                   mes=mes, dia=dia, situacao=situacao, tipo=tipo, categoria=categoria)
        elif textBotao == "Atualizar":
            retorno = prog.editar(id=self.label_id.text(), conta=conta, valor=valor, parcela=parcela, ano=ano,
                                  mes=mes, dia=dia, situacao=situacao, tipo=tipo, categoria=categoria)

        self.frame_cadastro.setVisible(False)

        resumo = prog.exibeResumo(mes, ano)
        self.label_resumo.setText(resumo)

        self.abrePesquisa(tipo, mes, ano)

        if retorno:
            QMessageBox.information(
                self, 'Cadastro', f'Cadastro realizado com sucesso!')
        else:
            QMessageBox.warning(
                self, 'Cadastro', f'Houve um erro ao realizar o cadastro!')


qt = QApplication(sys.argv)

novo = Novo()
novo.show()
qt.exec_()
