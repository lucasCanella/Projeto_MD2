import datetime
import os
import csv
import tabulate # Abra o terminal e execute: pip install tabulate
import pandas as pd

def perguntar_genero():
    genero = input('Qual o seu gênero? \n[1] Masculino \n[2] Feminino \n[3] Outro\nDigite aqui:')
    if genero == '1':
        return 'Masculino'
    if genero == '2':
        return 'Feminino'
    if genero == '3':
        return 'Outro'
    else:
        os.system("cls")
        print('Selecione uma opção válida!')
        return perguntar_genero()
        

class Perguntas():
    def __init__(self, pergunta_1, pergunta_2, pergunta_3, pergunta_4):
        os.system("cls")
        while True:
            try:
                self.pergunta_1 = int(input(pergunta_1))
                if self.pergunta_1 == 1:
                    self.pergunta_1 = 'Sim'
                    break
                elif self.pergunta_1 == 2 :
                    self.pergunta_1 = 'Não'
                    break
                elif self.pergunta_1 == 3:
                    self.pergunta_1 = 'Não sei responder'
                    break
                else:
                    os.system("cls")
                    print('Opção inválida.\nEscolha uma das opções!!')
            except ValueError:
                os.system("cls")
                print('Opção inválida,digite o número correspondente da opção para escolhe-la.')
        os.system("cls")
        while True:
            try:
                self.pergunta_2 = int(input(pergunta_2))
                if self.pergunta_2 == 1 :
                    self.pergunta_2 = 'Sim'
                    break 
                elif self.pergunta_2 == 2 :
                    self.pergunta_2 = 'Não'
                    break
                elif self.pergunta_2 == 3:
                    self.pergunta_2 = 'Não sei responder'
                    break
                else:
                    os.system("cls")
                    print('Opção inválida.\nEscolha uma das opções!!')
            except ValueError:
                os.system("cls")
                print('Opção inválida,digite o número correspondente da opção para escolhe-la.')
        os.system("cls")
        while True:
            try:
                self.pergunta_3 = int(input(pergunta_3))
                if self.pergunta_3 == 1 :
                    self.pergunta_3 = 'Sim'
                    break
                elif self.pergunta_3 == 2 :
                    self.pergunta_3 = 'Não'
                    break
                elif self.pergunta_3 == 3:
                    self.pergunta_3 = 'Não sei responder'
                    break
                else:
                    os.system("cls")
                    print('Opção inválida.\nEscolha uma das opções!!')
            except ValueError:
                os.system("cls")
                print('Opção inválida,digite o número correspondente da opção para escolhe-la.')
        os.system("cls")
        while True:
            try:
                self.pergunta_4 = int(input(pergunta_4))
                if self.pergunta_4 == 1 :
                    self.pergunta_4 = 'Sim'
                    break
                elif self.pergunta_4 == 2 :
                    self.pergunta_4 = 'Não'
                    break
                elif self.pergunta_4 == 3:
                    self.pergunta_4 = 'Não sei responder'
                    break
                else:
                    os.system("cls")
                    print('Opção inválida.\nEscolha uma das opções!!')
            except ValueError:
                os.system("cls")
                print('Opção inválida,digite o número correspondente da opção para escolhe-la.')
        os.system("cls")


class Entrevistados():
    
    def __init__(self, p1, p2, p3, p4): # p = pergunta 
        count = 0
        while True:
            count += 1 
            self.pessoa = []
            while True :
                idade = input(f"Participante {count}:\nQual a sua idade?(Digite 00 para sair do programa.)\n")
                if idade.isnumeric():
                    if idade == '00':
                        os.system("cls")
                        print('Saindo...')
                        self.__tabela = Tabela(todos_entrevistados)
                        self.__tabela.criarTabela()
                        self.__tabela.mostrarTabela()
                        exit()
                    idade = int(idade)
                    if (idade > 120)or (idade < 0):
                        os.system("cls")
                        print('Idade inválida.\nTente novamente...')
                        
                    else:
                        break
                else:
                    os.system("cls")
                    print('Idade inválida.\nTente novamente...')
            os.system("cls")        
            self.pessoa.append(idade)
            self.pessoa.append(perguntar_genero())
            #print(self.pessoa) conferir o resultado.
            self.perguntas = Perguntas(p1, p2, p3, p4)
            self.pessoa.append(self.perguntas.pergunta_1)
            self.pessoa.append(self.perguntas.pergunta_2)
            self.pessoa.append(self.perguntas.pergunta_3)
            self.pessoa.append(self.perguntas.pergunta_4)
            agora = datetime.datetime.now()
            data = agora.strftime('%d/%m/%y')
            self.pessoa.append(data)
            hora = agora.strftime('%I:%M %p')
            self.pessoa.append(hora)
            todos_entrevistados.append(self.pessoa)

            
class Tabela():
    def __init__(self,lista):
        self.__lista = lista

    def criarTabela(self): # Equivalente a um set para a tabela
        arquivo_csv = open('entrevistados.csv', 'w', encoding='utf-8', newline = '')
        writer = csv.writer(arquivo_csv)
        writer.writerow(['Idade', 'Genero', 'Resposta_1', 'Resposta_2', 'Resposta_3', 'Resposta_4', 'Data da resposta.', 'Hora da resposta.'])
        for data_list in self.__lista:
            writer.writerow(data_list)
        arquivo_csv.close()

    def mostrarTabela(self):
        self.__tabela = pd.read_csv('entrevistados.csv',sep = ',')
        print(tabulate.tabulate(self.__tabela, headers = 'keys',tablefmt = 'github',showindex=range(1,len(todos_entrevistados)+1)))

os.system("cls")
print('Olá! Estamos representando o IRTE (Instituto Resiliente de Tecnologia e Estatística), para participar da nossa pesquisa, responda as perguntas a seguir:')
todos_entrevistados =[]
tabela = Tabela(todos_entrevistados)
pergunta_1 = (f"Pergunta 1: Você se vê mudando de área de trabalho atual para a de tecnologia?\n 1.Sim \n 2.Não \n 3.Não sei responder\nDigite aqui: ") 
pergunta_2 = (f"Pergunta 2: A tecnologia é uma área que você tem interesse?\n 1.Sim \n 2.Não \n 3.Não sei responder\nDigite aqui: ")  
pergunta_3 = (f"Pergunta 3: Você já possui algum conhecimento sobre programação?\n 1.Sim \n 2.Não \n 3.Não sei responder\nDigite aqui: ")  
pergunta_4 = (f"Pergunta 4: Caso tenha interesse, você se inscreveria em algum curso para aprender mais sobre tecnologia?\n 1.Sim \n 2.Não \n 3.Não sei responder\nDigite aqui: ")  

dados_apurados = Entrevistados(pergunta_1, pergunta_2, pergunta_3, pergunta_4 )

