import cv2
import numpy as np

cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

img = cv2.imread('teste.png')

def detection(grayscale, img):    
  face = cascade_face.detectMultiScale(grayscale, 1.3, 5)

  for (xface, yface, wface, hface) in face:        
    imgHeadAccessory= cv2.imread('Filters/graduate.png',-1)
        
    width, depth, _= imgHeadAccessory.shape
    width= int(wface + 0.1* width)
    depth= int(hface* 2/3)
    imgHeadAccessory= cv2.resize(imgHeadAccessory, (width, depth))
        
    centrex= xface + wface/2
    xHeadAccessory= int(centrex-width/2)  
    yHeadAccessory= int(yface- (depth*2/3) )
        
    if xHeadAccessory<0:
      xHeadAccessory=0
    if yHeadAccessory<0:
      yHeadAccessory=0
    y2=int(yHeadAccessory+depth)
    if(y2>= img.shape[0]): 
      y2= img.shape[0]
    x2= int(xHeadAccessory+width)
    if(x2>= img.shape[1]):
      x2= img.shape[1]
           
           
    imgHeadAccessory= imgHeadAccessory[0: y2-yHeadAccessory, 0:x2-xHeadAccessory] 
    bg=  img[yHeadAccessory: y2, xHeadAccessory: x2]
    sg = np.atleast_3d(255 - imgHeadAccessory[:, :,3])/255.0
    np.multiply(bg, sg, out=bg, casting="unsafe")
    np.add(bg, 255-imgHeadAccessory[:, :,0:3] * np.atleast_3d(imgHeadAccessory[:, :,3]), out=bg)
    img[yHeadAccessory: y2, xHeadAccessory: x2] = bg
        
    return img        


cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('graduateVideo.mp4',fourcc, 20.0, (640,480))

cnt=0
while cnt<500:
    _, img = cap.read()
    
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    final = detection(grayscale, img) 
    
    if final is not None:
      cv2.imshow('Video', final) 
      out.write(final)

    key = cv2.waitKey(10)

    if key != -1:
      key = chr(key)

    if key == '\x1b':
      break

    if key == '1':
      cv2.imwrite('StoriesDownloads/graduate.png', final)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break 
    
    cnt+=1
cap.release()
out.release()
cv2.destroyAllWindows() 