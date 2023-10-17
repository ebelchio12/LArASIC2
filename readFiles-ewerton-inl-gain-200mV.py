# importing module
from glob import glob
from pandas import *
import time
import sys
import csv
import os.path
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import matplotlib.pyplot as plt
import statistics
import math
import scipy
from scipy.stats import norm
from Makeplots import makeplot

def getColumnRemove(file,column_key,n):
  bl = read_csv(file)
  # converting column data to list
  column = bl[column_key].tolist()

  # remove last elements from column
  column = column[:-n]

  #print(len(column))
  result = []

  # skip files with different formatting
  if len(column) != 35:
    print('len column=',len(column))
    print('file with double measurements(?), skipping file ',file)
    return result

  # remove first elements from column
  column = column[19:]

  for i in column:
    #print(i)
    result.append(float(i))
  #print('')

  return result

#get ENC gain files
files = glob('./**/Gain_Lin_raw_200mV*.csv', recursive=True)

#ENC gain from all chips (files)
enc05=[]
enc1=[]
enc2=[]
enc3=[]


# append each ENC to corresponding list
for i in files:
  #print(i)

  e05 = getColumnRemove(i,'Gain @0.5us',2)
  e1 = getColumnRemove(i,'Gain @1us',2)
  e2 = getColumnRemove(i,'Gain @2us',2)
  e3 = getColumnRemove(i,'Gain @3us',2)

  '''    
    for j in e05:
      print(j)
    print("")

    for j in e1:
      print(j)
    print("")

    for j in e2:
      print(j)
    print("")

    for j in e3:
      print(j)
    print("")
  '''

  enc05.extend(e05)
  enc1.extend(e1)
  enc2.extend(e2)
  enc3.extend(e3)

#mean
enc05_mean=statistics.mean(enc05)
enc1_mean=statistics.mean(enc1)
enc2_mean=statistics.mean(enc2)
enc3_mean=statistics.mean(enc3)

#sd
enc05_sd=statistics.stdev(enc05)
enc1_sd=statistics.stdev(enc1)
enc2_sd=statistics.stdev(enc2)
enc3_sd=statistics.stdev(enc3)

#3 sigma
enc05_sign = enc05_mean - 3*enc05_sd
enc05_sigp = enc05_mean + 3*enc05_sd
enc1_sign = enc1_mean - 3*enc1_sd
enc1_sigp = enc1_mean + 3*enc1_sd
enc2_sign = enc2_mean - 3*enc2_sd
enc2_sigp = enc2_mean + 3*enc2_sd
enc3_sign = enc3_mean - 3*enc3_sd
enc3_sigp = enc3_mean + 3*enc3_sd

total_channels = len(enc05)

#plotting
#'''
nbins=10
xtitle='INL gain (200mV) @0.5$\mu$s, Total channels: %1.0f'%(total_channels)
ytitle='Counts'
unit=''
saveTo='./test-plots/inl_gain_200mV_0.5us-outliers-included.png'
makeplot(enc05,nbins,xtitle,ytitle,unit,saveTo)
#'''

#plotting
#'''
nbins=10
xtitle='INL gain (200mV) @1$\mu$s, Total channels: %1.0f'%(total_channels)
ytitle='Counts'
unit=''
saveTo='./test-plots/inl_gain_200mV_1us-outliers-included.png'
makeplot(enc1,nbins,xtitle,ytitle,unit,saveTo)
#'''

#plotting
#'''
nbins=10
xtitle='INL gain (200mV) @2$\mu$s, Total channels: %1.0f'%(total_channels)
ytitle='Counts'
unit=''
saveTo='./test-plots/inl_gain_200mV_2us-outliers-included.png'
makeplot(enc1,nbins,xtitle,ytitle,unit,saveTo)
#'''

#plotting
#'''
nbins=10
xtitle='INL gain (200mV) @3$\mu$s, Total channels: %1.0f'%(total_channels)
ytitle='Counts'
unit=''
saveTo='./test-plots/inl_gain_200mV_3us-outliers-included.png'
makeplot(enc1,nbins,xtitle,ytitle,unit,saveTo)
#'''


