#open files
#Joshua D. Gonzalez
import re
import pandas as pd
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
file = open("wine.data","r")#file name/dir

for line in file:
    value = [values for values in line]
    values = re.split(", |  \n",line)

dtatframe = pd.io.parsers.read_csv('wine.data',header =None, usecols=[3,4,5])

dtatframe.columns = ['colum1', 'colum2', 'colum3']


std_scale = scaler.fit(dtatframe)


dataFrameTransform = std_scale.transform(dtatframe)



# Calculating min max
minMax_scale = scaler.fit(dtatframe)
dataFrameMinMax = minMax_scale.transform(dtatframe)

print("************** MIN MAX **************")
n = 0

for m in dataFrameMinMax:
    print("row",n,": max =", dataFrameMinMax[n,:].max(),"min =", dataFrameMinMax[n,:].min())
    n = n + 1
#print('Feature 1={:.2f}, Feature 2={:.2f} '.format(dataFrameMinMax[:,0].max(), dataFrameMinMax[:,1].max() ))
#print('Feature 1={:.2f}, Feature 2={:.2f} '.format(dataFrameMinMax[:,0].min(), dataFrameMinMax[:,1].min() ))
print("  ")
print("************** after Lamba **************")
n = 0
for m in dataFrameMinMax:
    dataFrameMinMax[n,0] = dataFrameMinMax[n,0] * 2
    dataFrameMinMax[n,1] = dataFrameMinMax[n,1] * 2
    dataFrameMinMax[n,2] = dataFrameMinMax[n,2] * 2
    n = n + 1
    
print(dataFrameMinMax)

