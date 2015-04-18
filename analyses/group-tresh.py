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
nRevs = 10 # number of reversals for calculating the threshold

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
    # CSV file for getting the current subject and session:
    thisCsv = pd.read_csv(dataDir + os.sep + thisSubjDir + '.csv')
    thisSubj = thisCsv.participant[0]
    thisSession = thisCsv.session[0]
    # The list of files for the current session:
    files = glob.glob(dataDir + os.sep + thisSubjDir + os.sep + '*.psydat')
    # Looping through the files:
    subjtdf = pd.DataFrame()
    #sumtdf = pd.DataFrame()
    for thisFileName in files:
        thisDat = fromFile(thisFileName)
        assert isinstance(thisDat, data.StairHandler) # probably a routine check
        nTrials = len(thisDat.intensities)
        # A local data set to be later appended to the whole data set:
        df = pd.DataFrame({
            'subj': np.repeat(thisSubj, nTrials),
            'session': np.repeat(thisSession, nTrials),
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
            'session': thisSession,
            'maskSpeed': thisDat.extraInfo['maskSpeed'],
            #'targLoc': thisDat.extraInfo['targLoc'],
            'startVal': thisDat.extraInfo['startVal'],
            'label': thisDat.extraInfo['label'],
            'threshold': [np.average(thisDat.reversalIntensities[-nRevs:])] })
        subjtdf = subjtdf.append(tdf) # this is specific to this subject
        wtdf = wtdf.append(tdf) # this is accumulating across subjects
        print thisFileName
        print 'reversals ' + str(thisDat.reversalIntensities[-nRevs:])
    #print subjtdf
    sumtdf = subjtdf.groupby('maskSpeed')
    sumtdf = sumtdf['threshold'].agg([np.mean])
    sumtdf = sumtdf.reset_index()
    sumtdf.rename(columns={'mean':'threshold'}, inplace=True)
    sumtdf['subj'] = thisSubj
    sumtdf['session'] = thisSession
    #print sumtdf
    sumtdf['normThresh'] = sumtdf['threshold'] / np.average(sumtdf['threshold'])
    wsumtdf = wsumtdf.append(sumtdf)
    # getting the subject directory name to use as the name for plots:
    subjDirName = os.path.basename(os.path.dirname(thisFileName))

#print 'whole data frame'
#print wdf
print 'whole threshold data frame'
print wtdf
print 'threshold summaries'
print wsumtdf

#g=sns.factorplot('maskSpeed', 'threshold', 'targLoc', col='subj', data=wtf, 
g=sns.factorplot('maskSpeed', 'threshold', col='subj', data=wsumtdf, 
    col_wrap=3, kind='bar',)
g.set(ylim=(0,.35))
pylab.savefig(dataDir + os.sep + 'subjThresholds.pdf')
#pylab.show()

g=sns.factorplot('maskSpeed', 'threshold', data=wsumtdf, kind='box')
g.set(ylim=(0,.35))
pylab.savefig(dataDir + os.sep + 'groupThresholds.pdf')
#pylab.show()

g=sns.factorplot('maskSpeed', 'normThresh', col='subj', data=wsumtdf, 
    col_wrap=3, kind='bar')
g.set(ylim=(0,3.5))
pylab.savefig(dataDir + os.sep + 'subjNormThresh.pdf')
#pylab.show()

g=sns.factorplot('maskSpeed', 'normThresh', data=wsumtdf, kind='box')
g.set(ylim=(0,3.5))
pylab.savefig(dataDir + os.sep + 'groupNormThresh.pdf')
#pylab.show()
