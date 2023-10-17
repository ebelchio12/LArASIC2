# importing module
import csv
from glob import glob
import numpy as np
import matplotlib.pyplot as plt
import statistics
from Makeplots import makeplot
from filesToSkip import filesToSkip
#from outliers200mvSEOFFSEDCOFF import skipMe200mvSEOFFSEDCOFF
from outliers900mvSEOFFSEDCOFF import skipMe900mvSEOFFSEDCOFF

def getPowerMeasurement(file):

  with open(file) as csv_file:

    csv_reader = csv.reader(csv_file)
    rows = [r for r in csv_reader]

  row5=list(rows[5])
  row12=list(rows[12])
  row19=list(rows[19])
  row26=list(rows[26])
  row33=list(rows[33])
  row40=list(rows[40])

  row5.pop()
  row12.pop()
  row19.pop()
  row26.pop()
  row33.pop()
  row40.pop()

  se_off_sedc_off_900mv=next(reversed(row5))
  se_on_sedc_off_900mv=next(reversed(row12))
  se_off_sedc_on_900mv=next(reversed(row19))

  se_off_sedc_off_200mv=next(reversed(row26))
  se_on_sedc_off_200mv=next(reversed(row33))
  se_off_sedc_on_200mv=next(reversed(row40))

  result=[]

  result.append(float(se_off_sedc_off_900mv))
  result.append(float(se_on_sedc_off_900mv))
  result.append(float(se_off_sedc_on_900mv))

  result.append(float(se_off_sedc_off_200mv))
  result.append(float(se_on_sedc_off_200mv))
  result.append(float(se_off_sedc_on_200mv))

  return result


#get power measurement files
files = glob('./**/Power_FEChip*csv', recursive=True)

#power measurements from all chips (files)
power_se_off_sedc_off_200mv=[]
power_se_on_sedc_off_200mv=[]
power_se_off_sedc_on_200mv=[]

power_se_off_sedc_off_900mv=[]
power_se_on_sedc_off_900mv=[]
power_se_off_sedc_on_900mv=[]

# append each power measurement to corresponding list
total_chips = 0
for i in files:
  #print(i)

  # skip files with weird power measurement
  #if i in filesToSkip:
   # continue

  # skip files with weird power measurement
  #if i in skipMe200mvSEOFFSEDCOFF:
    #continue

  if i in skipMe900mvSEOFFSEDCOFF:
    continue

  result = getPowerMeasurement(i)
  '''
  if result[0]<3  or result[0]>7 or result[3]<3 or result[3]>7:
   print('off,off out of range:',i)

  if result[1] < 8 or result[1] > 12 or result[4] < 8 or result[4] > 12:
    print('on,off out of range:', i)
  '''
  if result[3]<5.7: # outliers 200mV off,off
   print('off,off 200mv <5.7:',i)

  if result[0]<5.7: # outliers 900mV off,off
   print('off,off 900mv <5.7:',i)

  if result[0]>7: # outliers 900mV off,off
   print('off,off 900mv >7:',i)

  power_se_off_sedc_off_900mv.append(result[0])
  power_se_on_sedc_off_900mv.append(result[1])
  power_se_off_sedc_on_900mv.append(result[2])

  power_se_off_sedc_off_200mv.append(result[3])
  power_se_on_sedc_off_200mv.append(result[4])
  power_se_off_sedc_on_200mv.append(result[5])

  total_chips = total_chips + 1


#mean
power_se_off_sedc_off_200mv_mean=statistics.mean(power_se_off_sedc_off_200mv)
power_se_on_sedc_off_200mv_mean=statistics.mean(power_se_on_sedc_off_200mv)
power_se_off_sedc_on_200mv_mean=statistics.mean(power_se_off_sedc_on_200mv)
power_se_off_sedc_off_900mv_mean=statistics.mean(power_se_off_sedc_off_900mv)
power_se_on_sedc_off_900mv_mean=statistics.mean(power_se_on_sedc_off_900mv)
power_se_off_sedc_on_900mv_mean=statistics.mean(power_se_off_sedc_on_900mv)

#sd
power_se_off_sedc_off_200mv_stdev=statistics.stdev(power_se_off_sedc_off_200mv)
power_se_on_sedc_off_200mv_stdev=statistics.stdev(power_se_on_sedc_off_200mv)
power_se_off_sedc_on_200mv_stdev=statistics.stdev(power_se_off_sedc_on_200mv)
power_se_off_sedc_off_900mv_stdev=statistics.stdev(power_se_off_sedc_off_900mv)
power_se_on_sedc_off_900mv_stdev=statistics.stdev(power_se_on_sedc_off_900mv)
power_se_off_sedc_on_900mv_stdev=statistics.stdev(power_se_off_sedc_on_900mv)

