import glob
import skimage.io as io
from skimage.external import tifffile

with tifffile.TiffWriter('pred.tif') as stack:
    for filename in glob.glob('data/membrane/423_test/*.png'):
        stack.save(io.imread(filename))