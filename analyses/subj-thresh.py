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
allIntensities, allResponses, allInfos = [],[],[]
for thisFileName in files:
    thisDat = fromFile(thisFileName)
    assert isinstance(thisDat, data.StairHandler)
    allIntensities.append(thisDat.intensities)
    allResponses.append(thisDat.data)
    allInfos.append(thisDat.extraInfo)
#    print '======'
#    print thisFileName
#    print thisDat.intensities
#    print thisDat.extraInfo
dataFolder = os.path.split(thisFileName)[0] #just the path, excluding file name

# Load the conditions data set.
cond = pd.read_csv(dataFolder + os.sep + 'cond-expt01.csv')

# Find the variables that differ between conditions.
#for curColIx in range(len(cond.columns)+1):
#    print '===column ' + str(curColIx) + '==='
#    print pd.unique(cond.ix[:,curColIx])
#    print len(pd.unique(cond.ix[:,curColIx]))

#print len(condVars)
#print np.zeros([1,len(condVars)])
#condNFactors = pd.DataFrame(np.zeros([1,len(condVars)]), columns=list(condVars))
#for curCol in condVars:
    #print pd.unique(cond.ix[:,curCol])
    #condNFactors.ix[:,curCol] = len(pd.unique(cond.ix[:,curCol]))

# My own plotting function:
#f, axarr = plt.subplots(2,5)
#print allIntensities
#print list(enumerate(allIntensities))
#for fileN, thisStair in enumerate(allIntensities):
#    print fileN
#    axarr[0,0].plot(thisStair, label=files[fileN])
#for fileN, thisStair in enumerate(allIntensities):
    #axarr.plot(thisStair, label=files[fileN])
# A double-nested loop to go through levels of factors:
fileN = 0
colors = 'brgkcmbrgkcm'
f, axarr = plt.subplots(2,5)
for ixMaskSpeed, curMaskSpeed in enumerate(pd.unique(cond.maskSpeed)):
    for ixTargLoc, curTargLoc in enumerate(pd.unique(cond.targLoc)):
        condLow = cond.label[(cond['targLoc']==curTargLoc) & \
            (cond['maskSpeed']==curMaskSpeed) & \
            (cond['startVal']==0.1)]
#        fileLow = allInfos[(allInfos['targLoc']==curTargLoc) & \
#            (allInfos['maskSpeed']==curMaskSpeed) & \
#            (allInfos['startVal']==0.1)]
        print condLow
        print dir(allInfos)
        print allInfos.get('label',None)
#        print allInfos
#        print allInfos['label']==condLow
#        fileLow = allInfos[allInfos['label']==condLow].index
#        print fileLow
        labelLow = cond.label[fileLow]
        print labelLow
        print allIntensities[fileLow]
        axarr[ixTargLoc, ixMaskSpeed].plot(allIntensities[fileLow])
        axarr[ixTargLoc, ixMaskSpeed].set
        fileHigh = cond[(cond['targLoc']==curTargLoc) & \
            (cond['maskSpeed']==curMaskSpeed) & \
            (cond['startVal']==0.8)].index
        labelHigh = cond.label[fileHigh]
        print labelHigh
        print allIntensities[fileHigh]
        axarr[ixTargLoc, ixMaskSpeed].plot(allIntensities[fileHigh])

## plot each staircase in left hand panel:
#pylab.subplot(121)
#colors = 'brgkcmbrgkcm'
#lines, names = [],[]
#for fileN, thisStair in enumerate(allIntensities):
    #lines.extend(pylab.plot(thisStair)) # uncomment these lines to get a legend for files
    #names = files[fileN] # uncomment these lines to get a legend for files
    #pylab.plot(thisStair, label=files[fileN])
#pylab.legend() # uncomment these lines to get a legend for files

# get combined data:
#combinedInten, combinedResp, combinedN = \
#             data.functionFromStaircase(allIntensities, allResponses, bins='unique')
#combinedN = pylab.array(combinedN) # convert to array so we can do maths with them

# fit curve:
#fit = data.FitWeibull(combinedInten, combinedResp, expectedMin=expectedMin,
#    sems = 1.0/combinedN)
#smoothInt = pylab.arange(min(combinedInten), max(combinedInten), 0.001)
#smoothResp = fit.eval(smoothInt)
#thresh = fit.inverse(threshVal)
#print thresh

# plot curve:
#pylab.subplot(122)
#pylab.plot(smoothInt, smoothResp, 'k-')
#pylab.plot([thresh, thresh],[0,threshVal],'k--') #vertical dashed line
#pylab.plot([0, thresh],[threshVal,threshVal],'k--') #horizontal dashed line
#pylab.title('threshold (%.2f) = %0.3f' %(threshVal, thresh))

# plot points:
#pointSizes = pylab.array(combinedN)*5 #5 pixels per trial at each point
#points = pylab.scatter(combinedInten, combinedResp, s=pointSizes, 
#    edgecolors=(0,0,0), facecolor=(1,1,1), linewidths=1,
#    zorder=10, #make sure the points plot on top of the line
#    )

#pylab.ylim([0,1.1])
#pylab.xlim([0,1])

# save a vector-graphics format for future:
#outputFile = os.path.join(dataFolder, 'last.pdf')
#pylab.savefig(outputFile)
#print 'saved figure to:', outputFile

pylab.show()
