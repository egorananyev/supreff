#!/usr/bin/env python2

from __future__ import division
from psychopy import data, gui, core
from psychopy.tools.filetools import fromFile
import pylab, scipy
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Selecting the files for processing.
dataDir = '..' + os.sep + '..' + os.sep + 'data' # common data directory
files = gui.fileOpenDlg(dataDir)
if not files:
    core.quit()

nRevs = 10

# My version of data input.
print 'BUILDING DATA FRAME'
wdf = pd.DataFrame()
subjtdf = pd.DataFrame()
for thisFileName in files:
    thisDat = fromFile(thisFileName)
    assert isinstance(thisDat, data.StairHandler) # not sure what this does but oh well
    nTrials = len(thisDat.intensities)
    df = pd.DataFrame({
        'maskSpeed': np.repeat(thisDat.extraInfo['maskSpeed'], nTrials),
        'startVal': np.repeat(thisDat.extraInfo['startVal'], nTrials),
        'trial': range(nTrials),
        'label': np.repeat(thisDat.extraInfo['label'], nTrials),
        'contrast': thisDat.intensities})
#    print df
    wdf = wdf.append(df)
    tdf = pd.DataFrame({
        'maskSpeed': thisDat.extraInfo['maskSpeed'],
        'startVal': thisDat.extraInfo['startVal'],
        'label': thisDat.extraInfo['label'],
        'threshold': [np.average(thisDat.reversalIntensities[-nRevs:])] })
    subjtdf = subjtdf.append(tdf) # this is specific to this subject
# getting the subject directory name to use as the name for plots:
subjDirName = os.path.basename(os.path.dirname(thisFileName))
#print wdf
wdf.to_csv(os.path.join(os.path.dirname(thisFileName), 'res-table.csv'))
print 'BUILDING DATA FRAME COMPLETED'
subjtdf['normThresh'] = subjtdf['threshold'] / np.average(subjtdf['threshold'])
print subjtdf

# Plotting using seaborn.
#sns.set(style="ticks")
sns.set(font_scale=1.8)
#grid = sns.FacetGrid(wdf, row='targLoc', col='maskSpeed', hue='startVal', size=5.5)
grid = sns.FacetGrid(wdf, col='maskSpeed', hue='startVal', size=5.5)
grid.map(plt.plot, 'trial', 'contrast', marker='o')
grid.set(ylim=(0,1))

# Output the figures.

# Staircases.
figFile = dataDir + os.sep + subjDirName + '_stairs.pdf'
pylab.savefig(figFile)
print 'saved figure to: ' + figFile
#pylab.show()

# Raw thresholds.
figFile = dataDir + os.sep + subjDirName + '_subjThresh.pdf'
g=sns.factorplot('maskSpeed', 'threshold', data=subjtdf, kind='box')
g.set(ylim=(0,.5))
pylab.savefig(figFile)
print 'saved figure to: ' + figFile
#pylab.show()

# Normalized thresholds.
figFile = dataDir + os.sep + subjDirName + '_normThresh.pdf'
g=sns.factorplot('maskSpeed', 'normThresh', data=subjtdf, kind='box')
g.set(ylim=(0,5))
pylab.savefig(figFile)
print 'saved figure to: ' + figFile
#pylab.show()
