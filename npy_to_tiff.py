import os
import sys
import numpy as np
import tifffile


if __name__ == "__main__" :
    for i in sys.argv[1:]:
        data = np.load(i)
        i += '.tiff'
        tifffile.imwrite(i, data)
