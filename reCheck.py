
# coding: utf-8

# In[1]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'ファイル名.ipynb'])

from analyze import bandpass
import csv
import numpy as np


# ## Z特性

# In[2]:


analyzeList = ("SLM", "myApp", "noset", "low", "high")
forCSV = []
for tmp in analyzeList:
    nameList = [tmp]
    caliFile = "./data/" + tmp + "_cali_30s.wav"
    cali = np.array([bandpass.getpower(caliFile)])
    ambientFile = "./data/" + tmp + "_ambient_30s.wav"
    ambient = np.array([bandpass.getpower(ambientFile)])
    overAll =94.0 + bandpass.ene2dB(ambient,cali)
    nameList.extend(overAll)
    forCSV.append(nameList)
    
with open("OA(Z).csv","a") as f:
    writer = csv.writer(f)
    writer.writerows(forCSV)


# ## Band

# In[10]:


analyzeList = ("SLM", "myApp")
forCSV = []
for tmp in analyzeList:
    nameList = [tmp]
    caliFile = "./data/" + tmp + "_cali_30s.wav"
    cali = np.array([bandpass.getpower(caliFile)])
    ambientFile = "./data/" + tmp + "_ambient_30s.wav"
    bandEne = bandpass.by3OctAnalyze(ambientFile)
    banddB  = bandpass.ene2dB(bandEne,cali) + 94.0
    nameList.extend(list(map(lambda i:i, banddB)))
    forCSV.append(nameList)
with open("ambient_Band.csv","a", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(forCSV)

