from __future__ import division
from psychopy import data, gui, core
from psychopy.tools.filetools import fromFile
import pylab, scipy
import os, glob # file and directory handling
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

thisCsv = pd.read_csv('3ddata.csv')

#g=sns.factorplot('maskRotSpeed', 'meanRT', data=thisCsv, kind='box')
#g.set(ylim=(0,4))
#plt.xlabel('Mask Speed')
#plt.ylabel('Mean Reaction Time')
#plt.yticks(np.arange(0,5,1))
#pylab.savefig('3dplot-box.pdf')
#pylab.show()

sns.set_style("white")
sns.set_context("poster")
sns.despine()

plt.figure(figsize=(5,5))
g=sns.regplot('maskRotSpeed', 'meanRT', data=thisCsv)
g.set(ylim=(0,4))
plt.xlabel('Mask Speed')
plt.ylabel('Mean Reaction Time')
plt.yticks(np.arange(0,5,1))
plt.xticks(np.array([0,15,30,60,90]))
pylab.tight_layout()
pylab.subplots_adjust(top=.95)
pylab.savefig('3dplot-dot.pdf')