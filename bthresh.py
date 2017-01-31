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

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'dm'  # from the Builder filename that created this script
expInfo = {u'paradigm': u't-dscm01b', u'domEye': u'r', u'participant': u'', u'training': u'1'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName) # dialogue box
if dlg.OK == False: core.quit()  # user pressed cancel
# expInfo['date'] = data.getDateStr()  # add a simple timestamp
timeNow = datetime.now()
expInfo['date'] = datetime.now().strftime('%Y-%m-%d_%H%M')
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
dataDir = '..' + os.sep + 'data'
fileName = 'bthresh_%s_%s_t%s_%s_dom-%s_%s' %(expName, 
    expInfo['paradigm'], expInfo['training'], expInfo['participant'], 
    expInfo['domEye'], expInfo['date'])
filePath = dataDir + os.sep + fileName
print filePath

# ====================================================================================
## Initial variables.
# Window boxes and black boxes (specified in degrees of visual angles [dva]):
windowSize = 5.03 # 4.47
windowOffsetX = 5.62 # 5.6 # 6.7
windowOffsetY = 5.5 # 2.83 # 4.97
windowThickness = 2
# targVertOffset = 1.5
blackBoxSize = windowSize + 0.5
blackBoxThickness = 10
# Mask variables:
nMaskElements = 248 # 300 must be divisible by the number of directions allowed (below)
# Timing variables (in seconds) and trial number:
targMaxDur = 3 # 3.6s in the Moors paper
targThreshT = 2 # the subject needs to break before this time
ISIduration = 0.0 # 0.5 before
# Contrast:
contrMin = 0
contrMax = 2
# Condition-related variables
conditionsFileName = 'cond-expt-'+expInfo['paradigm']+'.csv'
conditionsFilePath = 'cond-files'+os.sep+conditionsFileName
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

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1680, 1050), fullscr=False, screen=1, allowGUI=False, 
    allowStencil=False, monitor='testMonitor', color='black', colorSpace='rgb', 
    blendMode='avg', useFBO=True, units='deg')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
    frameRate = expInfo['frameRate']
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess
    frameRate = 60
