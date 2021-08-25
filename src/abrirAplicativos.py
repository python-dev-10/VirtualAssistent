#Aqui ficará a parte que interage com o sistema operacional
import os
def abrirPrograma(frase):
    #Abrindo Google chrome
    if "chrome" in frase:
        os.system("start Chrome.exe")
    #Abrindo Bloco de Notas
    if "bloco de notas" in frase:
        t=os.system("notepad")
        print("depois"+t)
        return
    #Abrindo Excel
    if "excel" in frase:
        os.system("start excel.exe")
    #Abrindo o Visual Studio Code
    if "vscode" in frase:
        os.system("code")
    #Se nao achar o programa
    else:
        return