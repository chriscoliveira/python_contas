import sqlite3
from playwright.sync_api import sync_playwright
from time import sleep
import os
from bs4 import BeautifulSoup
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

    def buscar_tipos(self, vtipo, vmes, vano):
        # if termo == 'pagar':
        # WHERE tipo LIKE ? AND ano LIKE ? AND mes LIKE ?  ORDER BY dia"
        sql = "SELECT * FROM contas WHERE tipo LIKE ? and mes LIKE ? and ano  LIKE ? order by dia"
        self.cursor.execute(sql, (vtipo, vmes, vano))
        # , '2022', '09'

        retorno = []
        retorno.append(f'conta \t\t\tcategoria: \t\tParcela:\t\tValor\t\tVencimento\tSituação:'
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

            retorno.append(f'{conta: <30} \t{str(categoria): <20}\t\t {str(parcela): <10} \tR${str(valor): <10} \t{str(dia)}-{str(mes)}-{str(ano)} \t{situacao}\t\t\t:{str(id)}'
                           )
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
        if not total_a_pagar:
            total_a_pagar = "0,00"
        if not total_pagar:
            total_pagar = "0,00"
        if not total_pago:
            total_pago = "0,00"
        if not total_receber:
            total_receber = "0,00"

        return f'Resumo do Mês {mes}/{ano}\n\nTotal a receber R${total_receber}\nTotal a pagar R${total_pagar}\nTotal pago R${total_pago}\nFalta pagar R${total_a_pagar}\n'


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