#3 sigma
power_se_off_sedc_off_200mv_sign = power_se_off_sedc_off_200mv_mean - 3*power_se_off_sedc_off_200mv_stdev
power_se_off_sedc_off_200mv_sigp = power_se_off_sedc_off_200mv_mean + 3*power_se_off_sedc_off_200mv_stdev
power_se_on_sedc_off_200mv_sign = power_se_on_sedc_off_200mv_mean - 3*power_se_on_sedc_off_200mv_stdev
power_se_on_sedc_off_200mv_sigp = power_se_on_sedc_off_200mv_mean + 3*power_se_on_sedc_off_200mv_stdev
power_se_off_sedc_on_200mv_sign = power_se_off_sedc_on_200mv_mean - 3*power_se_off_sedc_on_200mv_stdev
power_se_off_sedc_on_200mv_sigp = power_se_off_sedc_on_200mv_mean + 3*power_se_off_sedc_on_200mv_stdev

power_se_off_sedc_off_900mv_sign = power_se_off_sedc_off_900mv_mean - 3*power_se_off_sedc_off_900mv_stdev
power_se_off_sedc_off_900mv_sigp = power_se_off_sedc_off_900mv_mean + 3*power_se_off_sedc_off_900mv_stdev
power_se_on_sedc_off_900mv_sign = power_se_on_sedc_off_900mv_mean - 3*power_se_on_sedc_off_900mv_stdev
power_se_on_sedc_off_900mv_sigp = power_se_on_sedc_off_900mv_mean + 3*power_se_on_sedc_off_900mv_stdev
power_se_off_sedc_on_900mv_sign = power_se_off_sedc_on_900mv_mean - 3*power_se_off_sedc_on_900mv_stdev
power_se_off_sedc_on_900mv_sigp = power_se_off_sedc_on_900mv_mean + 3*power_se_off_sedc_on_900mv_stdev


#plotting
'''
nbins=10
xtitle='Power @200mV (mW/Ch) [SE=OFF|SEDC=OFF], Total chips: %1.0f'%(total_chips)
ytitle='Counts'
unit='mW/Ch'
#saveTo='./test-plots/power_measurement_200mV_SE-OFF_SEDC-OFF-logscale-outliers-included.png'
saveTo='./deleteme/deleteme1.png'
makeplot(power_se_off_sedc_off_200mv,nbins,xtitle,ytitle,unit,saveTo)
'''

'''
nbins=10
xtitle='Power @200mV (mW/Ch) [SE=ON|SEDC=OFF]'
ytitle='Counts'
unit='mW/Ch'
saveTo='./test-plots/power_measurement_200mV_SE-ON_SEDC-OFF-logscale-outliers-included.png'
makeplot(power_se_on_sedc_off_200mv,nbins,xtitle,ytitle,unit,saveTo)
'''

'''
nbins=10
xtitle='Power @200mV (mW/Ch) [SE=OFF|SEDC=ON]'
ytitle='Counts'
unit='mW/Ch'
saveTo='./test-plots/power_measurement_200mV_SE-OFF_SEDC-ON-logscale-outliers-included.png'
makeplot(power_se_off_sedc_on_200mv,nbins,xtitle,ytitle,unit,saveTo)
'''

#plotting
#'''
nbins=10
xtitle='Power @900mV (mW/Ch) [SE=OFF|SEDC=OFF], Total chips: %1.0f'%(total_chips)
ytitle='Counts'
unit='mW/Ch'
#saveTo='./test-plots/power_measurement_900mV_SE-OFF_SEDC-OFF-logscale-outliers-included.png'
saveTo='./deleteme/deleteme4.png'
makeplot(power_se_off_sedc_off_900mv,nbins,xtitle,ytitle,unit,saveTo)
#'''

'''
nbins=10
xtitle='Power @900mV (mW/Ch) [SE=ON|SEDC=OFF]'
ytitle='Counts'
unit='mW/Ch'
saveTo='./test-plots/power_measurement_900mV_SE-ON_SEDC-OFF-logscale-outliers-included.png'
makeplot(power_se_on_sedc_off_900mv,nbins,xtitle,ytitle,unit,saveTo)
#'''

'''
nbins=10
xtitle='Power @900mV (mW/Ch) [SE=OFF|SEDC=ON]'
ytitle='Counts'
unit='mW/Ch'
saveTo='./test-plots/power_measurement_900mV_SE-OFF_SEDC-ON-logscale-outliers-included.png'
makeplot(power_se_off_sedc_on_900mv,nbins,xtitle,ytitle,unit,saveTo)
'''



