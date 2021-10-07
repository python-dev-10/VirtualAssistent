import sched, time
from playsound import playsound
agendar = sched.scheduler(time.time, time.sleep)

def soar():
    playsound("sinos.wav")

def definir(frase):
    repitir=False
    palavras=frase.split()
    for palavra in palavras:
        if palavra == 'segundos':
            tempo = palavras[palavras.index('segundos') - 1]
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
