
# coding: utf-8

# In[1]:


from analyze import bandpass
import csv


# In[4]:


analyzeList = (40, 50, 60, 70, 80, 90)
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

