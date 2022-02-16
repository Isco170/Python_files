import os
# Renomear ficheiro
# os.rename('./files/Amor.pdf', './files/Eu.pdf')

# Apagar ficheiro
# os.remove('./files/1.pdf')

# Listar ficheiros
# ficheiros = os.listdir('./files')
# print (ficheiros)

# Buscar o nome do ficheiro
nome = os.path.basename('./files/2.pdf')
print(nome)