print frameRate

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instrText = visual.TextStim(win=win, ori=0, name='instrText', 
                            text='Press any key to continue',
                            font='Cambria', pos=[0, 0], height=1,
                            wrapWidth=10, color='white', 
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

# Setting up the staircases.
stairConds = data.importConditions(conditionsFilePath)
# print stairConds
if train:
    nConditions = np.size(stairConds)
else:
    nConditions = np.size(stairConds)
print "number of non-training conditions: " + str(nConditions)

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

# Setting up each staircase, one by one:
stairs=[] # setting up a variable containing all our staircases
for thisCondition in stairConds:
    # Some variables to be reset at each iteration:
    termNRevs = False # these two variables track whether the stairc termination...
    termNTrials = False # ...relies on the number of trials or reversals.
    skipStairc = False
    # Number of trials/reversals for termination - need to establish which
    if train:
        nTrialsPerStair = thisCondition['trainTrials']
        nRevsPerStair = thisCondition['trainRevs']
        if nTrialsPerStair==0 and nRevsPerStair>0:
            termNRevs = True
            print 'nRevsPerStair = ' + str(nRevsPerStair)
        elif nTrialsPerStair>0 and nRevsPerStair==0:
            termNTrials = True
            print 'nTrialsPerStair = ' + str(nTrialsPerStair)
        elif nTrialsPerStair==0 and nRevsPerStair==0:
            skipStairc = True
        else:
            print 'ATTENTION! Make sure that either trainTrials or trainRevs ' + \
                'is 0 in the conditions file!'
    else: 
        nTrialsPerStair = thisCondition['exptTrials']
        nRevsPerStair = thisCondition['exptRevs']
        if nTrialsPerStair==0 and nRevsPerStair>0:
            termNRevs = True
            print 'nRevsPerStair = ' + str(nRevsPerStair)
        elif nTrialsPerStair>0 and nRevsPerStair==0:
            termNTrials = True
            print 'nTrialsPerStair = ' + str(nTrialsPerStair)
        elif nTrialsPerStair==0 and nRevsPerStair==0:
            skipStairc = True
        else:
            print 'ATTENTION! Make sure that either exptTrials or exptRevs ' + \
                'is 0 in the conditions file!'
    thisStair = data.StairHandler(startVal = thisCondition['startVal'],
        extraInfo = thisCondition, nTrials=nTrialsPerStair, nReversals=nRevsPerStair,
        nUp=2, nDown=1, minVal = contrMin, maxVal = contrMax, #~66% breaking rate
        stepSizes = contrSteps[0:nRevsPerStair+1], stepType='lin')
    if not skipStairc:
        stairs.append(thisStair) # appending and 'setting' (?) this stairc
        thisStair.setExp(thisExp)
    
# Printing the attributes of the stairs:  
#print dir(stairs[0])
print stairs
# Creating a copy of the Conditions file for book-keeping and analyses:
shutil.copyfile(conditionsFilePath, filePath + os.sep + conditionsFileName)

# ====================================================================================

# for trialN in range(nTrialsPerStair):
while len(stairs)>0:
    print '===new=trial==='
    shuffle(stairs) # randomizing the appearance of the stairs for each trial
    thisStair = stairs.pop()
    try:
        thisIntensity = thisStair.next() # contrast value
    except StopIteration:
        print 'reversals:'
        print thisStair.reversalIntensities
        if train:
            print 'mean of final 6 reversals = %.3f' \
                  %(np.average(thisStair.reversalIntensities[-6:]))
        else:
            print 'mean of final 4 reversals = %.3f' \
                  %(np.average(thisStair.reversalIntensities[-4:]))
        stairFilePath = filePath + os.sep + '%s_stair-%s' %(fileName, 
            thisStair.extraInfo['label']) 
        thisStair.saveAsPickle(stairFilePath)
        thisStair.saveAsText(stairFilePath)
        print "finished staircase"
    else:
    #for thisStair in stairs:
        # Based on the current staircase, assigning the current contrast value and
        #  other variables:
        thisIntensity = thisStair.next() # contrast value
        if thisIntensity <= 1:
            thisTargContr = thisIntensity
            thisMaskContr = 1
        else:
            thisTargContr = 1
            thisMaskContr = 2 - thisIntensity
        thisTargContin = thisStair.extraInfo['targContin']
        thisMaskContin = thisStair.extraInfo['maskContin']
        thisTask = thisStair.extraInfo['taskDet0Dir1Loc2']
        # Timing variables:
        preStimInterval = np.random.rand(1)*.5
        stimOffset = preStimInterval + targMaxDur
        print 'frame rate: ' + str(frameRate)
        print 'targ maximum duration: ' + str(targMaxDur)
        fadeInNofFrames = round(frameRate*targMaxDur)
        # Variables set to random values:
        thisTargDir = np.random.choice([-1,1])
        thisTargLoc = np.random.choice([thisStair.extraInfo['targLoc1'], \
            thisStair.extraInfo['targLoc2']])
        thisTargInitPos = np.random.choice([thisStair.extraInfo['targInitPos1'],\
            thisStair.extraInfo['targInitPos2'],thisStair.extraInfo['targInitPos3']])
        # print 'thisTargInitPos: ' + str(thisTargInitPos)
        thisTargVertices = thisStair.extraInfo['targVertices']
        thisMaskVertices = thisStair.extraInfo['maskVertices']
        # Need to make sure that the square diameteres are somewhat reduced to match
        #   the area of the circle:
        if thisTargVertices == 4 and thisMaskVertices > 4:
            thisTargSize = thisStair.extraInfo['targSize'] * 0.886
            thisMaskSize = thisStair.extraInfo['maskSize']
        elif thisTargVertices > 4 and thisMaskVertices == 4:
            thisTargSize = thisStair.extraInfo['targSize']
            thisMaskSize = thisStair.extraInfo['maskSize'] * 0.886
        elif thisTargVertices == 4 and thisMaskVertices == 4:
            thisTargSize = thisStair.extraInfo['targSize'] * 0.886
            thisMaskSize = thisStair.extraInfo['maskSize'] * 0.886
        else:
            thisTargSize = thisStair.extraInfo['targSize']
            thisMaskSize = thisStair.extraInfo['maskSize']
        thisTargSpeed = thisStair.extraInfo['targSpeed']
        if thisTargContin:
            thisTargSpeed = (thisTargSpeed/thisTargLoc)*57.296
        thisTargColour = thisStair.extraInfo['targColour']
        thisMaskSpeed = thisStair.extraInfo['maskSpeed']
        thisMaskColRed = thisStair.extraInfo['maskColRed']
        thisMaskColGreen = thisStair.extraInfo['maskColGreen']
        thisMaskColYellow = thisStair.extraInfo['maskColYellow']
        thisMaskColBlue = thisStair.extraInfo['maskColBlue']
        thisMaskColGrey = thisStair.extraInfo['maskColGrey']
        # What changes from trial to trial (will be different for dif expts)?
        print 'thisIntensity (contrast): start=%.2f, current=%.3f' \
            %(thisStair.extraInfo['startVal'], thisIntensity)
        # print 'thisTargLoc: ' + str(thisTargLoc)
        # print 'thisMaskSpeed: ' + str(thisMaskSpeed)
        # print 'thisTargDir: ' + str(thisTargDir)
        #print 'thisCondition: ' + str(thisCondition)
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
        # Resetting the starting positions of mask elements - 
        #  (assuming that the mask is different for every trial):
        if thisMaskContin:
            # Since the mask is moving circularly, x=position along the circle, y=r
            maskInitPosX = np.random.rand(nMaskElements,1)
            maskInitPosY = np.random.rand(nMaskElements,1)*0.85+0.15 # no clutter ar fixation
            thisMaskSpeed = (thisMaskSpeed/maskInitPosY)*57.296
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
        tMaskMove = 0
        key_pressed = False
        key_pause = False
        respRecorded = False
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
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1 # number of completed frames (0 is the first frame)
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
            if ~key_pause and t > stimOffset:
                pauseTextLeft.setAutoDraw(True)
                pauseTextRight.setAutoDraw(True)

            # *mask* updates
            if mask.status == NOT_STARTED and t > preStimInterval:
                mask.tStart = t
                mask.frameNStart = frameN
                # setting the initial positions for the mask elements
                maskInitPos = np.concatenate((maskInitPosX, maskInitPosY), axis=1)
                mask.xys = maskInitPos
                mask.fieldPos = [maskOffsetX, windowOffsetY]
                mask.setAutoDraw(True)
                maskMoveClock.reset()
            if mask.status == STARTED and t > preStimInterval and t < stimOffset:
                if thisMaskContin:
                    maskCurPosX = maskInitPosX + \
                        np.array([maskDirs]).T*(t-mask.tStart)*thisMaskSpeed*\
                        maskSpeedMult/360
                    maskMovePosX = maxTravDist*maskInitPosY*np.cos(2*np.pi*maskCurPosX)
                    maskMovePosY = maxTravDist*maskInitPosY*np.sin(2*np.pi*\
                        (maskInitPosX+np.array([maskDirs]).T*(t-mask.tStart)*\
                        thisMaskSpeed*maskSpeedMult/360))
                    mask.xys = np.concatenate((maskMovePosX, maskMovePosY), axis=1)
                    mask.oris = np.reshape(-maskCurPosX.T * 360, nMaskElements)
                else: # discontinuous mask
                    if tMaskMove == 0:
                        tMaskMove = frameDur # maskMoveClock.getTime()
                        tMaskRec = maskMoveClock.getTime()
                        maskMovePos = maskInitPos
                    else:
                        tMaskMove = maskMoveClock.getTime() - tMaskRec
                        tMaskRec = maskMoveClock.getTime()
                    maskMovePos = np.array(maskMovePos) + np.array(maskDirs) * \
                        thisMaskSpeed * tMaskMove
                    posSq = np.sqrt(np.square(maskMovePos[:,0]) + \
                        np.square(maskMovePos[:,1]))
                    maskElemsOutside = np.where(posSq>=maxTravDist)
                    # print maskElemsOutside
                    maskMovePos[maskElemsOutside] = maskMovePos[maskElemsOutside] - \
                        1.95 * np.square(np.array(maskDirs[maskElemsOutside])) * \
                        maskMovePos[maskElemsOutside]
                    mask.xys = maskMovePos
            if mask.status == STARTED and t >= stimOffset:
                mask.setAutoDraw(False)

            # *target* updates
            if t >= preStimInterval and target.status == NOT_STARTED:
                # keep track of start time/frame for later
                target.tStart = t  # underestimates by a little under one frame
                target.frameNStart = frameN  # exact frame index
                target.setAutoDraw(True)
                edgeReached = False # this is only true for the first cycle
                moveClock.reset()
            if target.status == STARTED:
                curFrameN = frameN - target.frameNStart
                # Target opacity
                if thisTargSpeed>0:
                    targOpacity = ((targMaxDur/targThreshT)*thisIntensity) \
                                  * (curFrameN/fadeInNofFrames)
                    if targOpacity>1:
                        target.opacity = 1
                    else:
                        target.opacity = targOpacity
                else:
                    target.opacity = 0
                # Clocking the time spent moving:
                tMove = moveClock.getTime()
                if thisTargContin:
                    targPosX=thisTargLoc*np.cos(2*np.pi*(thisTargInitPos+\
                             thisTargDir*(t-target.tStart)*\
                             thisTargSpeed/360))+targOffsetX
                    targPosY=thisTargLoc*np.sin(2*np.pi*(thisTargInitPos+\
                             thisTargDir*(t-target.tStart)*thisTargSpeed/360))+\
                             windowOffsetY
                    target.pos = [targPosX, targPosY]
                else:
                    if edgeReached: # if the edge is reached, reappear on the other end
                        travDist = tMove*thisTargSpeed-(maxTravDist*.5)
                    else: # otherwise, start from the initial target position:
                        # note that this is only for the first cycle!
                        travDist = tMove*thisTargSpeed+thisTargInitPos
                    # if the target has already moved beyond max allowed travel dist
                    if travDist > (maxTravDist*.5):
                        edgeReached = True
                        moveClock.reset() # reset the movement clock (set it to zero)
                        tMove = moveClock.getTime() # get the time
                        # use that reset time for new travDist, but start from the edge
                        travDist = tMove*thisTargSpeed-(maxTravDist*.5)
                    # target movement:
                    target.pos = [targOffsetX+thisTargDir*travDist, \
                        targOffsetY]
            if target.status == STARTED and t >= stimOffset:
                target.setAutoDraw(False)

            # *key_space* updates
            if ~key_pause and t >= stimOffset:
#                spaceKey = event.getKeys(keyList=['space'])
                if 'space' in event.getKeys(keyList=['space']):
                    print 'spacebar pressed'
                    key_pause = True
            
            # *key_upDown* updates
            if t >= preStimInterval and key_upDown.status == NOT_STARTED:
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
                    key_pressed = True
                    thisRT = key_upDown.clock.getTime()
                    # was this 'correct'? i.e., pressed .5<t<2s?
                    if t > (preStimInterval+.5) and \
                       t < (stimOffset-(targMaxDur-targThreshT)):
                        key_upDown.corr = 1
                        print '"correct" response - took ' + str(thisRT)
                    else:
                        key_upDown.corr = 0
                        print '"incorrect" response - took ' + str(thisRT)

            # if key is not pressed, and the pause key is pressed, terminate the trial
            if not key_pressed and key_pause and t>= stimOffset:
                thisStair.addData(0) # recording as 'incorrect'
                thisStair.addOtherData('key_upDown.rt', 0)
                respRecorded = True
                print '"incorrect" response recorded - button not pressed'
                
            # if key is pressed, wait for the presentation time to pass to terminate\
            #   the trial:
            if key_pressed and key_pause and t >= stimOffset:
                # update staircase with the last response:
                thisStair.addData(key_upDown.corr)
                thisStair.addOtherData('key_upDown.rt', thisRT)
                respRecorded = True
                print 'response recorded'

            # if the response is recorded, terminate the trial
            if respRecorded:
                # update staircase with the random variable combination:
                thisStair.addOtherData('thisTargDir', thisTargDir)
                thisStair.addOtherData('thisTargLoc', thisTargLoc)
                thisStair.addOtherData('thisTargInitPos', thisTargInitPos)
                print 'reversal intensities for stair %s:' \
                      %(thisStair.extraInfo['label'])
                print thisStair.reversalIntensities
                # a response ends the routine
                stairs.append(thisStair)
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
            else: # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        thisExp.nextEntry()

win.close()
core.quit()
