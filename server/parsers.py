from datetime import datetime

def parseTimestamp(timeData):
    # EX:
    # YY   MM DD hh mm
    # 2014 02 13 02 00
    timeStr = "%s/%s/%s %s:%s" % (timeData[2], timeData[1], timeData[0], timeData[3], timeData[4])
    return datetime.strptime(timeStr, "%d/%m/%Y %H:%M")

# based on code written by frostymoose
def parseSpectralWave(waveFile):
    waveFile.readline() # ignore first line header
    data = []

    for line in waveFile:
        line = line.replace('(', '').replace(')', '')
        line = line.split()
        timestamp = line[:5]
        sepFreq = float(line[5])
        rawFreqs = line[6:]

        timestamp = parseTimestamp(timestamp)

        freqs = []
        i = 0

        # Format: (amplitude, frequency)
        while i < len(rawFreqs):
            freq = float(rawFreqs[i+1]), float(rawFreqs[i])
            freqs.append(freq)
            i += 2

        data.append({
            "freqs": freqs,
            "sepFreq": sepFreq,
            "timestamp": timestamp.isoformat()
        })

    return data