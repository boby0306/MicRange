from scipy.io.wavfile import read, write
from scipy.signal import butter, sosfilt
import numpy as np

from . import by3OctBand


def ene2dB(by3OctEne, power):
    return 10 * np.log10((by3OctEne / power))


def getpower(fileDirectory):
    fs, data = read(fileDirectory)
    floatData = data.astype("float32")
    power = (floatData * floatData).mean()
    return power


def by3OctAnalyze(fileDirectory):
    fs, data = read(fileDirectory)
    by3OctEne = []
    for f in by3OctBand.fList:
        lowcut = by3OctBand.rangeDic[f][0]
        highcut = by3OctBand.rangeDic[f][1]
        filtData = bandPass(data, lowcut, highcut, fs)
        power = (filtData * filtData).mean()
        by3OctEne.append(power)
    return by3OctEne


#----------------------------------------------
#各バンド分析
#---------------------------------------------
def bandPass(data, lowcut, highcut, fs, order=8):
    sos = mk_bandPassFilter(lowcut, highcut, fs, order=order)
    filtData = sosfilt(sos, data)
    return filtData

def mk_bandPassFilter(lowcut, highcut, fs, order=8):
    fnyq = 0.5 * fs
    low = lowcut / fnyq
    high = highcut / fnyq
    sos = butter(order, [low, high], btype="bandpass", output="sos")  # 発散するので2次セクション化
    return sos
