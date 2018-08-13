import numpy as np
import matplotlib.pyplot as pyp

#Inputs:
name = 'dog.png'

def mread (name):
    if(name[-3:] == 'png'):
        return np.uint8((pyp.imread(name)*255))
    else:
        return np.uint8(pyp.imread(name))

#Return number of Channel
def nchannels(name):
    #print(nome.shape[2])
    return np.size(name[0][0])

def size(name):
    tam = []
    #Invertendo a posição dos de Largura e Comprimento
    tam.append(name.shape[1]) #Largura
    tam.append(name.shape[0]) #Altura
    return tam

def rgb2gray(name):
    if (nchannels(name) == 4):
        return np.dot(name, [0.299, 0.587, 0.114, 0]).astype(int)
    else:
        return np.dot(name, [0.299, 0.587, 0.114]).astype(int)

def imgrayread(name):
    if (nchannels(name) == 1):
        return name
    else:
        return rgb2gray(name)

def imshow(image):
    if (nchannels(image) == 1):
        pyp.imshow(image, cmap='gray') # CMAP - Warning when image stay state gray
        pyp.show()  # Force image show
    else:
        #if (nchannels(image) == 3): ##Test
        pyp.imshow(image)
        pyp.show()

#To Do Test this fuction
def tresh(image, limit):
    max = 255 #max value in image
    #Mount image with zeros in dimension of input image
    imgzero = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8) #Shape height and width
    #Search in image point in equal or high limit in image input
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j] >= limit:
                imgzero[i][j] = max #save value in matrix zeros with max input image
    return imgzero


def negative(image):
    if nchannels(image) == 1: #Gray Image
        imgnegative = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8) #Shape height and width
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                imgnegative[i][j] = 255 - image[i][j]
        return imgnegative
    else: #Other images with three channels
        imgnegative = np.zeros((image.shape[0], image.shape[1], image.shape[2]), dtype=np.uint8)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                for k in range(image.shape[2]):
                    imgnegative[i][j][k] = 255 - image[i][j][k]
        return imgnegative

def contrast(image, r, m):
    if nchannels(image) == 1: #Gray Image
        imgcontrast = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8) #Shape height and width
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                imgcontrast[i][j] = r*(image[i][j] - m) + m
                return imgcontrast
    else: #Other images with three channels
        imgcontrast = np.zeros((image.shape[0], image.shape[1], image.shape[2]), dtype=np.uint8)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                for k in range(image.shape[2]):
                    imgcontrast[i][j][k] = r*(image[i][j][k] - m) + m
        return imgcontrast

def hist(image):
    if nchannels(image) == 1:
        hist = np.zeros((256, 1), dtype=np.uint)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                hist[int(image[i][j])] += 1
        return hist
    else:
        hist = np.zeros((256, 3), dtype=np.uint)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                hist[int(image[i][j][0])] += 1
                hist[int(image[i][j][1])] += 1
                hist[int(image[i][j][2])] += 1
        return hist


def showhist(hist, bin = 1):
    x_axis = []
    for i in range(256): #Begin axis X 0 -> 255
        x_axis.append(i) #Add in vector position this value
    if hist.shape[1] == 1:
        pyp.bar(x_axis, color='black', align='center')
    else:
        red_bar = pyp.bar(x_axis, hist.transpose()[0], color='red', align='center')
        green_bar = pyp.bar(x_axis, hist.transpose()[1], color='green', align='center')
        blue_bar = pyp.bar(x_axis, hist.transpose()[2], color='blue', align='center')
        pyp.show()


##Read Image
img = mread(name)
hist = hist(img)
showhist(hist)
#print(i# mg)
#negative = negative(img)
#print(negative)
#contrast = contrast(img, 2, 10)
#imshow(contrast)
#tresh = tresh(img, 244)
#print(tresh)
#gray = rgb2gray(img)
#number = nchannels(img)
#print(number)
#Size Image
#size = size(img)
#Number of Channels
#nchannel = nchannels(img)
#To gray image
#gray = imgrayread(img)
#print(nchannel)
#imshow(tresh)
#Verify the image when modify after fuction rgb2gray
