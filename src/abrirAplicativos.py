#Aqui ficará a parte que interage com o sistema operacional
import os
from threading import Thread
#Gerencia qual programa vai ser aberto
def abrir_programa(frase):
    #Abrindo Google chrome
    if "chrome" in frase:
        abrir_terminal("start Chrome.exe","Google Chrome")
    #Abrindo Bloco de Notas
    if "bloco de notas" in frase:
        abrir_terminal("notepad","Bloco de Notas")
    #Abrindo Excel
    if "excel" in frase:
        abrir_terminal("start excel.exe","Microsoft Excel")
    #Abrindo o Visual Studio Code
    if "vscode" in frase:
        abrir_terminal("code","Visual Studio Code")
    #Abrindo o Visual Studio Code
    if "arquivos" in frase:
        abrir_terminal("explorer","Explorador de arquivos")
    #Abrindo o Microsoft Word
    if "word" in frase:
        abrir_terminal("start winword","Microsoft Word")
    #Se nao achar o programa
    else:
        return "Desulpe, não consigo abrir esse programa."
#Excecuta o programa em um segundo processo 
def abrir_terminal(comandoParaAbrir,Programa):
    processo=Thread(target=executar_programa,args=[comandoParaAbrir])
    processo.start()
    yield "abriu o: "+str(Programa)
#Excecuta comando para abrir atravez do terminal
def executar_programa(comando):
    os.system(comando)


