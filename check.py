
# coding: utf-8

# In[ ]:


import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'analyze.ipynb'])


# In[ ]:


from analyze import bandpass
import csv


# In[3]:


fileName = "./data/Cali_30s.wav"
Cali = bandpass.getpower(fileName)


# In[ ]:


analyzeList = ("34dB", "40db", "45dB", "50dB", "ambient")
forCSV = []
for dB in analyzeList:
    tmp = [dB]
    fileName = "./data/" + dB + "_30s.wav"
    power = bandpass.getpower(fileName)
    dB =ban
    tmp.extend(list(map(lambda i:i, banddB)))
    forCSV.append(tmp)


# In[ ]:


analyzeList = ("34dB", "40db", "45dB", "50dB", "ambient")
forCSV = []
for dB in analyzeList:
    tmp = [str(dB) + "dB"]
    fileName = "./data/" + str(dB) + "dB_30s.wav"
    bandEne = bandpass.by3OctAnalyze(fileName)
    power = bandpass.getpower(fileName)
    banddB = bandpass.ene2dB(bandEne, power)
    tmp.extend(list(map(lambda i:i, banddB)))
    forCSV.append(tmp)


# In[5]:


with open("Analyze.csv","a") as f:
    writer = csv.writer(f)
    writer.writerows(forCSV)

