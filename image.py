import glob
import skimage.io as io
import numpy as np
from skimage import img_as_ubyte
from skimage.external import tifffile

def tiff(form='data/membrane/pred/{:d}.png'):
    with tifffile.TiffWriter('pred.tif') as stack:
        for fid in range(30):
            filename = form.format(fid)
            img = io.imread(filename)[:, :, 2] * 255
            stack.save(img)


def convert():
    src = 'data/membrane/train/label/'
    dst = 'data/membrane/train/label_rgb/'
    img = np.zeros((512, 512, 3), dtype=np.uint8)
    for fid in range(30):
        filename = src + str(fid) + '.png'
        img[:, :, 2] = (io.imread(filename) / 255)
        io.imsave(dst + str(fid) + '.png', img)


if __name__ == '__main__':
    # tiff()
    convert()