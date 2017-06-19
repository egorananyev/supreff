#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.00), Mon Mar 16 14:30:23 2015
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, gui #,logging
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
from datetime import datetime
import os  # handy system and path functions
import itertools
import shutil
import pyglet
allScrs = pyglet.window.get_platform().get_default_display().get_screens()
print allScrs

# Import the threshold information for the subject:

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expInfo = {u'session': u's1', u'domEye': u'r', u'participant': u'0', u'thresh': u'1',
           u'training': u'0', u'exptCond': 'vid'}
dlg = gui.DlgFromDict(dictionary=expInfo, title='dm') # dialogue box
expName = 'dm' + expInfo['exptCond']
exptCond = expInfo['exptCond']
if dlg.OK == False: core.quit()  # user pressed cancel
# expInfo['date'] = data.getDateStr()  # add a simple timestamp
timeNow = datetime.now()
expInfo['date'] = datetime.now().strftime('%Y-%m-%d_%H%M')
expInfo['expName'] = expName
subjThresh = float(expInfo['thresh'])
print subjThresh

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
dataDir = '..' + os.sep + 'data'
fileName = '%s_p-%s_dom-%s_%s_t%s_%s' %(expName, expInfo['participant'],
    expInfo['domEye'], expInfo['session'], expInfo['training'], expInfo['date'])
filePath = dataDir + os.sep + fileName
print filePath

# ====================================================================================
## Initial variables.
# Window boxes and black boxes (specified in degrees of visual angles [dva]):
windowSize = 5.03 # 4.47
windowOffsetX = 5.62 # 5.62 # 6.71
windowOffsetY = 5.5 # 2.83 # 4.97
windowThickness = 2
# targVertOffset = 1.5
blackBoxSize = windowSize + 0.5
blackBoxThickness = 10
# Mask variables:
nMaskElements = 300 # 248 # must be divisible by the number of directions allowed (below)
# Timing variables (in seconds) and trial number:
tRev = 3/5 # the duration of each direction reversal, in sec, kept constant for all targ & mask v's
nRev = int(tRev * 60)
# jitTime = .5 # the jittering for the onset; the max for preStimInterval 
# stimDuration = 3 # 3.6s in the Moors paper
# threshTime = 2 # the threshold time will appear at 2s
ISIduration = 0.0 # 0.5 before
# Contrast:
contrMin = 0
contrMax = 2
# Condition-related variables
#exptCond = 6
conditionsFilePath = 'cond-files'+os.sep+'cond-bcfs-'+exptCond+'.csv'
if expInfo['training']=='1':
    train = True
else:
    train = False
# Other variables:
# contrSteps = [.6,.6,.3,.3,.3,.3,.2,.2,.1,.1,.05,.05,.03,.03] #14, for version b (max=2)
contrSteps = [.3,.3,.2,.2,.1,.1,.05,.05,.02,.02,.01,.01,.005,.005,.003,.003] #16, for versions a or c (max=1)
print conditionsFilePath
# ====================================================================================

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='', extraInfo=expInfo, 
    runtimeInfo=None, originPath=None, savePickle=True, saveWideText=True, 
    dataFileName=filePath)
##save a log file for detail verbose info
#logFile = logging.LogFile(filePath+'.log', level=logging.EXP)
#logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1680, 1050), fullscr=False, screen=1, allowGUI=False, 
    allowStencil=False, monitor='testMonitor', color='black', colorSpace='rgb', 
    blendMode='avg', useFBO=True, units='deg')
# store frame rate of monitor if we can measure it successfully
#frameRate=win.getActualFrameRate()
frameRate=60
if frameRate!=None:
    frameDur = 1.0/round(frameRate)
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
#instrText = visual.TextStim(win=win, ori=0, name='instrText',
#    text='Indicate which direction the target is moving in:\n\n"comma (,)" = left\n"period (.)" = right \n\n The frame will turn *yellow* when the target disappeared.',
#    font='Cambria', pos=[0, 0], height=1, wrapWidth=10, color='white', \
#    colorSpace='rgb', opacity=1)
instrText = visual.TextStim(win=win, ori=0, name='instrText',
    text='Press any key to start', font='Cambria', pos=[0, 0], height=1, wrapWidth=10, color='white', \
    colorSpace='rgb', opacity=1)

