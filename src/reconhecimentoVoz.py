#Aqui ficará o reconhecimento de voz da aplicacao
import speech_recognition
import time
#Ouvir o microfone
def ouvir_voz():
    #Microfone
    microfone = speech_recognition.Recognizer()
    #Ouvindo o microfone
    while True:
        try:
            with speech_recognition.Microphone() as source:
                microfone.adjust_for_ambient_noise(source)
                audio = microfone.listen(source)
                frase = microfone.recognize_google(audio,language='pt-BR')
                return frase
        #Caso nao reconheca o audio
        except speech_recognition.RequestError:
            return None
        except speech_recognition.UnknownValueError:
            return None
    #Escuta no maximo 3 segundos
    time.sleep(3)