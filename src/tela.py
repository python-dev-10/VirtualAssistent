#Aqui vai ser a UI/UX da aplicacao
import kivy
from centralAplicacao import reconhecimentoDeVoz
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
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
        print("test")
#Inicia a aplicacao
if __name__ == "__main__":
    Cortina().run()
    