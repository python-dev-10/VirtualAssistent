#Aqui vai ser a UI/UX da aplicacao
import kivy
#from centralAplicacao import reconhecimentoVoz
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from centralAplicacao import *
from threading import Thread

from reconhecimento_de_voz import *


#Dimensões da janela
Window.size = (410, 710)
#Cor de fundo da janela
Window.clearcolor = (1, 1, 1, 1)
#Interface gráfica
class Cortina(App):
    #Monta a tela
    def build(self):
        self.icon = 'img/mic.png'
        botao=Button(
            text = 'Mic',
            size_hint = (.1, .1),
            pos_hint = {"x":.9, "y":0.},
            on_press=self.test)
        return botao
    #Reconhecimento de voz    
    def test(self,obj):
        for respostas in ouvir_voz():
            print("test/ouvir_voz retornou: ",respostas)
#Inicia a aplicacao
if __name__ == "__main__":
    Cortina().run()
    