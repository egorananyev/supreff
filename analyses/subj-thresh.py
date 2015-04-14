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
dataDir = '..' + os.sep + 'data' # common data directory
files = gui.fileOpenDlg(dataDir)
if not files:
    core.quit()

# My version of data input.
print 'BUILDING DATA FRAME'
wdf=pd.DataFrame(columns=['maskSpeed','targLoc','startVal','trial','label','contrast'])
for thisFileName in files:
    thisDat = fromFile(thisFileName)
    assert isinstance(thisDat, data.StairHandler) # not sure what this does but oh well
    nTrials = len(thisDat.intensities)
    df = pd.DataFrame({
        'maskSpeed': np.repeat(thisDat.extraInfo['maskSpeed'], nTrials),
        'targLoc': np.repeat(thisDat.extraInfo['targLoc'], nTrials),
        'startVal': np.repeat(thisDat.extraInfo['startVal'], nTrials),
        'trial': range(nTrials),
        'label': np.repeat(thisDat.extraInfo['label'], nTrials),
        'contrast': thisDat.intensities})
#    print df
    wdf = wdf.append(df)
# getting the subject directory name to use as the name for plots:
subjDirName = os.path.basename(os.path.dirname(thisFileName))
#print wdf
wdf.to_csv(os.path.join(os.path.dirname(thisFileName), 'res-table.csv'))
print 'BUILDING DATA FRAME COMPLETED'

# Plotting using seaborn.
#sns.set(style="ticks")
sns.set(font_scale=1.8)
grid = sns.FacetGrid(wdf, row='targLoc', col='maskSpeed', hue='startVal', size=5.5)
grid.map(plt.plot, 'trial', 'contrast', marker='o')
grid.set(ylim=(0,1))

# Output the figure.
figFile = dataDir + os.sep + subjDirName + '.pdf'
pylab.savefig(figFile)
print 'saved figure to: ' + figFile
pylab.show()
