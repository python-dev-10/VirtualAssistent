# Aqui é a parte que visa abrir aplicativos
import os
from threading import Thread
#Carrega a lista
def lista():
    with open('app_list.txt', 'r') as arquivo:
        dado = [[dados.replace("\n","") for dados in linha.split('=')] for linha in arquivo]
    return dado
# Gerencia qual programa vai ser aberto
def qual(frase):
    dado=lista()
    tem=False
    volta=""
    for palavra in frase.split():
        for i in range(len(dado)):
            if palavra == dado[i][0]:
                tem = True
                volta +=str(executar(dado[i][0],dado[i][1]))+"\n"
    if tem:
        return volta
    if tem==False:
        return "Assistente: Nao foi possivel abrir o programa solicitado."
# Excecuta o programa em um segundo processo
def executar(nome,comando):
    processo = Thread(target=terminal, args=[comando])
    processo.setDaemon(True)
    processo.start()
    return "Assistente: Abrindo o "+ str(nome) + "."
# Excecuta comando para abrir atravez do terminal
def terminal(comando):
    os.system(comando)

print(lista())