from datetime import datetime
from os import system
import csv
import tabulate # Executar no terminal : pip install tabulate
import pandas as pd

def perguntar(pergunta, lista):
    resposta = input(pergunta)
    if resposta == '1':
        lista.append('Sim')
    elif resposta == '2':
        lista.append('Nao')
    elif resposta == '3':
        lista.append('Nao sei responder')
    else:
        system("cls")
        print('Resposta inválida! Por favor, selecione uma das opções.')
        perguntar(pergunta, lista)

def perguntar_genero():
    genero = input('Qual o seu gênero? \n[1] Masculino \n[2] Feminino \n[3] Outro\nDigite aqui:')
    if genero == '1':
        return 'Masculino'
    if genero == '2':
        return 'Feminino'
    if genero == '3':
        return 'Outro'
    else:
        system("cls")
        print('Selecione uma opção válida!')
        return perguntar_genero()

class Perguntas():
    def __init__(self, pergunta_1, pergunta_2, pergunta_3, pergunta_4):
        self.setpergunta_1(pergunta_1)
        self.setpergunta_2(pergunta_2)
        self.setpergunta_3(pergunta_3)
        self.setpergunta_4(pergunta_4)
        self.respostas = []

    def setpergunta_1(self, pergunta_1):
        self.pergunta_1 = pergunta_1

    def getpergunta_1(self):
        return self.pergunta_1

    def setpergunta_2(self, pergunta_2):
        self.pergunta_2 = pergunta_2

    def getpergunta_2(self):
        return self.pergunta_2
        
    def setpergunta_3(self, pergunta_3):
        self.pergunta_3 = pergunta_3

    def getpergunta_3(self):
        return self.pergunta_3    

    def setpergunta_4(self, pergunta_4):
        self.pergunta_4 = pergunta_4

    def getpergunta_4(self):
        return self.pergunta_4    

    def rodar_perguntas(self, pergunta_1, pergunta_2, pergunta_3, pergunta_4):

        perguntas = [pergunta_1, pergunta_2, pergunta_3, pergunta_4]

        for pergunta in perguntas:
            system("cls")
            perguntar(pergunta, self.respostas)
        data = datetime.now()
        self.respostas.append(data.strftime("%d/%m/%Y %H:%M:%S"))

class Entrevistado():
    def __init__(self, entrevistado_idade, entrevistado_genero, lista):
        self.set_idade(entrevistado_idade)
        self.set_genero(entrevistado_genero)
        lista.append(self.idade)
        lista.append(self.genero)
        self.perguntas = Perguntas(pergunta_1, pergunta_2, pergunta_3, pergunta_4)
        self.perguntas.rodar_perguntas(pergunta_1, pergunta_2, pergunta_3, pergunta_4)

    def set_idade(self, entrevistado_idade):
        self.idade = entrevistado_idade

    def get_idade(self):
        return self.idade

    def set_genero(self, entrevistado_genero):
        self.genero = entrevistado_genero

    def get_genero(self):
        return self.genero

class Tabela():
    def __init__(self,lista):
        self.setlista(lista)

    def setlista(self, lista):
        self.__lista = lista

    def getlista(self):
        return self.__lista

    def criarTabela(self): # Equivalente a um set para a tabela
        arquivo_csv = open('entrevistados.csv', 'w', encoding='utf-8', newline = '')
        writer = csv.writer(arquivo_csv)
        writer.writerow(['Idade', 'Genero', 'Resposta_1', 'Resposta_2', 'Resposta_3', 'Resposta_4', 'Data da resposta.'])
        for data_list in self.__lista:
            writer.writerow(data_list)
        arquivo_csv.close()

    def mostrarTabela(self):
        self.__tabela = pd.read_csv('entrevistados.csv',sep = ',')
        print(tabulate.tabulate(self.__tabela, headers = 'keys',tablefmt = 'github',showindex=range(1,len(self.getlista())+1)))

pergunta_1 = 'Você se vê mudando de área de trabalho atual para a de tecnologia?\n[1] Sim \n[2] Não \n[3] Não sei responder\nResponda Aqui: '
pergunta_2 = 'A tecnologia é uma área que você tem interesse?\n[1] Sim \n[2] Não \n[3] Não sei responder\nResponda Aqui: '
pergunta_3 = 'Você já possui algum conhecimento sobre programação?\n[1] Sim \n[2] Não \n[3] Não sei responder\nResponda Aqui: '
pergunta_4 = 'Caso tenha interesse, você se inscreveria em algum curso para aprender mais sobre tecnologia?\n[1] Sim \n[2] Não \n[3] Não sei responder\nResponda Aqui: '

entrevistados_todos = []

system("cls")
while True:

    dados_entrevistados = []
    print('olá! Estamos representando o IRTE (Instituto Resiliente de Tecnologia e Estatística), para participar da nossa pesquisa, responda as perguntas abaixo:')
    idade = input('Qual a sua idade? ').strip()
    if idade == '0':
        tabela = Tabela(entrevistados_todos)
        tabela.criarTabela()
        tabela.mostrarTabela()
        break
    elif idade.isnumeric() == False:
        system("cls")
        print('Idade Inválida! Por favor, escreva uma idade válida.')
    else:
        genero = perguntar_genero()
        entrevistado = Entrevistado(idade, genero, dados_entrevistados)
        dados_entrevistados += entrevistado.perguntas.respostas
        entrevistados_todos.append(dados_entrevistados)
        system("cls")
        
arquivo_csv = open('entrevistados.csv', 'w')
writer = csv.writer(arquivo_csv)
writer.writerow(['Idade', 'Genero', 'Resposta_1', 'Resposta_2', 'Resposta_3', 'Resposta_4', 'Data e hora da resposta'])
for data_list in entrevistados_todos:
    writer.writerow(data_list)
arquivo_csv.close()