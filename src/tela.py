# Aqui ficará a parte visual UI/UX da aplicacao
from kivy.uix.boxlayout import BoxLayout 
from kivy.app import App
# Layout
class Conversa(BoxLayout):
    mandar=False
    def texto(self,*args):
        formatado=("Voce disse:"+self.ids.entrada.text).lower()
        self.add(str(self.ids.entrada.text),"usuario")
        self.add(str(verificar(formatado)),"assistente")
        self.ids.entrada.text=""
    def mic(self):
        if self.mandar:
            Clock.schedule_once(self.texto)
        else:
            self.ids.micimg.source='img/audio.gif'
            self.ids.micimg.disabled = True
            self.lados(reconhecer())
            self.ids.micimg.source='img/mic.png'
    def lados(self,retornos):
        for palavras in retornos:
            if any(x in palavras for x in ["Assistente:"]):
                self.add(str(palavras),"assistente")
            if any(x in palavras for x in ["Voce disse:"]):
                self.add(str(palavras),"usuario")     
    def add(self,texto,lado):
        if texto!="":
            if lado == "usuario":
                self.ids.box.add_widget(Mensagem(str(texto.replace("Voce disse:",""))))
            if lado == "assistente":
                self.ids.box.add_widget(Resposta(str(texto.replace("Assistente:",""))))
        self.ids.micimg.source='img/mic.png'
        self.ids.micimg.disabled = False
    def modo(self):
        if self.ids.entrada.text=="":
            self.ids.micimg.source='img/mic.png'
            self.mandar=False
        else:
            self.ids.micimg.source='img/enviar.png'
            self.mandar=True
class Mensagem(BoxLayout):
    def __init__(self,texto=""):
        super().__init__()
        self.ids.usuario.text=texto
class Resposta(BoxLayout):
    def __init__(self,texto=""):
        super().__init__()
        self.ids.assitente.text=texto
# O aplicativo
class Cortina(App):
    # Monta a tela
    def build(self):
        self.icon = 'img/icon.png'
        return Conversa()
# Inicia a aplicacao
if __name__ == "__main__":
    from kivy.clock import Clock
    from kivy.lang import Builder
    from kivy.config import Config
    from kivy.core.window import Window
    from central import reconhecer,verificar
    #Desabilita o multitouch
    Config.set('input', 'mouse', 'mouse,disable_multitouch')
    #Tamanho da janela
    Window.size = (410, 710)
    Window.top = 320
    Window.left = 5
    # Interface gráfica
    Builder.load_file('ui/interface.kv')
    Cortina().run()

