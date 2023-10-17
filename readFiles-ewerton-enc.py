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

#define cuts to make plots
min_enc_05 = 0
max_enc_05 = 10000
min_enc_1 = 0
max_enc_1 = 10000
min_enc_2 = 0
max_enc_2 = 10000
min_enc_3 = 0
max_enc_3 = 10000


def getColumn(file,column_key,mincut,maxcut):
  bl = read_csv(file)
  # converting column data to list
  column = bl[column_key].tolist()

  result = []
  #print(len(column))
  # skip files with different formatting
  if len(column) != 18:
    print('len column=',len(column))
    print('file with double measurements(?), skipping file ',file)
    return result

  # remove nan from list
  column = [item for item in column if not(isnull(item)) == True]
  #print('len=',len(column))

  for i in column:
    # skip files which do not pass minimum criteria
    #if ( not (i > mincut and i < maxcut) ):
      #print(i)
      #print('file does not pass minimum criteria, skipping file ', file)
      #result.clear()
      #return result

    result.append(float(i))
  #print('')

  return result

#get ENC files
files = glob('./**/Noise_ENC_raw*.csv', recursive=True)

#ENC from all chips (files)
enc05=[]
enc1=[]
enc2=[]
enc3=[]

# append each ENC to corresponding list
for i in files:
  #print(i)
  e05 = getColumn(i,'ENC(e-) @0.5us',min_enc_05,max_enc_05)
  e1 = getColumn(i,'ENC(e-) @1us',min_enc_1,max_enc_1)
  e2 = getColumn(i,'ENC(e-) @2us',min_enc_2,max_enc_2)
  e3 = getColumn(i,'ENC(e-) @3us',min_enc_3,max_enc_3)

  # remove last elements from column
  e05 = e05[:-2]
  e1 = e1[:-2]
  e2 = e2[:-2]
  e3 = e3[:-2]
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
xtitle='ENC @0.5$\mu$s (e-), Total channels: %1.0f'%(total_channels)
ytitle='Counts'
unit='e-'
saveTo='./test-plots/enc_0.5us-outliers-included.png'
makeplot(enc05,nbins,xtitle,ytitle,unit,saveTo)
#'''

#plotting
'''
nbins=10
xtitle='ENC @1$\mu$s (e-), Total channels: %1.0f'%(total_channels)
ytitle='Counts'
unit='e-'
saveTo='./test-plots/enc_1us-outliers-included.png'
makeplot(enc1,nbins,xtitle,ytitle,unit,saveTo)
#'''

#plotting
'''
nbins=10
xtitle='ENC @2$\mu$s (e-), Total channels: %1.0f'%(total_channels)
ytitle='Counts'
unit='e-'
saveTo='./test-plots/enc_2us-outliers-included.png'
makeplot(enc2,nbins,xtitle,ytitle,unit,saveTo)
#'''

#plotting
'''
nbins=10
xtitle='ENC @3$\mu$s (e-), Total channels: %1.0f'%(total_channels)
ytitle='Counts'
unit='e-'
saveTo='./test-plots/enc_3us-outliers-included.png'
makeplot(enc3,nbins,xtitle,ytitle,unit,saveTo)
'''

