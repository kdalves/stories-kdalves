import cv2
import colorFilter
import numpy as np

class ChangeVideo():
  def __init__(self, cap):
    media = [0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111]
    # cap = cv2.VideoCapture(2)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('StoriesDownloads/video/videoFiltros.mp4',fourcc, 20.0, (640,480))

    mask = np.reshape(media, (3, 3))

    while(True):
      ret, frame = cap.read()
      frame32f = np.float32(frame)
      frameFiltered = cv2.filter2D(frame32f, cv2.CV_32F, mask, anchor=(1, 1), delta=0)

      result = np.uint8(frameFiltered)

      key = cv2.waitKey(10)

      if key != -1:
        key = chr(key)

      if key == '\x1b':
        break

      if key == '1':
        maskgreyscale = colorFilter.greyscale(frame)
        cv2.imshow('greyscale', maskgreyscale)
        filter = maskgreyscale
        cv2.imwrite('StoriesDownloads/images/videoGray.png', maskgreyscale)
      elif key == '2':      
        maskinvertmask = colorFilter.invertmask(frame)
        cv2.imshow('invertmask', maskinvertmask)
        filter = maskinvertmask
        cv2.imwrite('StoriesDownloads/images/videoRadioactive.png', maskinvertmask)
      elif key == '3':      
        painting = colorFilter.painting(frame)
        cv2.imshow('painting', painting)
        filter = painting
        cv2.imwrite('StoriesDownloads/images/videoPainting.png', painting)
      elif key == '4':      
        light = colorFilter.light(frame)
        cv2.imshow('light', light)
        filter = light
        cv2.imwrite('StoriesDownloads/images/videoLight.png', light)
      elif key == '5':      
        rouge = colorFilter.rouge(frame)
        cv2.imshow('rouge', rouge)
        filter = rouge
        cv2.imwrite('StoriesDownloads/images/videoRouge.png', rouge)

      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      
      cv2.imshow("videoFiltros", result)
      out.write(result)
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cap.release()
    out.release()
    cv2.waitKey(0)
    cv2.destroyAllWindows()