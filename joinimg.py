import numpy as np
from PIL import Image
import glob
import sys


print("To join vertically: py -m join v")

print("To join horizzontally: py -m join h")


def join():
    list_im = glob.glob("*.png")
    imgs = [Image.open(i) for i in list_im]
    # resize images to the smallest one
    min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
    imgs_comb = np.hstack((np.asarray(i.resize(min_shape)) for i in imgs))

    # save that beautiful picture
    if sys.argv[1] == "v":
        # for a vertical stacking it is simple: use vstack
        imgs_comb = np.vstack((np.asarray(i.resize(min_shape)) for i in imgs))
        imgs_comb = Image.fromarray(imgs_comb)
        imgs_comb.save('vertical.png')

    else:
        imgs_comb = Image.fromarray(imgs_comb)
        imgs_comb.save('horizontal.png')


join()