# Initial positions of the mask:
maskInitPos = np.zeros((nMaskElements,2))

# Initialize components for Routine "trial"
trialClock = core.Clock()
moveClock = core.Clock()
maskMoveClock = core.Clock()
windowLeft = visual.Rect(win=win, name='windowLeft', width=[windowSize, 
    windowSize][0], height=[windowSize, windowSize][1], ori=0, 
    pos=[-windowOffsetX, windowOffsetY], 
    lineWidth=windowThickness, lineColor=u'white', lineColorSpace='rgb', 
    fillColor=None, opacity=1, interpolate=True)
windowRight = visual.Rect(win=win, name='windowRight', width=[windowSize, 
    windowSize][0], height=[windowSize, windowSize][1], ori=0, 
    pos=[windowOffsetX, windowOffsetY], lineWidth=windowThickness, 
    lineColor=u'white', lineColorSpace='rgb', 
    fillColor=None, opacity=1, interpolate=True)
blackBoxLeft = visual.Rect(win=win, name='blackBoxLeft', width=[blackBoxSize, 
    blackBoxSize][0], height=[blackBoxSize, blackBoxSize][1], ori=0, 
    pos=[-windowOffsetX, windowOffsetY], lineWidth=blackBoxThickness, 
    lineColor=u'black', 
    lineColorSpace='rgb', fillColor=None, opacity=1, interpolate=True)
blackBoxRight = visual.Rect(win=win, name='blackBoxRight', width=[blackBoxSize, 
    blackBoxSize][0], height=[blackBoxSize, blackBoxSize][1], ori=0, 
    pos=[windowOffsetX, windowOffsetY], lineWidth=blackBoxThickness, 
    lineColor=u'black', 
    lineColorSpace='rgb', fillColor=None, opacity=1, interpolate=True)
