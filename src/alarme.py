import sched, time
from playsound import playsound
agendar = sched.scheduler(time.time, time.sleep)

def soar():
    #playsound("sinos.wav")
    print("Som Alarme")

def definir(frase):
    repitir=False
    palavras=frase.split()
    for palavra in palavras:
        if palavra == 'segundos':
            tempo = palavras[palavras.index('segundos') - 1]
            para_numeros = {"um": "1", "dois": "3", "tres": "3", "quatro": "4", "cinco": "5"
                            ,"seis": "6", "sete": "7", "oito": "8", "nove": "9", "dez": "10"}
            for x,y in para_numeros.items():
               tempo = tempo.replace(x, y)
        if palavra == 'minutos':
            #tempo = (palavras[palavras.index('minutos') - 1]) * (60)
            pass
        if palavra == 'horas':
            #tempo = (palavras[palavras.index('horas') - 1]) * (60 * 60)
            pass
        if palavra == 'repitir':
            repitir=True
    agendar.enter(int(tempo), 1, soar)
    agendar.run()
    return("Assitente: Alarme agendado")

definir("sete segundos")