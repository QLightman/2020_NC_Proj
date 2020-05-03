import glob
import skimage.io as io
from skimage.external import tifffile

with tifffile.TiffWriter('pred.tif') as stack:
    for fid in range(30):
        filename = 'data/membrane/423_test/{:d}_predict.png'.format(fid)
        # filename = 'data/membrane/423_test/{:d}.png'.format(fid)
        stack.save(io.imread(filename, as_gray=True))