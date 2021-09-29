# Aqui ficará a parte visual UI/UX da aplicacao
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout 
from central import reconhecer
#Tamanho da janela
Window.size = (410, 710)
Window.top = 320
Window.left = 5
# Interface gráfica
Builder.load_file('ui\interface.kv')
# Layout
class Conversa(BoxLayout):
    def mic(self):
        for retorno in reconhecer():
            self.add(retorno)
    def add(self,texto):
        if texto!="":
            self.ids.box.add_widget(Mensagem(str(texto)))
class Mensagem(BoxLayout):
    def __init__(self,texto=""):
        super().__init__()
        self.ids.label.text=texto
# O aplicativo
class Cortina(App):
    # Monta a tela
    def build(self):
        self.icon = 'img/icon.png'
        return Conversa()
# Inicia a aplicacao
if __name__ == "__main__":
    Cortina().run()

