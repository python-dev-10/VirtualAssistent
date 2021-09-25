# Aqui ficará a central afim de organizar as demais funcionalidades
from reconhecimento_de_voz import *
from abrirAplicativos import *
from pesquisarNavegador import *
from multiprocessing.pool import ThreadPool
# Liga o reconhecimento de voz


def reconhecer_voz():
    frase = ouvir_voz()
    respostas = reconheceu(frase)
    #for resposta in respostas:
        #yield resposta

# Verifica se é a cortina entendeu oque foi falado
def reconheceu(frase):
    if frase == None:
        yield "Sinto muito, mas não entendi oque disse."
    else:
        yield "Voce disse: " + str(frase)
        fraseLower = frase.lower()
        respostas_abrir = abrir_algo(fraseLower)
        for resposta in respostas_abrir:
            yield str(resposta)
        respostas_pesquisar = pesquisar_algo(fraseLower)
        for resposta in respostas_pesquisar:
            yield str(resposta)
# Verifica se é para abrir algo


def abrir_algo(frase):
    if "abra" in frase:
        respostas_abrir = abrir_programa(frase)
        for resposta in respostas_abrir:
            yield str(resposta)
    if "abrir" in frase:
        respostas_abrir = abrir_programa(frase)
        for resposta in respostas_abrir:
            yield str(resposta)
# Verifica se é para pesquisar algo


def pesquisar_algo(frase):
    if "pesquise" in frase:
        yield pesquisar_no_google(frase)
    if "pesquisar" in frase:
        yield pesquisar_no_google(frase)

