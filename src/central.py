# Aqui é a central afim de organizar todas as funcionalidades do assitente virtual.
from abrir import qual
from pesquisar import oque
from reconhecimento import ouvir
from alarme import definir
#Verifica comandos de funcionalidades
def verificar(frase):
    #Verifica comando para abrir
    if any(x in frase for x in ["abra","abrir"]):
        return qual(frase)
    #Verifica comando para pesquisar
    if any(x in frase for x in ["pesquise","pesquisar"]):
        return oque(frase)
    #Verifica comando para criar alarme
    if any(x in frase for x in ["alarme"]):
        return definir(frase)
    #Nenhum comando for solicitado
    else:
        return "Assistente: Nao posso te ajudar com isso."
# Reconhece
def reconhecer(nada):
    frase = ouvir()
    for palavra in frase:
        audio=palavra
    retorno_verificar=verificar(audio.lower())
    return audio,retorno_verificar

