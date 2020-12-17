# To support both python 2 and python 3
#!/usr/bin/python
 #-*- coding: utf8 -*-
from __future__ import division, print_function, unicode_literals

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#df = pd.read_excel("D:\DataPython\First.xlsx", 'dt')
df = pd.read_excel("D:\Machine Learning\Laboratory Blood Test Analysis\ML_Laboratory\input\laokhoa.xlsx", 'laokhoa')
#Remove Duplicate Values based on values of variables "Gender" and "BMI"
#rem_dup=df.drop_duplicates(['Gender', 'BMI'])
#print(rem_dup)
#test = df.groupby(['Gender'])
#print(test.describe())
#print(df)
# Plots in matplotlib reside within a figure object, use plt.figure to create new figure%fig = plt.figure()
# Create one or more subplots using add_subplot, because you can't create blank figure
test= df.groupby(['Patient_Sex'])
test.describe()
meanHST = np.mean(df.HST)     #Using numpy mean function to calculate the mean value
df.HST = df.HST.fillna(meanHST) #replacing missing values in the DataFrame
fig=plt.figure()
ax = fig.add_subplot(1,1,1)
# Variable
ax.hist(df['HST'],bins= 9)
# Labels and Tit
# print(df)
plt.title('Đồ thị phân phối huyết sắc tố')
plt.xlabel('Lượng huyết sắc tố Hemoglobin')
plt.ylabel('Số lượng Bênh nhân - Patients')
plt.show()
#sns.boxplot(df['HST'])
#sns.despine()

plt.boxplot(df['HST']) #Nen dung cai nay de ve
plt.show()
