# Aqui ficará o reconhecimento de voz da aplicacao
import speech_recognition
import time
# Ouvir o microfone
def ouvir():
    # Microfone
    microfone = speech_recognition.Recognizer()
    # Ouvindo o microfone
    while True:
        with speech_recognition.Microphone() as source:
            # microfone.adjust_for_ambient_noise(source)
            audio = microfone.listen(source)
        try:
            # armazena o texto na variavel frase
            frase = microfone.recognize_google(audio, language='pt-BR')
            # se tiver frase imprime ela
            if frase != None:
                yield "Voce disse: " + frase
                break
        # Caso nao reconheca o audio
        except speech_recognition.RequestError:
            # Imprime que nao entendeu
            yield "Assistente: Nao foi possivel entender"
            break
        except speech_recognition.UnknownValueError:
            # Imprime que nao entendeu
            yield "Assistente: Nao foi possivel entender"
            break
    # Escuta no maximo 3 segundos
    time.sleep(3)
