from scipy.io.wavfile import read, write
from scipy.signal import butter,sosfilt
import by3OctBand.py

def byOctAnalyze(fileDirectory):
    fs, data = read(fileDirectory)
    by3OctEne = []
    for f in by3OctBand.fList:
        lowcut = by3OctBand.rangeDic[f][0]
        highcut = by3OctBand.rangeDic[f][1]
        filtData = bandPass(data, lowcut, highcut, fs)
        power = (filtData * filtData).mean()
        by3OctEne.append(power)
    return by3OctEne

def mk_bandPassFilter(lowcut, highcut, fs, order = 8):
    fnyq = 0.5 * fs
    low  = lowcut / fnyq
    high = highcut / fnyq
    sos = butter(order, [low, high], btype = "bandpass", output = "sos")#発散するので2次セクション化
    return sos

def bandPass(data, lowcut, highcut, fs, order = 8):
    sos = mk_bandPassFilter(lowcut, highcut, fs, order=order)
    filtData = sosfilt(sos, data)
    return filtData