ISI = core.StaticPeriod(win=win, screenHz=frameRate, name='ISI')
# setting the edges to 3 (triangle) initially: this will change once ...
# ... the attributes are read from the configuration file:
target = visual.Polygon(win=win, name='target',units='deg', edges = 3, size=[0.1, 0.1],
    ori=45, pos=[0, 0], lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb', opacity=1, interpolate=True)
# field size needs to be changed later on in the code:
mask = visual.ElementArrayStim(win=win, name='mask', units='deg', 
    fieldSize=(windowSize,windowSize), fieldShape='circle',colors=(1,1,1),
    colorSpace='rgb', opacities=1, fieldPos=[0,0], sizes=1, nElements=nMaskElements, 
    elementMask=None, elementTex=None, sfs=3, xys=maskInitPos, interpolate=True)
    # note that fieldSize has no effect
# fixation crosses:
fixationLeft = visual.GratingStim(win, name='fixationLeft', color='white', 
    tex=None, mask='circle', size=0.2, pos=[-windowOffsetX, windowOffsetY])
fixationRight = visual.GratingStim(win, name='fixationRight', color='white', 
    tex=None, mask='circle', size=0.2, pos=[windowOffsetX, windowOffsetY])
# question text:
qntxtLeft = visual.TextStim(win=win, name='qntxtLeft',
    text='1=no experience\n2=weak glimpse\n3=almost clear\n4=absolutely clear',
    font='Cambria', pos=[-windowOffsetX, windowOffsetY], height=.55, wrapWidth=4.5,
    color='white', colorSpace='rgb', opacity=1)
qntxtRight = visual.TextStim(win=win, name='qntxtRight',
    text='1=no experience\n2=weak glimpse\n3=almost clear\n4=absolutely clear',
    font='Cambria', pos=[windowOffsetX, windowOffsetY], height=.55, wrapWidth=4.5,
    color='white', colorSpace='rgb', opacity=1)
# pause text:
pauseTextLeft = visual.TextStim(win=win, ori=0, name='pauseTextLeft',
    text='Press Spacebar to continue.', font='Cambria', alignHoriz='center',
    pos=[-windowOffsetX, windowOffsetY], height=.7, wrapWidth=3, color='white',
    colorSpace='rgb', opacity=1)
pauseTextRight = visual.TextStim(win=win, ori=0, name='pauseTextRight',
    text='Press Spacebar to continue.', font='Cambria', alignHoriz='center',
    pos=[windowOffsetX, windowOffsetY], height=.7, wrapWidth=3, color='white',
    colorSpace='rgb', opacity=1)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instrKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
instrKey.status = NOT_STARTED
# keep track of which components have finished
instructionsComponents = []
instructionsComponents.append(instrText)
instructionsComponents.append(instrKey)
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED


# ====================================================================================
## Preparing the mask and the target.
# Target starting position (assuming that the target is always presented to the non-dominant eye):
if expInfo['domEye'] == 'r': # if the dominant eye is right...
    targOffsetX = -windowOffsetX
    maskOffsetX = windowOffsetX
elif expInfo['domEye'] == 'l': # if the dominant eye is left...
    targOffsetX = windowOffsetX
    maskOffsetX = -windowOffsetX

# Creating a directory for storing staircase outputs:
if not os.path.exists(filePath):
    os.makedirs(filePath)

# Setting up the conditions:
condList = data.importConditions(conditionsFilePath)
conds = []
curCond = 0
commonNTrials = []
for thisCondition in condList:
    skipCond = False
    if thisCondition['cond']==expInfo['session']:
        if train:
            nTrials = thisCondition['trainTrials']
            if nTrials==0:
                skipCond = True
        else: 
            nTrials = thisCondition['exptTrials']
        if nTrials>0:
            print 'Number of trials in this condition: ' + str(nTrials)
            conds.append(thisCondition)
            # commonNTrials[curCond] = nTrials
            commonNTrials = nTrials
            curCond += 1
        else:
            print 'Skipping ' + thisCondition['cond']
    else:
        print 'Skipping ' + thisCondition['cond']
    
# Printing the attributes of the conds:  
print commonNTrials
trials = data.TrialHandler(conds, commonNTrials, extraInfo=expInfo)
trials.data.addDataType('RT')
# Creating a copy of the Conditions file for book-keeping and analyses:
shutil.copyfile(conditionsFilePath, filePath + os.sep + os.path.basename(conditionsFilePath))

#-------Start Routine "instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText* updates
    if t >= 0.0 and instrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrText.tStart = t  # underestimates by a little under one frame
        instrText.frameNStart = frameN  # exact frame index
        instrText.setAutoDraw(True)
    
    # *instrKey* updates
    if t >= 0.0 and instrKey.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrKey.tStart = t  # underestimates by a little under one frame
        instrKey.frameNStart = frameN  # exact frame index
        instrKey.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
        fixationLeft.setAutoDraw(True)
        fixationRight.setAutoDraw(True)
        windowLeft.setAutoDraw(True)
        windowRight.setAutoDraw(True)
    if instrKey.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ====================================================================================
# Initiating the trial loop

nDone=0
for thisTrial in trials:
    print '===new=trial==='
    nDone += 1
    print 'trial#' + str(nDone)
    # Annoyingly, the right side of the following appears everywhere. More 
    # efficient to store this as a variable since it is fixed (for a given trial):
    preStimInterval = 0 #np.random.rand(1)*thisTrial['targOnsetJit']
    trials.data.add('thisPreStimInterval', preStimInterval)
    stimOffset = (preStimInterval + (thisTrial['targMaxDur']-win.monitorFramePeriod*0.75))
    fadeInNofFrames = round( frameRate * (stimOffset - preStimInterval) )
    thisTargContin = thisTrial['targContin']
    thisMaskContin = thisTrial['maskContin']
    thisTask = thisTrial['taskDet0Dir1Loc2']
    # Variables set to random values:
    thisTargDir = np.random.choice([-1,1])
    trials.data.add('thisTargDir', thisTargDir)
    thisTargLoc = np.random.choice([thisTrial['targLoc1'], \
        thisTrial['targLoc2']])
    trials.data.add('thisTargLoc', thisTargLoc)
    thisTargInitPos = np.random.choice([0,.25,.5,.75])
    trials.data.add('thisTargInitPos', thisTargInitPos)
    # print 'thisTargInitPos: ' + str(thisTargInitPos)
    thisTargVertices = thisTrial['targVertices']
    thisMaskVertices = thisTrial['maskVertices']
    # Need to make sure that the square diameteres are somewhat reduced to match
    #   the area of the circle:
    if thisTargVertices == 4 and thisMaskVertices > 4:
        thisTargSize = thisTrial['targSize'] * 0.886
        thisMaskSize = thisTrial['maskSize']
    elif thisTargVertices > 4 and thisMaskVertices == 4:
        thisTargSize = thisTrial['targSize']
        thisMaskSize = thisTrial['maskSize'] * 0.886
    elif thisTargVertices == 4 and thisMaskVertices == 4:
        thisTargSize = thisTrial['targSize'] * 0.886
        thisMaskSize = thisTrial['maskSize'] * 0.886
    else:
        thisTargSize = thisTrial['targSize']
        thisMaskSize = thisTrial['maskSize']
    thisTargSpeed = thisTrial['targSpeed']
    print 'thisTargSpeed: ' + str(thisTargSpeed)
    if thisTargSpeed == 0:
        print 'blank trial'
        allSpeeds = [.3,1,2,3,5,8] # kind of sketchy to put it manually; need to fix it
        thisMaskSpeed = allSpeeds[np.random.choice(6)]
    else:
        print 'non-blank trial'
        thisMaskSpeed = thisTrial['maskSpeed']
        thisMaskFrameSpeed = thisMaskSpeed / 60
    if thisTargContin:
        thisTargSpeed = (thisTargSpeed/thisTargLoc)*57.296
        print 'thisTargSpeed: ' + str(thisTargSpeed)
        thisTargFrameSpeed = thisTargSpeed / 60
    thisTargColour = thisTrial['targColour']
    thisMaskColRed = thisTrial['maskColRed']
    thisMaskColGreen = thisTrial['maskColGreen']
    thisMaskColYellow = thisTrial['maskColYellow']
    thisMaskColBlue = thisTrial['maskColBlue']
    thisMaskColGrey = thisTrial['maskColGrey']
    targMaxDur = thisTrial['targMaxDur']
    targThreshT = thisTrial['targThreshT']
    targThreshN = targThreshT * 60 # for screenshot
    targDirSwitch = thisTrial['targDirSwitch']
    maskDirSwitch = thisTrial['maskDirSwitch']
    # What changes from trial to trial (will be different for dif expts)?
    # print 'thisTargLoc: ' + str(thisTargLoc)
    print 'thisMaskSpeed: ' + str(thisMaskSpeed)
    # print 'thisTargDir: ' + str(thisTargDir)
    #print 'thisTrial: ' + str(thisTrial)
    # Setting up the colour, shape, and size specifications:
    target.setFillColor(thisTargColour)
    target.setLineColor(thisTargColour)
    # shapes of the target and the mask:
    target.edges = thisTargVertices # updating the shape of the target
    if thisMaskVertices>4:
        mask.elementMask = 'circle'
    # sizes of the target and the mask:
    target.size = [thisTargSize, thisTargSize] # target size
    mask.sizes = [thisMaskSize, thisMaskSize] # mask size
    # Maximum travel distance from the centre - i.e., 'effective' radius:
    maxTravDist = (windowSize - thisTargSize) / 2
    if exptCond == 5: # controling for travel distance in 5th condition
        targMaxTravDist = maxTravDist*.5*thisTrial['targSpeed']/5
    else:
        targMaxTravDist = maxTravDist*.5
    # Resetting the starting positions of mask elements - 
    #  (assuming that the mask is different for every trial):
    if thisMaskContin:
        # Since the mask is moving circularly, x=position along the circle, y=r
        maskInitPosX = np.random.rand(nMaskElements,1)
        maskInitPosY = np.random.rand(nMaskElements,1)*0.85+0.15 # no clutter ar fixation
        thisMaskSpeed = (thisMaskSpeed/maskInitPosY)*57.296
        thisMaskFrameSpeed = (thisMaskFrameSpeed/maskInitPosY)*57.296
        maskMovePosX = maskInitPosX
        maskMovePosY = maskInitPosY
        maskDirections = [-1,1] # ccw, cw
    else: # discontinuous mask
        maskInitPosY = (np.random.rand(nMaskElements,1)*1.6-1)*maxTravDist
        # print maskInitPosY
        # cord length = 2*r*(arccos(height/r))
        cordLength = 2*1*np.sin(np.arccos(maskInitPosY/maxTravDist))
        # print cordLength # looks correct
        maskInitPosX = (np.random.rand(nMaskElements,1)*2-1)#*maxTravDist
        # print maskInitPosX
        maskInitPosX = maskInitPosX * cordLength
        # print maskInitPosX
        maskDirections = [[1,0],[-1,0],[0,1],[0,-1]] # right, left, up, down

    maskSpeedMult = np.random.rand(nMaskElements,1)*.6+.7

    # Picking a list of directions. If there are four allowed directions, 
    #  one out of four needs to be picked for each element equally. 
    #  [1 4 2 3 4 2 1 3...]
    # number of times to repeat the directions: 
    maskDirectionNumReps = nMaskElements/np.shape(maskDirections)[0] 
    maskDirectionIndices = np.repeat(range(1,5), maskDirectionNumReps)
    maskDirs = np.random.permutation(np.repeat(maskDirections,
        maskDirectionNumReps,0))
    # Setting the mask colours.
    maskColIDs = np.array([thisMaskColRed, thisMaskColBlue, thisMaskColGreen,
        thisMaskColYellow])
    if subjThresh > 1:
        thisMaskContr = 2 - subjThresh
    else:
        thisMaskContr = 1
    maskColContr = -1 + 2*thisMaskContr
    maskColAll = np.array([[maskColContr,-1,-1], [-1,-1,maskColContr],
        [-1,maskColContr,-1], [maskColContr,maskColContr,-1]]) 
    maskColCurSet = maskColAll[maskColIDs==1]
    maskColNumReps = nMaskElements/np.shape(maskColCurSet)[0]
    maskColCurSetRepd = np.repeat(maskColCurSet, maskColNumReps, 0)
    maskColours = np.random.permutation(maskColCurSetRepd)
    mask.setColors(maskColours)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    nMaskMove = 0
    key_pressed = False
    key_pause = False
    windowLeft.lineColor = 'white'
    windowRight.lineColor = 'white'
    # Vertical offset of the target - this is only used in disc scen
    targOffsetY = windowOffsetY + thisTargLoc #*targVertOffset
    # update component parameters for each repeat
    key_upDown = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_upDown.status = NOT_STARTED
    key_space = event.BuilderKeyResponse()
    key_space.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(windowLeft)
    trialComponents.append(windowRight)
    trialComponents.append(ISI)
    trialComponents.append(target)
    trialComponents.append(mask)
    trialComponents.append(qntxtLeft)
    trialComponents.append(qntxtRight)
    trialComponents.append(fixationLeft)
    trialComponents.append(fixationRight)
    trialComponents.append(key_upDown)
    trialComponents.append(key_space)
    trialComponents.append(pauseTextLeft)
    trialComponents.append(pauseTextRight)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
        #-------Start Routine "trial"-------
    continueRoutine = True

    # screenshot variables:
    frameMax = 60 * targMaxDur
    screenshotName = 'targ' + str(thisTargContin) + '-v' + str(thisTrial['targSpeed']) + '_' + \
                     'mask' + str(thisMaskContin) + '-v' + str(thisTrial['maskSpeed']) + '_'
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1 # number of completed frames (0 is the first frame)
        if frameN <= frameMax:
            print 'frameN = ' + str(frameN)
        # update/draw components on each frame
        
        # *windowLeft* updates
        if windowLeft.status == NOT_STARTED:
            # keep track of start time/frame for later
            windowLeft.tStart = t  # underestimates by a little under one frame
            windowLeft.frameNStart = frameN  # exact frame index
            windowLeft.setAutoDraw(True)
            fixationLeft.setAutoDraw(True)
            blackBoxLeft.setAutoDraw(True)
        
        # *windowRight* updates
        if windowRight.status == NOT_STARTED:
            # keep track of start time/frame for later
            windowRight.tStart = t  # underestimates by a little under one frame
            windowRight.frameNStart = frameN  # exact frame index
            windowRight.setAutoDraw(True)
            fixationRight.setAutoDraw(True)
            blackBoxRight.setAutoDraw(True)

        # pause text (after the response is made):
        if ~key_pause and frameN > frameMax:
            qntxtLeft.setAutoDraw(False)
            qntxtRight.setAutoDraw(False)
            pauseTextLeft.setAutoDraw(True)
            pauseTextRight.setAutoDraw(True)
            if 'space' in event.getKeys(keyList=['space']):
                print 'spacebar pressed - continuing to the next trial'
                key_pause = True

        # *mask* updates
        if mask.status == NOT_STARTED:
            mask.tStart = t
            mask.frameNStart = frameN
            # setting the initial positions for the mask elements
            maskInitPos = np.concatenate((maskInitPosX, maskInitPosY), axis=1)
            mask.xys = maskInitPos
            mask.fieldPos = [maskOffsetX, windowOffsetY]
            mask.setAutoDraw(True)
            #maskMoveClock.reset()
            nMaskMove = 0
            maskTrajLength = 2*np.pi*nRev*thisMaskFrameSpeed*maskSpeedMult/360 # trajLen is diff for diff r
            maskCjit = np.random.rand(nMaskElements) # jittered location along c
        if mask.status == STARTED and frameN < frameMax:
            if thisMaskContin:
                if maskDirSwitch:
                    # tc%2 # cycles travelled in this odd-even cycle:
                    tc = (frameN - mask.frameNStart) / nRev
                    # jittered location along c:
                    c = np.remainder(np.array([maskCjit+np.repeat(tc,nMaskElements)]).T,2)
                    maskTravAngles = 2*np.pi * maskInitPosX + np.array([maskDirs]).T * \
                                maskTrajLength * (np.floor(c) + np.ceil(c)%2*c - np.floor(c) * c%1)
                    maskPosX=maskInitPosY*np.cos(maskTravAngles)*maxTravDist
                    maskPosY=maskInitPosY*np.sin(maskTravAngles)*maxTravDist
                    mask.xys = np.concatenate((maskPosX, maskPosY), axis=1)
                    mask.oris = np.reshape(-maskTravAngles.T*360/(2*np.pi), nMaskElements)
                else:
                    maskCurPosX = maskInitPosX + \
                        np.array([maskDirs]).T*(frameN-mask.frameNStart)*thisMaskFrameSpeed*\
                        maskSpeedMult/360
                    maskMovePosX = maxTravDist*maskInitPosY*np.cos(2*np.pi*maskCurPosX)
                    maskMovePosY = maxTravDist*maskInitPosY*np.sin(2*np.pi*\
                        (maskInitPosX+np.array([maskDirs]).T*(frameN-mask.frameNStart)*\
                        thisMaskFrameSpeed*maskSpeedMult/360))
                    mask.xys = np.concatenate((maskMovePosX, maskMovePosY), axis=1)
                    mask.oris = np.reshape(-maskCurPosX.T * 360, nMaskElements)
            else: # discontinuous mask
                if nMaskMove == 0:
                    #tMaskMove = frameDur # maskMoveClock.getTime()
                    nMaskMove = 1 # move one frame on each iteration?
                    #tMaskRec = maskMoveClock.getTime()
                    nMaskRec = frameN
                    maskMovePos = maskInitPos
                else:
                    #tMaskMove = maskMoveClock.getTime() - tMaskRec
                    nMaskMove = frameN - nMaskRec
                    #tMaskRec = maskMoveClock.getTime()
                    nMaskRec = frameN
                maskMovePos = np.array(maskMovePos) + np.array(maskDirs) * \
                    thisMaskFrameSpeed * nMaskMove
                posSq = np.sqrt(np.square(maskMovePos[:,0]) + np.square(maskMovePos[:,1]))
                maskElemsOutside = np.where(posSq>=maxTravDist)
                # print maskElemsOutside
                maskMovePos[maskElemsOutside] = maskMovePos[maskElemsOutside] - \
                    1.95 * np.square(np.array(maskDirs[maskElemsOutside])) * \
                    maskMovePos[maskElemsOutside]
                mask.xys = maskMovePos
        if mask.status == STARTED and frameN >= frameMax:
            mask.setAutoDraw(False)

        # *target* updates
        if target.status == NOT_STARTED:
            # keep track of start time/frame for later
            target.tStart = t  # underestimates by a little under one frame
            target.frameNStart = frameN  # exact frame index
            target.setAutoDraw(True)
            trajLength = 2*np.pi*nRev*thisTargFrameSpeed/360
            # print trajLength
            if not exptCond == 6:
                edgeReached = False # this is only true for the first cycle
                curRefAngle = thisTargInitPos
                #moveClock.reset()
                nMove = 0
        if target.status == STARTED and frameN < frameMax:
            curFrameN = frameN - target.frameNStart
            # Target opacity
            if thisTargSpeed!=0:
                targOpacity = ((frameMax/targThreshN)*subjThresh) * \
                              (curFrameN/fadeInNofFrames)
                if targOpacity>1:
                    target.opacity = 1
                else:
                    target.opacity = targOpacity
            else:
                target.opacity = 0
            # Clocking the time spent moving:
            #tMove = moveClock.getTime()
            nMove = frameN
            if thisTargContin:
                if targDirSwitch:
                    #tc = (t - target.tStart) / tRev # total cycles travelled
                    c =  ((frameN - target.frameNStart) / nRev)%2 # tc%2 # cycles travelled in this odd-even cycle
                    #oc = np.floor(c) + np.ceil(c)%2*c # odd cycle
                    #ec = np.floor(c) * c%1 # even cycle in reverse direction
                    travAngle = 2*np.pi * thisTargInitPos + thisTargDir * trajLength * \
                                (np.floor(c) + np.ceil(c)%2*c - np.floor(c) * c%1) #(oc - ec) * 
                    #print 'tc='+str(tc)+'; c='+str(c)+'; oc='+str(oc)+'; ec='+str(ec)+'; a='+str(travAngle)
                else:
                    travAngle = 2*np.pi*(curRefAngle+thisTargDir*nMove*\
                            thisTargFrameSpeed/360)
                targPosX=thisTargLoc*np.cos(travAngle)+targOffsetX
                targPosY=thisTargLoc*np.sin(travAngle)+windowOffsetY
                target.pos = [targPosX, targPosY]
            else:
                if edgeReached: # if the edge is reached, reappear on the other end
                    travDist = nMove*thisTargFrameSpeed-targMaxTravDist
                else: # otherwise, start from the initial target position:
                    # note that this is only for the first cycle!
                    travDist = nMove*thisTargFrameSpeed+thisTargInitPos
                # if the target has already moved beyond max allowed travel dist
                if travDist > targMaxTravDist:
                    edgeReached = True
                    #moveClock.reset() # reset the movement clock (set it to zero)
                    #tMove = moveClock.getTime() # get the time
                    nMove = 0
                    # use that reset time for new travDist, but start from the edge
                    travDist = nMove*thisTargFrameSpeed-targMaxTravDist
                # target movement:
                target.pos = [targOffsetX+thisTargDir*travDist,targOffsetY]
        if target.status == STARTED and frameN >= frameMax:
            target.setAutoDraw(False)
        
        # *key_upDown* updates
        if key_upDown.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_upDown.tStart = t  # underestimates by a little under one frame
            key_upDown.frameNStart = frameN  # exact frame index
            key_upDown.status = STARTED
            # keyboard checking is just starting
            key_upDown.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_upDown.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0 and not key_pressed:
                print 'key pressed'
                thisRT = key_upDown.clock.getTime()
                key_pressed = True

        # wait for the presentation time to pass to terminate the trial:
        if key_pause:
            if not key_pressed:
                print 'no response was made'
                trials.data.add('RT', 0)
            else:
                print 'RT: ' + str(thisRT)
                trials.data.add('RT', thisRT)
            continueRoutine = False
        # *ISI* period
        if ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(ISIduration)
        #one frame should pass before updating params and completing
        elif ISI.status == STARTED: 
            ISI.complete() #finish the static period
        
        # check if all components have finished
        # a component has requested a forced-end of Routine:
        if not continueRoutine: 
            # if we abort early the non-slip timer needs reset:
            routineTimer.reset() 
            break
        # will revert to True if at least one component still running
        continueRoutine = False  
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and \
                    thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        # don't flip if this routine is over or we'll get a blank screen
        if continueRoutine:  
            win.flip()
            # taking a screenshot of the image:
            if frameN > 0 and frameN <= frameMax:
                win.getMovieFrame() #(buffer='back')
                win.saveMovieFrames(screenshotName + str(frameN).zfill(3) + '.png')
        else: # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    thisExp.nextEntry()

trialsFilePath = filePath + os.sep + fileName + '_trials'
trials.saveAsPickle(trialsFilePath)
trials.saveAsText(trialsFilePath)
print trials
print "finished the experiment"

win.close()
core.quit()
