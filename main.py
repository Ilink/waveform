import json
from pylab import *

import parsers

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

    figure()
    plot(x, y, 'r')
    xlabel('x')
    ylabel('y')
    title('title')
    show()