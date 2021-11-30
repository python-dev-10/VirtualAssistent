from logging import info
import requests 
from lxml import html
from googletrans import Translator
#Traduz
def traduza4pt(Frase):
  Tradutor = Translator()
  return Tradutor.translate(Frase,dest="pt").text
def traduza4en(Frase):
  Tradutor2 = Translator()
  return Tradutor2.translate(Frase,dest="en").text
def animal(frase):
  palavras=frase.replace(":"," ")
  palavras=palavras.split()
  for palavra in palavras:
    if palavra == 'infauna':
      NomeDoanimal = palavras[palavras.index('infauna') + 1]
      return animal_infos(str(traduza4en(NomeDoanimal)))
def animal_infos(NomeAnimal):
  informas={}
   #Define o animal
  Animal = traduza4en(NomeAnimal)
  #Define o local dos dados
  url='https://a-z-animals.com/animals/'+str(Animal)+'/'
  #Requisita a pagina
  req = requests.get(url)  
  #transoforma a pagina para leitura
  tree = html.fromstring(req.content) 
  #Pega Nome Reino Familia Classe
  informas['Nome'] = Animal
  for num in range(1,6):
    path = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[5]/div[1]/dl/dt['+str(num)+']/a'
    elemento = tree.xpath(path)
    if elemento[0].text == 'Kingdom':
      path2 = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[5]/div[1]/dl/dd['+str(num)+']'
      elemento = tree.xpath(path2)
      informas['Reino'] = elemento[0].text
    if elemento[0].text == 'Class':
      path2 = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[5]/div[1]/dl/dd['+str(num)+']'
      elemento = tree.xpath(path2)
      informas['Classe'] = elemento[0].text
    if elemento[0].text == 'Family':
      path2 = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[5]/div[1]/dl/dd['+str(num)+']'
      elemento = tree.xpath(path2)
      informas['Familia'] = elemento[0].text
  #Pega Estatus de conservação
  for num in range(1,2):
    path = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[5]/div['+str(num)+']/h2[2]'
    elemento = tree.xpath(path)
    if elemento[0].text.find("Conservation Status"):
      path2 = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[5]/div[1]/ul/li/a'
      elemento = tree.xpath(path2)
      informas['Estatus de conservação'] = elemento[0].text
  #Pega Localizacao
  for num in range(1,2):
    path = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[5]/div[2]/h2'
    elemento = tree.xpath(path)
    if elemento[0].text.find("Locations"):
      path2 = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[5]/div[2]/ul/li/a'
      elemento = tree.xpath(path2)
      informas['Localizacao'] = elemento[0].text
  #Pega oque come, alimentacao,populacao,ameaca,habitade e dieta
  for num in range(1,6):
    path = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[6]/div/div[1]/div[1]/dl/div[1]/div/dt['+str(num)+']/a'
    elemento = tree.xpath(path)
    if elemento[0].text == 'Prey' or elemento[0].text == 'Main Prey':
      path2 = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[6]/div/div[1]/div[1]/dl/div[1]/div/dd['+str(num)+']'
      elemento = tree.xpath(path2)
      informas['Alimenta-se de'] = elemento[0].text
    if elemento[0].text == 'Estimated Population Size':
      path2 = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[6]/div/div[1]/div[1]/dl/div[1]/div/dd['+str(num)+']'
      elemento = tree.xpath(path2)
      informas['Estimativa da populacao'] = elemento[0].text
    if elemento[0].text == 'Biggest Threat':
      path2 = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[6]/div/div[1]/div[1]/dl/div[1]/div/dd['+str(num)+']'
      elemento = tree.xpath(path2)
      informas['Maior ameaca'] = elemento[0].text
    if elemento[0].text == 'Habitat':
      path2 = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[6]/div/div[1]/div[1]/dl/div[1]/div/dd['+str(num)+']'
      elemento = tree.xpath(path2)
      informas['Habitate'] = elemento[0].text
    if elemento[0].text == 'Diet':
      path2 = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[6]/div/div[1]/div[1]/dl/div[1]/div/dd['+str(num)+']'
      elemento = tree.xpath(path2)
      informas['Dieta'] = elemento[0].text
  #Pega oque come, alimentacao,populacao,ameaca,habitade e dieta
  for num in range(1,5):
    path = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[6]/div/div[1]/div[1]/dl/div[2]/div/dt['+str(num)+']/a'
    elemento = tree.xpath(path)
    if elemento[0].text == 'Habitat':
      path2 = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[6]/div/div[1]/div[1]/dl/div[2]/div/dd['+str(num)+']'
      elemento = tree.xpath(path2)
      informas['Habitate'] = elemento[0].text
    if elemento[0].text == 'Diet':
      path2 = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[6]/div/div[1]/div[1]/dl/div[2]/div/dd['+str(num)+']'
      elemento = tree.xpath(path2)
      informas['Dieta'] = elemento[0].text
    if elemento[0].text == 'Prey' or elemento[0].text == 'Main Prey':
      path2 = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[6]/div/div[1]/div[1]/dl/div[2]/div/dd['+str(num)+']'
      elemento = tree.xpath(path2)
      informas['Alimenta-se de'] = elemento[0].text
    if elemento[0].text == 'Estimated Population Size':
      path2 = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[6]/div/div[1]/div[1]/dl/div[2]/div/dd['+str(num)+']'
      elemento = tree.xpath(path2)
      informas['Estimativa da populacao'] = elemento[0].text
    if elemento[0].text == 'Biggest Threat':
      path2 = '//*[@id="content-wrapper"]/div[1]/main/article/div[1]/div[6]/div/div[1]/div[1]/dl/div[2]/div/dd['+str(num)+']'
      elemento = tree.xpath(path2)
      informas['Maior amaca'] = elemento[0].text
  volta=""
  for key, value in informas.items():
    volta+= 'Assistente:' + str(key)+':'+str(traduza4pt(value))+"\n"
  return volta

