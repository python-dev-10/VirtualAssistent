class TestAplicacao():
    def __init__(self,texto=""):
        super().__init__()
        print("|testes|")
        self.test_ouvir()
        self.test_reconhecer()
        self.test_oque()
        self.test_qual()
    def test_ouvir(self):
        from reconhecimento import ouvir
        for retorno in ouvir():
            retornou=retorno
        print("|teste[1]|ouvir|",retorno)
    def test_reconhecer(self):
        from central import reconhecer
        for retorno in reconhecer():
            retornou=retorno
        print("|teste[2]|reconhecer|",retorno)
    def test_oque(self):
        from pesquisar import oque
        retorno=oque("pesquisar universidade catolica")
        print("|teste[3]|oque|",retorno)
    def test_qual(self):
        from abrir import qual
        retorno=qual("abrir chrome")
        print("|teste[4]|qual|",retorno)
# Iniciar
if __name__ == "__main__":
    TestAplicacao()
