import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from googletrans import Translator

model= keras.models.load_model('src/modelo.h5')
class_names= ['Bear', 'Brown bear', 'Bull', 'Butterfly', 'Camel', 'Canary', 'Caterpillar', 'Cattle', 'Centipede', 'Cheetah', 'Chicken', 'Crab', 'Crocodile', 'Deer', 'Duck', 'Eagle', 'Elephant', 'Fish', 'Fox', 'Frog', 'Giraffe', 'Goat', 'Goldfish', 'Goose', 'Hamster', 'Harbor seal', 'Hedgehog', 'Hippopotamus', 'Horse', 'Jaguar', 'Jellyfish', 'Kangaroo', 'Koala', 'Ladybug', 'Leopard', 'Lion', 'Lizard', 'Lynx', 'Magpie', 'Monkey', 'Moths and butterflies', 'Mouse', 'Mule', 'Ostrich', 'Otter', 'Owl', 'Panda', 'Parrot', 'Penguin', 'Pig', 'Polar bear', 'Rabbit', 'Raccoon', 'Raven', 'Red panda', 'Rhinoceros', 'Scorpion', 'Sea lion', 'Sea turtle', 'Seahorse', 'Shark', 'Sheep', 'Shrimp', 'Snail', 'Snake', 'Sparrow', 'Spider', 'Squid', 'Squirrel', 'Starfish', 'Swan', 'Tick', 'Tiger', 'Tortoise', 'Turkey', 'Turtle', 'Whale', 'Woodpecker', 'Worm', 'Zebra']
batch_size = 32
img_height = 180
img_width = 180

def traduza4pt(Frase):
  Tradutor = Translator()
  return Tradutor.translate(Frase,dest="pt").text

def imgarquivo(frase):
    palavras=frase.replace(":"," ")
    palavras=palavras.split()
    for palavra in palavras:
        if palavra == 'identifique':
            arquivo = palavras[palavras.index('identifique') + 1]
            animal = "/mnt/c/Users/Jopes/Pictures/"+str(arquivo)
            return idanimal(animal)
    
def idanimal(animal):
    img = tf.keras.utils.load_img(animal, target_size=(img_height, img_width))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) 
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    volta=[]
    volta.append(str(class_names[np.argmax(score)]))
    volta.append(str(100 * np.max(score)))
    return "O Animal é {} com {:.2f}% de certeza.".format(traduza4pt(class_names[np.argmax(score)]), 100 * np.max(score))