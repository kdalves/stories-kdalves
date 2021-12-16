import cv2
import numpy as np

image = cv2.imread('StoriesUploads/teste.png')

def reduzir_imagem(imagem):
  porcetagem_escala = 10
  comprimento = int(imagem.shape[1] * porcetagem_escala / 100)
  altura = int(imagem.shape[0] * porcetagem_escala / 100)
  dimensao_imagem = (comprimento, altura)
  return cv2.resize(imagem, dimensao_imagem, interpolation = cv2.INTER_AREA)

def greyscale(img):
  greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  return greyscale

def invertmask(img):
  imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  invertmask = cv2.bitwise_not(imghsv)
  return invertmask

def painting(img):
  NCLUSTERS = 10
  NRODADAS = 10
  
  height, width, channels = img.shape
  samples = np.zeros([height*width, 3], dtype = np.float32)
  count = 0
  
  for x in range(height):
    for y in range(width):
      samples[count] = img[x][y]
      count += 1
          
  compactness, labels, centers = cv2.kmeans(samples,
                                      NCLUSTERS, 
                                      None,
                                      (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001), 
                                      NRODADAS, 
                                      cv2.KMEANS_RANDOM_CENTERS)
  centers = np.uint8(centers)
  res = centers[labels.flatten()]
  painting = res.reshape((img.shape))
  return painting

def light(img):
  light = cv2.convertScaleAbs(img, beta=50)
  return light

def rouge(img):
  imagehsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  lower_red = np.array([160,100,50])
  upper_red = np.array([180,255,255])
  mask = cv2.inRange(imagehsv, lower_red, upper_red)
  mask_inv = cv2.bitwise_not(mask)
  res = cv2.bitwise_and(img, img, mask=mask)
  background = cv2.bitwise_and(gray, gray, mask = mask_inv)
  background = np.stack((background,)*3, axis=-1)
  rouge = cv2.add(res, background)
  # rouge_re = reduzir_imagem(rouge)
  return rouge

cv2.waitKey(0)
cv2.destroyAllWindows()