import os
import whatsapp
url = './files/'
# Renomear ficheiro
# os.rename('./files/Amor.pdf', './files/Eu.pdf')

# Apagar ficheiro
# os.remove('./files/1.pdf')

# Listar ficheiros
# ficheiros = os.listdir('./files')
# print (ficheiros)

# Buscar o nome do ficheiro
# nome = os.path.basename('./files/2.pdf')
# print(nome)

# Buscar o nome do ficheiro sem extensão
# nome = os.path.splitext(os.path.basename('./files/Francisco Mavie - 258846461323.pdf'))[0]
# print(nome)

# Separar nome do ficheiro
# nomeSeparado = nome.split("-")
# print(nomeSeparado)

def apagarLocalmente(ficheiro):
    try:
        os.remove(url+ficheiro)
    except:
        print("Sem ficheiro na pasta local")

def acao(link, ficheiro):
    separar = ficheiro.split("-")
    numero = separar[0]
    
    if numero[0:2] != '123':
        resposta = whatsapp.send(link, numero)
        if resposta:
            apagarLocalmente(ficheiro)
            print("FATURA ENVIADA")
        else:
            print("Falha no envio da fatura")