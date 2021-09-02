#Aqui ficará a central afim de organizar as demais funcionalidades
from reconhecimentoVoz import *
from abrirAplicativos import *
from pesquisarNavegador import *
from multiprocessing.pool import ThreadPool
#Liga o reconhecimento de voz
def reconhecimentoDeVoz():
    frase=ouvirvoz()
    respostas=reconheceu(frase)
    for resposta in respostas:
        yield resposta
#Verifica se é a cortina entendeu oque foi falado
def reconheceu(frase):
    if frase==None:
        yield "Sinto muito, mas não entendi oque disse."
    else:
        yield "Voce disse: " + frase
        fraseLower = frase.lower()
        abrirAlgo(fraseLower)
        PesquisarAlgo(fraseLower)
#Verifica se é para abrir algo
def abrirAlgo(frase):
    if "abra" in frase:
        abrirPrograma(frase)
    if "abrir" in frase:
        abrirPrograma(frase)
#Verifica se é para pesquisar algo
def PesquisarAlgo(frase):
    if "pesquise" in frase:
        pesquisarNoGoogle(frase)
    if "pesquisar" in frase:
        pesquisarNoGoogle(frase)
