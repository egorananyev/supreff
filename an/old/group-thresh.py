#!/usr/bin/env python2

from __future__ import division
from psychopy import data, gui, core
from psychopy.tools.filetools import fromFile
import pylab, scipy
import os, glob # file and directory handling
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# CONSTANTS.
nRevs = 2 # number of reversals for calculating the threshold

# Selecting the files for processing.
dataDir = '..' + os.sep + '..' + os.sep + 'data' # common data directory
allSubjDirs = os.walk(dataDir).next()[1] # get the directory names
print allSubjDirs

## Nested loop to go through the directories and files.
wdf = pd.DataFrame() # single data frame for the entire data set
wtdf = pd.DataFrame() # whole threshold frame
wsumtdf = pd.DataFrame() # summary threshold information across subjects
# Looping through the directories:
for thisSubjDir in allSubjDirs:
    print 'thisSubjDir = ' + thisSubjDir
    # CSV file for getting the current subject and experiment:
    thisCsv = pd.read_csv(dataDir + os.sep + thisSubjDir + os.sep + thisSubjDir + '.csv')
    thisSubj = thisCsv.participant[0]
    thisParadigm = thisCsv.paradigm[0]
    # The list of files for the current experiment:
    files = glob.glob(dataDir + os.sep + thisSubjDir + os.sep + '*stair*.psydat')
    # Looping through the files:
    subjtdf = pd.DataFrame()
    #sumtdf = pd.DataFrame()
    for thisFileName in files:
        print 'thisFileName = ' + thisFileName
        thisDat = fromFile(thisFileName)
        #print dir(thisDat)
        assert isinstance(thisDat, data.StairHandler) # probably a routine check
        nTrials = len(thisDat.intensities)
        # A local data set to be later appended to the whole data set:
        df = pd.DataFrame({
            'subj': np.repeat(thisSubj, nTrials),
            'experiment': np.repeat(thisParadigm, nTrials),
            'maskSpeed': np.repeat(thisDat.extraInfo['maskSpeed'], nTrials),
            #'targLoc': np.repeat(thisDat.extraInfo['targLoc'], nTrials),
            'startVal': np.repeat(thisDat.extraInfo['startVal'], nTrials),
            'trial': range(nTrials),
            'label': np.repeat(thisDat.extraInfo['label'], nTrials),
            'contrast': thisDat.intensities})
        wdf = wdf.append(df)
        # Threshold data set:
        tdf = pd.DataFrame({
            'subj': thisSubj,
            'experiment': thisParadigm,
            'maskSpeed': thisDat.extraInfo['maskSpeed'],
            #'targLoc': thisDat.extraInfo['targLoc'],
            'startVal': thisDat.extraInfo['startVal'],
            'label': thisDat.extraInfo['label'],
            'threshold': [np.average(thisDat.reversalIntensities[-nRevs:])] })
        subjtdf = subjtdf.append(tdf) # this is specific to this subject
        wtdf = wtdf.append(tdf) # this is accumulating across subjects
        print thisFileName
        print 'reversals ' + str(thisDat.reversalIntensities[-nRevs:])
    print subjtdf
    sumtdf = subjtdf.groupby('maskSpeed')
    sumtdf = sumtdf['threshold'].agg([np.mean])
    sumtdf = sumtdf.reset_index()
    sumtdf.rename(columns={'mean':'threshold'}, inplace=True)
    sumtdf['subj'] = thisSubj
    sumtdf['experiment'] = thisParadigm
    # this, for some reason, yields only 1s, so this is later recalculated:
    sumtdf['normThresh'] = sumtdf['threshold'] / np.average(sumtdf['threshold'])
    wsumtdf = wsumtdf.append(sumtdf)
    # getting the subject directory name to use as the name for plots:
    subjDirName = os.path.basename(os.path.dirname(thisFileName))

#print 'whole data frame'
#print wdf
print 'whole threshold data frame'
print wtdf
# recalculation of normalised thresholds based on the overall mean:
wsumtdf['normThresh'] = wsumtdf['threshold'] / np.average(wsumtdf['threshold'])
print 'threshold summaries'
print wsumtdf
pd.DataFrame.to_csv(wsumtdf, dataDir + os.sep + 'groupThresholds.csv', index = False)

sns.set_style("white")
sns.set_context("poster")
sns.despine()

#g=sns.factorplot('maskSpeed', 'threshold', 'targLoc', col='subj', data=wtf, 
#g=sns.factorplot('maskSpeed', 'threshold', col='subj', data=wsumtdf, 
#    col_wrap=3, kind='bar',)
#g.set(ylim=(0,.55))
#pylab.savefig(dataDir + os.sep + 'subjThresholds.pdf')
#pylab.show()
#
#g=sns.factorplot('maskSpeed', 'threshold', data=wsumtdf, kind='box')
#g.set(ylim=(0,.55))
#pylab.savefig(dataDir + os.sep + 'groupThresholds.pdf')
#pylab.show()
#
#g=sns.factorplot('maskSpeed', 'normThresh', col='subj', data=wsumtdf, 
#    col_wrap=3, kind='bar')
#g.set(ylim=(0,2))
#pylab.savefig(dataDir + os.sep + 'subjNormThresh.pdf')
#pylab.show()
#
#g=sns.factorplot('maskSpeed', 'normThresh', data=wsumtdf, kind='box')
#g.set(ylim=(0,2))
#plt.xlabel('Mask Speed')
#plt.ylabel('Normalized Contrast Threshold')
#pylab.savefig(dataDir + os.sep + 'groupNormThresh.pdf')
#pylab.show()

plt.figure(figsize=(5,5))
g=sns.regplot('maskSpeed', 'normThresh', data=wsumtdf)
g.set(ylim=(0,2))
plt.xlabel('Mask Speed',va='top')
plt.ylabel('Normalized Contrast Threshold')
#plt.xticks(np.array([15,30,45,75,120]))
plt.xticks(np.array([1,2,3,5,8]))
pylab.tight_layout()
pylab.subplots_adjust(top=.95)
pylab.savefig(dataDir + os.sep + 'groupNormThresh-dot.pdf')
#pylab.show()