from googletrans import Translator

def traduza(frase):
  palavras=frase.replace(":"," ")
  palavras=palavras.split()
  for palavra in palavras:
    if palavra == 'traduza':
      traduzir_palavra = palavras[palavras.index('traduza') + 1]
      so_frase=frase.replace("voce","").replace("disse","").replace("traduza","").replace(":","")
      print(so_frase)
      return traduza4pt(so_frase)
    if palavra == 'traduzir':
      traduzir_palavra = palavras[palavras.index('traduzir') + 1]
      so_frase=frase.replace("voce","").replace("disse","").replace("traduza","").replace(":","")
      return traduza4pt(so_frase)

def traduza4pt(Frase):
  Tradutor = Translator()
  return "Assistente: "+Tradutor.translate(Frase,dest="pt").text