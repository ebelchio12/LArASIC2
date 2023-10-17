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


def makeplot(data,nbins,xtitle,ytitle,unit,saveTo):

  # get total entries before fitting
  snorm = len(data)
  #print(snorm)

  # best fit of data
  (mu, sigma) = norm.fit(data)

  # the histogram of the data
  n, bins, patches = plt.hist(data, nbins, density=False, facecolor='cyan')

  #for u in n:
   # print('ni=',u)

  # x data is bin centres
  bin_centres = (bins[:-1] + bins[1:]) / 2

  # add a 'best fit' line
  binwidth = bins[1]- bins[0]
  #print('binwidth=',binwidth)
  x = np.linspace(np.min(data), np.max(data), 100)
  y = 1.0 / np.sqrt(2 * np.pi * sigma**2) * np.exp(-0.5 * (x - mu) ** 2 / sigma**2)
  y = snorm*binwidth*y

  l = plt.plot(x, y, 'r--', linewidth=1.5)

  # plot
  print('mu=',mu)
  sign = mu - 3 * sigma
  sigp = mu + 3 * sigma
  plt.xlabel(xtitle)
  plt.ylabel(ytitle)
  plt.ylim(1, np.max(n)+3*sqrt( np.max(n) ) )
  #plt.yscale("log")
  plt.title(f'Mean={mu:.2f}{unit:s}, -3$\sigma$={sign:.2f}{unit:s}, 3$\sigma$={sigp:.2f}{unit:s}')

  # Plot the error bars, centred on (bin_centre, bin_count), with length y_error
  y_error = [sqrt(i) for i in n]
  plt.errorbar(bin_centres, n,yerr=y_error, fmt='ko', label='data', capsize=3)

  plt.legend([f'RMS: {sigma:.3f}{unit:s}'])
  plt.savefig(saveTo, dpi=100) #do this before plt.show(), otherwise blank plot
  plt.show()