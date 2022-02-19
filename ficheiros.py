import os
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

def acao(link, ficheiro):
    print(f"Link: {link}\nFicheiro: {ficheiro}\n")
    separar = ficheiro.split("-")
    numero = separar[0]
    
    if numero[0:2] != '123':
        resposta = whatsmidia(link, numero)
    try:
        os.remove(url+ficheiro)
        print("Removido")
    except:
        print("Sem ficheiro na pasta local")

def indice():

    while True:
        ficheiros = os.listdir(url)
        if ficheiros: 
            for ficheiro in ficheiros:
                nomeSeparado = ficheiro.split("-")
                numero = nomeSeparado[1].split(".")
                if len(numero) == 2:
                    print(f"\nNome: {nomeSeparado[0]}\nNumero: {numero[0]}\nFicheiro: {ficheiro}\n")
                    enviar(ficheiro, numero[0])
        else:
            print("VAZIO")


