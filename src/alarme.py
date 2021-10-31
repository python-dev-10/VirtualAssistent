import sched, time
from playsound import playsound
agendar = sched.scheduler(time.time, time.sleep)

def soar():
    playsound("sinos.wav")
    
def verificar_segundos(palavras):
    word = palavras
    if word == 'um': return 1
    if word == 'dois':
        print(f'if word igual a dois : {word}')
        return 2
    if word == 'três' or word == "tres": return 3
    if word == 'quatro': return 4
    if word == 'cinco': return 5
    if word == 'seis': return 6
    if word == 'sete': return 7
    if word == 'oito': return 8
    if word == 'nove': return 9
    if word == 'dez': return 10
    
    

def definir(frase):
    repitir=False
    palavras=frase.split()
    for palavra in palavras:
        if palavra == 'segundos':
            tempo = palavras[palavras.index('segundos') - 1]
            print(f'antes verificar tempo: {tempo}')
            print(type(tempo))
            if tempo.isalpha():
                tempo = verificar_segundos(tempo)
                print(f'tempo: {tempo}')
        if palavra == 'minutos':
            tempo = (palavras[palavras.index('minutos') - 1]) * (60)
        if palavra == 'horas':
            tempo = (palavras[palavras.index('horas') - 1]) * (60 * 60)
        if palavra == 'repitir' or palavra == 'repetir':
            repitir=True
    print(f"tempo: {tempo}")
    agendar.enter(int(tempo), 1, soar)
    agendar.run()
    return("Assitente: Alarme agendado")
