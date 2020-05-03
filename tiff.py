import glob
import skimage.io as io
import numpy as np
from skimage import img_as_ubyte
from skimage.external import tifffile

def tiff(form='data/membrane/pred/{:d}.png'):
    with tifffile.TiffWriter('pred.tif') as stack:
        for fid in range(30):
            filename = form.format(fid)
            img = io.imread(filename)[:, :, 2]
            stack.save(img)


def convert():
    src = 'data/membrane/'
    dst = 'data/membrane_rgb/'
    dirs = ['train/image/', 'train/label/', 'test/']
    img = np.zeros((512, 512, 3), dtype=np.uint8)
    for dir in dirs:
        for fid in range(30):
            filename = src + dir + str(fid) + '.png'
            print(filename)
            img[:, :, 2] = io.imread(filename)
            io.imsave(dst + dir + str(fid) + '.png', img)


if __name__ == '__main__':
    tiff()
    # convert()