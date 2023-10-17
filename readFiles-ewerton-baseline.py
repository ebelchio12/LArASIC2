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
from scipy import stats
from math import sqrt
from scipy.optimize import curve_fit
from scipy.optimize import Bounds
from Makeplots import makeplot


#define cuts to make plots
min_vbgr = 0
min_bl_200 = 0
max_bl_200 = 10000
min_bl_900 = 0
max_bl_900 = 10000


#def gauss(x,mean,sigma): #params[0]=mean, params[1]=sigma
#  return (1.0/np.sqrt(2*np.pi*sigma**2))*np.exp(-0.5*(x-mean)**2/sigma**2)


def getColumn(file,column_key,mincut,maxcut):
  bl = read_csv(file)
  # converting column data to list
  column = bl[column_key].tolist()

  result = []

  #print(len(column))

  # skip files with different formatting
  if len(column) != 20:
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


#get baseline files
files = glob('./**/Baseline_VBGR_Temp_FEChip_*.csv', recursive=True)

#baseline and vbgr from all chips (files)
bl_200mv=[]
bl_900mv=[]
vbgr=[]

# append each baseline and vbgr to corresponding list
for i in files:
  #print(i)
  bl_200 = getColumn(i,'BL @ 200mV',min_bl_200,max_bl_200)
  bl_900 = getColumn(i,'BL @ 900mV',min_bl_900,max_bl_900)

  # skip files with different formatting or which do not pass minimum criteria
  if len(bl_200) == 0 or len(bl_900) == 0:
    continue

  '''
    for j in bl_200:
      print(j)
    print("")

    for j in bl_900:
      print(j)
    print("")
  '''

  #get vbgr
  bl_200 = bl_200[:-1]
  vb = next(reversed(bl_200))
  #if(vb==1.1824): #check chip 001-00266
    #print(i)

  #skip file if does not pass minimum criteria
  if vb < min_vbgr:
    print('file does not pass minimum criteria, skipping file ', i)
    continue

  # remove last elements from column
  bl_200 = bl_200[:-3]
  bl_900 = bl_900[:-2]
  '''
  for j in bl_200:
    print(j)
  print("")

  for j in bl_900:
    print(j)
  print("")
  '''
  bl_200mv.extend(bl_200)
  bl_900mv.extend(bl_900)
  vbgr.append(vb)

total_chips = len(vbgr)
total_channels = len(bl_200mv)
#-----------------------------------------------
#plotting
#'''
nbins=9
xtitle='VBGR (V), Total chips: %1.0f'%(total_chips)
ytitle='Counts'
unit='V'
#saveTo='./test-plots/vbgr-outliers-included.png'
saveTo='./deleteme/deleteme1.png'
makeplot(vbgr,nbins,xtitle,ytitle,unit,saveTo)
#'''

'''
nbins=15
xtitle1='Baseline 200mV (mV), Total channels: %1.0f'%(total_channels)
ytitle1='Counts'
unit1='mV'
saveTo='./est-plots/baseline_200mV-outliers-included.png'
makeplot(bl_200mv,nbins,xtitle1,ytitle1,unit1,saveTo)
'''

'''
nbins=15
xtitle2='Baseline 900mV (mV), Total channels: %1.0f'%(total_channels)
ytitle2='Counts'
unit2='mV'
saveTo='./test-plots/baseline_900mV-outliers-included.png'
makeplot(bl_900mv,nbins,xtitle2,ytitle2,unit2,saveTo)
'''
