from math import *

from noise import SimplexNoise

def genDirectionalSpectrum(width, height, R1, R2, a1, a2):
    data = [[0]*height for i in range(width)]
    noiseGen = SimplexNoise()
    for y in range(0, height):
        for x in range(0, width):
            # r = sqrt(width*width + height*height)
            theta = atan2(y, x)
            freq = 1.0/pi * (0.5+R1*cos(theta-a1) + R2*cos(2*(theta-a2)))
            noiseVal = noiseGen.noise2(x, y)
            data[x][y] = freq
    return data

def trochoid(x, y, wavelength, freq, meanDir, w, phase, dt):
    k = 2*pi / wavelength
    return k*(x*cos(meanDir)+y*sin(meanDir))-w*dt+phase
