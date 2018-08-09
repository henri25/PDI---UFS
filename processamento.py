import numpy as np
import matplotlib.pyplot as pyp

nome = 'dilma.jpg'

def mread (nome):
    if(nome[-3:] == 'png'):
        return np.uint8(np.round(pyp.imread(nome)*255))
    else:
        return np.uint8(pyp.imread(nome))

def nchannels(nome):
    return nome.shape[2]

def size(nome):
    tam = []
    #Invertendo a posição dos de Largura e Comprimento
    tam.append(nome.shape[1]) #Largura
    tam.append(nome.shape[0]) #Altura
    return tam

def rgb2gray(nome):
    return np.dot(nome, [0.299, 0.587, 0.114]).astype(int)


im = mread(nome)
tam = size(im)
tamanho = nchannels(im)
gray = rgb2gray(im)
#Verificar se a imagem nao esta sendo alterada depois da rgb2gray
#print (tam)
pyp.imshow(gray, cmap='gray')
    #CMAP - Avisa que ao imshow que esta em uma camaada
pyp.show()