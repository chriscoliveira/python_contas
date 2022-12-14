import sqlite3
from playwright.sync_api import sync_playwright
from time import sleep
import os
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import numpy as np

#  C:\Users\Christian\AppData\Roaming\Python\Python310\Scripts\pyuic5 .\layout.ui -o .\layout.py


class Contas:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def criartabela(self):
        # conta,valor,parcela,ano,mes,dia,situacao,tipo,categoria
        sql = 'CREATE TABLE IF NOT EXISTS "Contas" ( "id" INTEGER UNIQUE, "CONTA" TEXT, "VALOR" TEXT, "PARCELA" TEXT, "ANO" TEXT, "MES" TEXT, "DIA" TEXT, "SITUACAO" TEXT, "TIPO" TEXT, "CATEGORIA" TEXT, PRIMARY KEY("id" AUTOINCREMENT) )'
        self.cursor.execute(sql)

    def inserir(self, conta, valor, parcela, ano, mes, dia, situacao, tipo, categoria):
        if conta and valor and parcela and ano and mes and dia and tipo and categoria:
            for i in range(int(parcela)):
                mes = int(mes)
                ano = int(ano)
                parc = f'PARCELA {i+1}/{int(parcela)}'

                print(parc)
                sql = "INSERT INTO Contas (conta,valor,parcela,ano,mes,dia,situacao,tipo,categoria) VALUES (?,?,?,?,?,?,?,?,?)"
                self.cursor.execute(sql, (str(conta).upper(), str(valor).upper(), str(parc).upper(), str(ano).upper(),
                                          str(mes).upper(), str(dia).upper(), str(situacao).upper(), str(tipo).upper(), str(categoria).upper()))
                self.conn.commit()

                # altera o mes e o ano nos cadastro em lote
                # altera o mes de acordo com a parcela
                if mes < 12:
                    mes += 1
                else:
                    mes = 1
                    ano += 1
            return True
        else:
            return False

    def editar(self, id, conta, valor, parcela, ano, mes, dia, situacao, tipo, categoria):
        try:
            sql = "UPDATE Contas SET conta=?, valor=?, parcela=?, ano=?, mes=?, dia=?, situacao=?, tipo=?, categoria=? WHERE id=?"
            self.cursor.execute(sql, (str(conta).upper(), str(valor).upper(), str(parcela).upper(), str(ano).upper(),
                                      str(mes).upper(), str(dia).upper(), str(situacao).upper(), str(tipo).upper(), str(categoria).upper(), id))
            self.conn.commit()
            return True
        except:
            return False

    def pagarCartao(self, ano, mes):
        try:
            sql = "UPDATE Contas SET situacao='PAGO' WHERE mes=? and ano=? and categoria='CARTAO'"
            self.cursor.execute(sql, (str(mes).upper(), str(ano).upper()))
            self.conn.commit()
            return True
        except:
            return False

    def remover(self, id):
        sql = "DELETE FROM Contas WHERE id=?"
        self.cursor.execute(sql, (id,))
        self.conn.commit()

    def listar_tudo(self):
        sql = "SELECT * FROM Contas"
        self.cursor.execute(sql)
        for linha in self.cursor.fetchall():
            print(linha)

    def listar_id(self, id):
        sql = "SELECT * FROM Contas where id =="+id
        self.cursor.execute(sql)
        for linha in self.cursor.fetchall():
            return linha

    def buscar_tipos(self, vtipo, vmes, vano, credito=False):
        # if termo == 'pagar':
        # WHERE tipo LIKE ? AND ano LIKE ? AND mes LIKE ?  ORDER BY dia"
        if credito:
            sql = "SELECT * FROM contas WHERE tipo LIKE ? and mes LIKE ? and ano  LIKE ? and categoria = 'CARTAO' order by dia"
        else:
            sql = "SELECT * FROM contas WHERE tipo LIKE ? and mes LIKE ? and ano  LIKE ? and categoria != 'CARTAO' order by dia"
        self.cursor.execute(sql, (vtipo, vmes, vano))
        # , '2022', '09'

        retorno = []
        retorno.append(f'conta \t\t\tcategoria: \t\tParcela:\t\tValor\t\tVencimento\tSitua????o:'
                       )
        for linha in self.cursor.fetchall():
            id = str(linha[0]) + ':'
            conta = linha[1]
            valor = linha[2]

            parcela = linha[3]
            ano = linha[4]
            mes = linha[5]
            dia = linha[6]
            situacao = linha[7]
            tipo = linha[8]
            categoria = linha[9]

            retorno.append(f'{conta: <33} \t{str(categoria): <20}\t\t {str(parcela): <10} \tR${valor: <10} \t{str(dia)}-{str(mes)}-{str(ano)} \t{situacao}\t\t\t:{str(id)}'
                           )
        sql = f'Select sum(valor) from Contas where tipo == "PAGAR" and mes == "{vmes}" and ano == "{vano}" and categoria=="CARTAO"'
        self.cursor.execute(sql)

        for linha in self.cursor.fetchall():
            total_cartao = linha[0]

        if total_cartao and vtipo == 'PAGAR' and not credito:

            retorno.append(
                f'CART??O DE CR??DITO\t\t\t\t\t\tR${round(total_cartao,2)}')

        return retorno

    def exibeResumo(self, mes, ano):
        sql = f'Select sum(valor) from Contas where tipo == "PAGAR" and mes == "{mes}" and ano == "{ano}"'
        self.cursor.execute(sql)
        for linha in self.cursor.fetchall():
            total_pagar = linha[0]
        sql = f'Select sum(valor) from Contas where tipo == "RECEBER" and mes == "{mes}" and ano == "{ano}"'
        self.cursor.execute(sql)
        for linha in self.cursor.fetchall():
            total_receber = linha[0]
        sql = f'Select sum(valor) from Contas where tipo == "PAGAR" and situacao =="PAGO" and mes == "{mes}" and ano == "{ano}"'
        self.cursor.execute(sql)
        for linha in self.cursor.fetchall():
            total_pago = linha[0]
        sql = f'Select sum(valor) from Contas where tipo == "PAGAR" and situacao =="" and mes == "{mes}" and ano == "{ano}"'
        self.cursor.execute(sql)
        for linha in self.cursor.fetchall():
            total_a_pagar = linha[0]
        sql = f'Select sum(valor) from Contas where tipo == "PAGAR" and mes == "{mes}" and ano == "{ano}" and categoria=="CARTAO"'
        self.cursor.execute(sql)
        for linha in self.cursor.fetchall():
            total_cartao = linha[0]

        if not total_a_pagar:
            total_a_pagar = "0.00"
        else:
            total_a_pagar = round(total_a_pagar, 2)
        if not total_pagar:
            total_pagar = "0.00"
        else:
            total_pagar = round(total_pagar, 2)
        if not total_pago:
            total_pago = "0.00"
        else:
            total_pago = round(total_pago, 2)
        if not total_receber:
            total_receber = "0.00"
        else:
            total_receber = round(total_receber, 2)
        if not total_cartao:
            total_cartao = "0.00"
        else:
            total_cartao = round(total_cartao, 2)

        # # gera o grafico
        # cars = ['RECEBER', 'PAGAR']

        # data = [total_receber, total_pagar]
        # fig = plt.figure(figsize=(10, 7))
        # plt.title(f'Gr??fico de {mes}/{ano}')
        # plt.pie(data, labels=cars)
        # plt.savefig('grafico.jpg')
        try:
            os.remove('grafico.jpg')
            print('removido')
        except:
            pass

        # Pie chart
        labels = ['RECEBER', 'PAGAR']
        sizes = [total_receber, total_pagar]
        # colors
        colors = ['#66b3ff', '#ff9999']
        # explsion
        explode = (0.05, 0.05)

        plt.pie(sizes, colors=colors, autopct='%1.1f%%',
                startangle=90, pctdistance=0.85, explode=explode)

        # draw circle
        # centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig = plt.gcf()
        # fig.gca().add_artist(centre_circle)
        # Equal aspect ratio ensures that pie is drawn as a circle
        # ax1.axis('equal')
        plt.rcParams.update({'font.size': 16})
        plt.tight_layout()

        plt.savefig('grafico.png', transparent=True)
        plt.close()

        return f'Resumo do M??s {mes}/{ano}\n\nTotal a receber R${total_receber}\nTotal a pagar R${total_pagar}\nTotal Cart??o Cr??dito R${total_cartao}\nTotal pago R${total_pago}\nFalta pagar R${total_a_pagar}\n'


if __name__ == '__main__':
    a = Contas('db_contas.db')
    a.criartabela()
    # print(a.exibeResumo(10, 2022))
    # a.editar(8, '1salario', '100.00', '3/5', '2002',
    #          '11', '31', 'ok', 'receber', 'casa')
    # print(a.listar_tudo())
    # print(a.buscar_tipos('receber', '11', '2002'))
    a.listar_id('11')
    # a.inserir('1salario', '100.00', '5', '2002',
    #           '09', '31', '', 'receber', 'casa')
