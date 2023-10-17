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

def getColumn(file,column_key):
  bl = read_csv(file)
  # converting column data to list
  column = bl[column_key].tolist()

  #print(len(column))
  result = []

  # skip files with different formatting
  if len(column) != 18:
    # print('len column=',len(column))
    print('file with double measurements(?), skipping file ',file)
    return result

  for i in column:
    #print(i)
    result.append(float(i))
  #print('')

  return result

#get ENC gain files
files = glob('./**/Noise_Gain_raw*.csv', recursive=True)

#ENC gain from all chips (files)
enc05=[]
enc1=[]
enc2=[]
enc3=[]

# append each ENC to corresponding list
for i in files:
  #print(i)
  e05 = getColumn(i,'Gain @0.5us')
  e1 = getColumn(i,'Gain @1us')
  e2 = getColumn(i,'Gain @2us')
  e3 = getColumn(i,'Gain @3us')

  # remove last elements from column
  e05 = e05[:-2]
  e1 = e1[:-2]
  e2 = e2[:-2]
  e3 = e3[:-2]

  #'''
  for j in e05:
    if float(j)>12:
      print('05us > 12',i)

  for j in e1:
    if float(j)>11.75:
      print('1us > 11.75',i)

  for j in e2:
    if float(j)>10.16:
      print('2us > 10.16',i)

  for j in e3:
    if float(j)>10.4:
      print('3us > 10.4',i)
  #'''

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
xtitle='Noise gain @0.5$\mu$s (e-/LSB), Total channels: %1.0f'%(total_channels)
ytitle='Counts'
unit=''
#saveTo='./test-plots/noise_gain_0.5us-outliers-included.png'
saveTo='./deleteme/deleteme1.png'
makeplot(enc05,nbins,xtitle,ytitle,unit,saveTo)
#'''

#plotting
#'''
nbins=10
xtitle='Noise gain @1$\mu$s (e-/LSB), Total channels: %1.0f'%(total_channels)
ytitle='Counts'
unit=''
#saveTo='./test-plots/noise_gain_1us-outliers-included.png'
saveTo='./deleteme/deleteme2.png'
makeplot(enc1,nbins,xtitle,ytitle,unit,saveTo)
#'''

#plotting
#'''
nbins=10
xtitle='Noise gain @2$\mu$s (e-/LSB), Total channels: %1.0f'%(total_channels)
ytitle='Counts'
unit=''
#saveTo='./test-plots/noise_gain_2us-outliers-included.png'
saveTo='./deleteme/deleteme3.png'
makeplot(enc2,nbins,xtitle,ytitle,unit,saveTo)
#'''

#plotting
#'''
nbins=10
xtitle='Noise gain @3$\mu$s (e-/LSB), Total channels: %1.0f'%(total_channels)
ytitle='Counts'
unit=''
saveTo='./test-plots/noise_gain_3us-outliers-included.png'
#saveTo='./deleteme/deleteme4.png'
makeplot(enc3,nbins,xtitle,ytitle,unit,saveTo)
#'''
