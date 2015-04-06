#!/usr/bin/env python2

# This analysis script takes one or more staircase datafiles as input from a GUI
# It then plots the staircases on top of each other on the left 
# and a combined psychometric function from the same data
# on the right.
#
# The combined plot uses every unique X value form the staircase, and alters the
# size of the points according to how many trials were run at that level.

from __future__ import division
from psychopy import data, gui, core
from psychopy.tools.filetools import fromFile
import pylab, scipy
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# conditional variables:
condVars = ['maskSpeed','targLoc']

# set to 0.5 for Yes/No (or PSE). Set to 0.8 for a 2AFC threshold
threshVal = 0.8 # 0.5
# set to zero for Yes/No (or PSE). Set to 0.5 for 2AFC
expectedMin = 0.5 # 0.0

files = gui.fileOpenDlg('..' + os.sep + 'data')
if not files:
    core.quit()

# get the data from all the files:
allIntensities, allResponses, allInfos, allCondLabels = [],[],[],[]
for thisFileName in files:
    thisDat = fromFile(thisFileName)
    assert isinstance(thisDat, data.StairHandler)
    allIntensities.append(thisDat.intensities)
    allResponses.append(thisDat.data)
    allInfos.append(thisDat.extraInfo)
    allCondLabels.append(thisDat.extraInfo['label'])
#    print '======'
#    print thisFileName
#    print thisDat.intensities
    print thisDat.extraInfo['label']
#    print thisDat.extraInfo
    print np.average(thisDat.reversalIntensities[-15:])
dataFolder = os.path.split(thisFileName)[0] #just the path, excluding file name

# Load the conditions data set.
cond = pd.read_csv(dataFolder + os.sep + 'cond-expt01.csv')

# My own plotting function.
# A double-nested loop to go through levels of factors:
fileN = 0
colors = 'obrgkcmobrgkcm'
f, axarr = plt.subplots(2,5)
for ixMaskSpeed, curMaskSpeed in enumerate(pd.unique(cond.maskSpeed)):
    for ixTargLoc, curTargLoc in enumerate(pd.unique(cond.targLoc)):
        print '======'
        print allCondLabels
        # Finding the cond file row matching the current loop iteration:
        condLow = cond.label[(cond['targLoc']==curTargLoc) & \
            (cond['maskSpeed']==curMaskSpeed) & \
            (cond['startVal']==0.1)]
        # Finding the file with the data for the above condition:
        fileLow = allCondLabels.index(condLow.values)
        print condLow.values
        print fileLow
        print allIntensities[fileLow]
        axarr[ixTargLoc, ixMaskSpeed].plot(allIntensities[fileLow])
        axarr[ixTargLoc, ixMaskSpeed]
        condHigh = cond.label[(cond['targLoc']==curTargLoc) & \
            (cond['maskSpeed']==curMaskSpeed) & \
            (cond['startVal']==0.8)]
        # Finding the file with the data for the above condition:
        fileHigh = allCondLabels.index(condHigh.values)
        print condHigh.values
        print fileHigh
        print allIntensities[fileHigh]
        axarr[ixTargLoc, ixMaskSpeed].plot(allIntensities[fileHigh])
        axarr[ixTargLoc, ixMaskSpeed].set_title(str(curMaskSpeed)+' '+curTargLoc)

pylab.show()
