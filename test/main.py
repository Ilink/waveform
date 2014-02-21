import json
from pylab import *

import parsers
import wave
import noise

if __name__ == '__main__':
    f = open("data/51004.data_spec", "r")
    spectralData = parsers.parseSpectralWave(f)
    data = spectralData[0]
    x = []
    y = []

    i = 0
    for freq in data["freqs"]:
        x.append(freq[0])
        y.append(freq[1])

    f.close()

    # figure()
    # plot(x, y, 'r')
    # xlabel('x')
    # ylabel('y')
    # title('title')
    # show()


    # def samplemat(dims):
    #     """Make a matrix with all zeros and increasing elements on the diagonal"""
    #     aa = zeros(dims)
    #     for i in range(min(dims)):
    #         aa[i, i] = i
    #     return aa

    mat = [[0]*5 for i in range(5)]
    mat[0][0] = 10

    # # Display 2 matrices of different sizes
    # dimlist = [(12, 12), (15, 35)]
    # for d in dimlist:
    #     matshow(samplemat(d))

    # # Display a random matrix with a specified figure number and a grayscale
    # # colormap

    mat = wave.genDirectionalSpectrum(64, 64, 0.1, 0.1, 0.1, 0.1)
    matshow(mat, cmap=cm.gray)
    show()