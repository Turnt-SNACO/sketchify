import click
from time import sleep
import logging
import imageio
import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

def dodge(front,back):
    result=front*255/(255-back) 
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')

def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

@click.command()
@click.option('--img_url', default='', help='Url to the image to process')
@click.option('--img_path', default='', help='path to the image file')
def run(img_url, img_path):
  if img_path:
    pass
  elif img_url:
    img = img_url

    s = imageio.imread(img)
    g=grayscale(s)
    i = 255-g

    b = scipy.ndimage.filters.gaussian_filter(i,sigma=10)
    r= dodge(b,g)

    # %matplotlib inline 
    plt.imshow(r, cmap="gray")
    sleep(10)
  else:
    print('You must provide at least a url or path to an image.')
    exit(1)

if __name__ == '__main__':
  run()