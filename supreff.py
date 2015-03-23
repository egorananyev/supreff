#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.00), Mon Mar 16 14:30:23 2015
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# ====================================================================================
## Initial variables (specified in visual angles):
# Window boxes and black boxes:
windowSize = 4.47
windowOffsetX = 6.71
windowOffsetY = 4.97
windowThickness = 2
targVertOffset = 1.5
blackBoxSize = windowSize + 0.5
blackBoxThickness = 10
# Mask variables:
nMaskElements = 160 # must be divisible by the number of directions allowed (below)
maskDirections = [[1,0],[-1,0],[0,1],[0,-1]] # right, left, up, down
# Timing variables:
preStimInterval = 1
stimDuration = 3.6
ISIduration = 0.5
fadeInNofFrames = 20 # the number of frames for the fade-in
# ====================================================================================

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'supreff'  # from the Builder filename that created this script
expInfo = {u'session': u'01', u'domEye': u'r', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data' + os.sep + '%s_%s_%s_%s_%s' %(expName, 
    expInfo['participant'], expInfo['domEye'], expInfo['session'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='', extraInfo=expInfo, runtimeInfo=None,
    originPath=None, savePickle=True, saveWideText=True, dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb', blendMode='avg', useFBO=True, units='deg')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instrText = visual.TextStim(win=win, ori=0, name='instrText',
    text='Indicate whether the red \ncircle appeared above or \nbelow fixation.\n\n"up" = above\n"down" = below',
    font='Cambria', pos=[0, 0], height=1, wrapWidth=None, color='white', colorSpace='rgb', opacity=1, depth=0.0)

# Initial positions of the mask:
maskInitPos = np.zeros((nMaskElements,2))

# Initialize components for Routine "trial"
trialClock = core.Clock()
moveClock = core.Clock()
maskMoveClock = core.Clock()
windowLeft = visual.Rect(win=win, name='windowLeft', width=[windowSize, windowSize][0], 
    height=[windowSize, windowSize][1], ori=0, pos=[-windowOffsetX, windowOffsetY], lineWidth=windowThickness, 
    lineColor=u'white', lineColorSpace='rgb', fillColor=None, opacity=1, interpolate=True)
windowRight = visual.Rect(win=win, name='windowRight', width=[windowSize, windowSize][0], 
    height=[windowSize, windowSize][1], ori=0, pos=[windowOffsetX, windowOffsetY], lineWidth=windowThickness, 
    lineColor=u'white', lineColorSpace='rgb', fillColor=None, opacity=1, interpolate=True)
blackBoxLeft = visual.Rect(win=win, name='blackBoxLeft', width=[blackBoxSize, blackBoxSize][0], 
    height=[blackBoxSize, blackBoxSize][1], ori=0, pos=[-windowOffsetX, windowOffsetY], 
    lineWidth=blackBoxThickness, lineColor=u'black', lineColorSpace='rgb',
    fillColor=None, opacity=1, interpolate=True)
blackBoxRight = visual.Rect(win=win, name='blackBoxRight', width=[blackBoxSize, blackBoxSize][0], 
    height=[blackBoxSize, blackBoxSize][1], ori=0, pos=[windowOffsetX, windowOffsetY], 
    lineWidth=blackBoxThickness, lineColor=u'black', lineColorSpace='rgb',
    fillColor=None, opacity=1, interpolate=True)
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
# setting the edges to 3 (triangle) initially: this will change once ...
# ... the attributes are read from the configuration file:
target = visual.Polygon(win=win, name='target',units='deg', edges = 3, size=[0.1, 0.1],
    ori=0, pos=[0, 0], lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb', opacity=1, interpolate=True)
# field size needs to be changed later on in the code:
mask = visual.ElementArrayStim(win=win, name='mask', units='deg', fieldSize=(windowSize,windowSize),
    fieldShape='sqr', colors=(1,1,1), colorSpace='rgb', opacities=1, fieldPos=[0,0], sizes=1,
    nElements=nMaskElements, elementMask=None, elementTex=None, sfs=3, xys=maskInitPos, interpolate=True)

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

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=4, method='random', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('cond-expt01.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

# ====================================================================================
## Preparing the mask and the target.
# Setting up the size specifications:
target.size = [targSize, targSize] # target size
mask.sizes = [maskSize, maskSize] # mask size
# Target starting position (assuming that the target is always presented to the non-dominant eye):
if expInfo['domEye'] == 'r': # if the dominant eye is right...
    targOffsetX = -windowOffsetX
    maskOffsetX = windowOffsetX
elif expInfo['domEye'] == 'l': # if the dominant eye is left...
    targOffsetX = windowOffsetX
    maskOffsetX = -windowOffsetX
# Maximum travel distance from the initial position:
maxTravDist = (windowSize - targSize/1) / 2
# Resetting the starting positions of mask elements (assuming that the mask is the same for every trial):
maskInitPos = (np.random.rand(nMaskElements,2)*2-1)*maxTravDist
# Picking a list of directions. If there are four allowed directions, one out of ...
# ... four needs to be picked for each element equally. [1 4 2 3 4 2 1 3...]
maskDirectionNumReps = nMaskElements/np.shape(maskDirections)[0] # number of times to repeat the directions
maskDirectionIndices = np.repeat(range(1,5), maskDirectionNumReps)
maskDirs = np.random.permutation(np.repeat(maskDirections,maskDirectionNumReps,0))
# Setting the mask colours.
maskColIDs = np.array([maskColRed, maskColBlue, maskColGreen, maskColYellow])
maskColAll = np.array([[1,-1,-1], [-1,-1,1], [-1,1,-1], [1,1,-1]])
maskColCurSet = maskColAll[maskColIDs==1]
maskColNumReps = nMaskElements/np.shape(maskColCurSet)[0]
maskColCurSetRepd = np.repeat(maskColCurSet, maskColNumReps,0)
maskColours = np.random.permutation(maskColCurSetRepd)
mask.colors = maskColours
# ====================================================================================

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    tMaskMove = 0
    # Vertical offset of the target (dependent on the type of trial):
    if targLoc == 'above':
        targOffsetY = windowOffsetY + targVertOffset
    elif targLoc == 'below':
        targOffsetY = windowOffsetY - targVertOffset
    # update component parameters for each repeat
    target.edges = targVertices # updating the shape of the target
    target.setFillColor(targColour)
    target.setLineColor(targColour)
    key_upDown = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_upDown.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(windowLeft)
    trialComponents.append(windowRight)
    trialComponents.append(ISI)
    trialComponents.append(target)
    trialComponents.append(mask)
    trialComponents.append(key_upDown)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *windowLeft* updates
        if windowLeft.status == NOT_STARTED:
            # keep track of start time/frame for later
            windowLeft.tStart = t  # underestimates by a little under one frame
            windowLeft.frameNStart = frameN  # exact frame index
            windowLeft.setAutoDraw(True)
            blackBoxLeft.setAutoDraw(True)
        if windowLeft.status == STARTED and t >= (preStimInterval+stimDuration-win.monitorFramePeriod*0.75):
            windowLeft.setAutoDraw(False)
            blackBoxLeft.setAutoDraw(False)
        
        # *windowRight* updates
        if windowRight.status == NOT_STARTED:
            # keep track of start time/frame for later
            windowRight.tStart = t  # underestimates by a little under one frame
            windowRight.frameNStart = frameN  # exact frame index
            windowRight.setAutoDraw(True)
            blackBoxRight.setAutoDraw(True)
        if windowRight.status == STARTED and t >= (preStimInterval+stimDuration-win.monitorFramePeriod*0.75):
            windowRight.setAutoDraw(False)
            blackBoxRight.setAutoDraw(False)

        # *mask* updates
        if mask.status == NOT_STARTED:
            mask.tStart = t
            mask.frameNStart = frameN
            mask.xys = maskInitPos # setting the initial positions for the mask elements
            mask.fieldPos = [maskOffsetX, windowOffsetY]
            mask.setAutoDraw(True)
            maskMoveClock.reset()
        if mask.status == STARTED and t>0.5:
            if tMaskMove == 0:
                tMaskMove = frameDur # maskMoveClock.getTime()
                tMaskRec = maskMoveClock.getTime()
                maskMovePos = maskInitPos
            else:
                tMaskMove = maskMoveClock.getTime() - tMaskRec
                tMaskRec = maskMoveClock.getTime()
            maskMovePos = np.array(maskMovePos) + np.array(maskDirs) * maskSpeed * tMaskMove
            maskElemsOutside = np.where(abs(maskMovePos)>maxTravDist)
            maskMovePos[maskElemsOutside] = -maxTravDist*maskMovePos[maskElemsOutside]/abs(maskMovePos[maskElemsOutside])
            mask.xys = maskMovePos
        if mask.status == STARTED and t >= (0 + (preStimInterval+stimDuration-win.monitorFramePeriod*0.75)):
            mask.setAutoDraw(False)
        
        # *target* updates
        if t >= preStimInterval and target.status == NOT_STARTED:
            # keep track of start time/frame for later
            target.tStart = t  # underestimates by a little under one frame
            target.frameNStart = frameN  # exact frame index
            target.setAutoDraw(True)
            edgeReached = False
            moveClock.reset()
        if target.status == STARTED:
            curFrameN = frameN - target.frameNStart
            if curFrameN < fadeInNofFrames:
                target.opacity = curFrameN / fadeInNofFrames
            else:
                target.opacity = 1
            tMove = moveClock.getTime()
            if edgeReached: # if the edge is reached, start from the other edge:
                travDist = tMove*targSpeed-maxTravDist
            else: # otherwise, start from the middle of the box:
                travDist = tMove*targSpeed
            # if the target has already moved beyond max allowed travel distance:
            if travDist > maxTravDist:
                edgeReached = True
                moveClock.reset() # reset the movement clock (set it to zero)
                tMove = moveClock.getTime() # get the time
                # use that reset time for new travDist, but start from the edge:
                travDist = tMove*targSpeed-maxTravDist
            # target movement:
            if targDir == 'left':
                target.pos = [targOffsetX-travDist, targOffsetY]
            elif targDir == 'right':
                target.pos = [targOffsetX+travDist, targOffsetY]
        if target.status == STARTED and t >= (preStimInterval + (stimDuration-win.monitorFramePeriod*0.75)):
            target.setAutoDraw(False)
        
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
            theseKeys = event.getKeys(keyList=['up', 'down'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_upDown.keys = theseKeys[-1]  # just the last key pressed
                key_upDown.rt = key_upDown.clock.getTime()
                # was this 'correct'?
                if (key_upDown.keys == str(targCorrAns)) or (key_upDown.keys == targCorrAns):
                    key_upDown.corr = 1
                else:
                    key_upDown.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *ISI* period
        if ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(ISIduration)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
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
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_upDown.keys in ['', [], None]:  # No response was made
       key_upDown.keys=None
       # was no response the correct answer?!
       if str(targCorrAns).lower() == 'none': key_upDown.corr = 1  # correct non-response
       else: key_upDown.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_upDown.keys',key_upDown.keys)
    trials.addData('key_upDown.corr', key_upDown.corr)
    if key_upDown.keys != None:  # we had a response
        trials.addData('key_upDown.rt', key_upDown.rt)
    thisExp.nextEntry()
    
# completed 4 repeats of 'trials'

win.close()
core.quit()
