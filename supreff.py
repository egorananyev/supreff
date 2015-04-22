#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.00), Mon Mar 16 14:30:23 2015
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, sound, gui #,logging
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
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
expName = 'supreff'  # from the Builder filename that created this script
expInfo = {u'session': u'02', u'domEye': u'r', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName) # dialogue box
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
#filename = _thisDir + os.sep + 'data' + os.sep + '%s_%s_%s_%s_%s' %(expName, 
filename = '..' + os.sep + 'data' + os.sep + '%s_%s_%s_%s_%s' %(expName, 
    expInfo['participant'], expInfo['domEye'], expInfo['session'], expInfo['date'])

# ====================================================================================
## Initial variables.
# Window boxes and black boxes (specified in degrees of visual angles [dva]):
windowSize = 5.03 # 4.47
windowOffsetX = 5.62 # 6.71
windowOffsetY = 2.83 # 4.97
windowThickness = 2
targVertOffset = 1.5
blackBoxSize = windowSize + 0.5
blackBoxThickness = 10
# Mask variables:
nMaskElements = 240 # must be divisible by the number of directions allowed (below)
maskDirections = [[1,0],[-1,0],[0,1],[0,-1]] # right, left, up, down
# Timing variables (in seconds) and trial number:
preStimInterval = 1
stimDuration = 2 # 3.6s in the Moors paper
ISIduration = 0.0 # 0.5 before
fadeInNofFrames = 20 # the number of frames for the fade-in
# Criteria for contrast staircases:
if expInfo['session']=='01': #expt.1a
    conditionsFileName = 'cond-expt01.csv'
    nTrialsPerStair = 30
elif expInfo['session']=='02': #expt.1b
    conditionsFileName = 'cond-expt02.csv'
    nTrialsPerStair = 48
print nTrialsPerStair
contrMin = 0
contrMax = 1
# Other variables:
contrSteps = [.3,.3,.2,.2,.2,.2,.1,.1,.1,.1,.05,.05,.05,.05,.03,.03,.03,.03,.02,.02]
targInitPosAll = [-1, 0, 1] # multiplier for starting target position along x-axis
# TEMP:
nTrialsPerStair = 12
conditionsFileName = 'cond-expt02-partial.csv'
contrSteps = [.3,.3,.2,.2,.1,.1,.05,.05,.03,.03,.02,.02]
# ====================================================================================

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='', extraInfo=expInfo, 
    runtimeInfo=None, originPath=None, savePickle=True, saveWideText=True, 
    dataFileName=filename)
##save a log file for detail verbose info
#logFile = logging.LogFile(filename+'.log', level=logging.EXP)
#logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

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
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instrText = visual.TextStim(win=win, ori=0, name='instrText',
    text='Indicate whether the red circle appeared above or below fixation:\n\n"up" = above\n"down" = below \n\n The frames will turn *yellow* when the target disappeared.',
    font='Cambria', pos=[0, 0], height=1, wrapWidth=10, color='white', \
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
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
# setting the edges to 3 (triangle) initially: this will change once ...
# ... the attributes are read from the configuration file:
target = visual.Polygon(win=win, name='target',units='deg', edges = 3, size=[0.1, 0.1],
    ori=0, pos=[0, 0], lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb', opacity=1, interpolate=True)
# field size needs to be changed later on in the code:
mask = visual.ElementArrayStim(win=win, name='mask', units='deg', 
    fieldSize=(windowSize,windowSize), fieldShape='sqr', colors=(1,1,1), 
    colorSpace='rgb', opacities=1, fieldPos=[0,0], sizes=1, nElements=nMaskElements, 
    elementMask=None, elementTex=None, sfs=3, xys=maskInitPos, interpolate=True)
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
stairConds = data.importConditions(conditionsFileName)
# print stairConds
nConditions = np.size(stairConds)
print "number of conditions: " + str(nConditions)

# ====================================================================================
## Preparing the mask and the target.
# Target starting position (assuming that the target is always presented to the non-dominant eye):
if expInfo['domEye'] == 'r': # if the dominant eye is right...
    targOffsetX = -windowOffsetX
    maskOffsetX = windowOffsetX
elif expInfo['domEye'] == 'l': # if the dominant eye is left...
    targOffsetX = windowOffsetX
    maskOffsetX = -windowOffsetX

# The target directions and starting positions must be random. Revised handling of 
#   randomization for trials. The values in each randCondCombi vector are: targDir, 
#   targInitPos, and targLoc. Note that targInitPos is NOT YET multiplied by the max
#   travel distance. randCondCombi yields a vector of conditions for twelve trials:
if expInfo['session']=='01': #expt.1a
    randCondCombi = list(itertools.product(*[[-1,1],[-.5,0,.5]]))
elif expInfo['session']=='02': #expt.1b
    randCondCombi = list(itertools.product(*[[-1,1],[-.5,0,.5],[-1,1]]))
nCombiReps = nTrialsPerStair / np.shape(randCondCombi)[0]
print 'random condition combination vector: ' + str(randCondCombi)
print 'number of repeats (blocks) for the vector: ' + str(nCombiReps)

# Setting up each staircase, one by one:
stairs=[] # setting up a variable containing all our staircases
for thisCondition in stairConds:
    # I want to record the sequence of the combinations, but not sure if it's a good
    #  idea, since I don't know how it's going to handle the output. I can do the
    #  conversion prior to the output, I guess.
    thisCombi_dirXpos = np.random.permutation(np.repeat(randCondCombi, nCombiReps, 0))
    thisCondition['randCondCombi'] = thisCombi_dirXpos
    thisStair = data.StairHandler(startVal = thisCondition['startVal'],
        extraInfo = thisCondition, nTrials=nTrialsPerStair, nUp=1, nDown=2,
        minVal = contrMin, maxVal = contrMax, stepSizes = contrSteps, stepType='lin')
    thisStair.setExp(thisExp)
    stairs.append(thisStair)
    stairFilename = filename + os.sep + '%s_%s_%s_%s_%s' %(expName, \
        expInfo['participant'], expInfo['domEye'], expInfo['session'], \
        expInfo['date'] + '_cond_' + thisStair.extraInfo['label']) #str(condN))
    print stairFilename
    thisStair.saveAsPickle(stairFilename)
    thisStair.saveAsText(stairFilename)
# Printing the attributes of the stairs:  
print dir(stairs[0])
# Creating a directory for storing staircase outputs:
if not os.path.exists(filename):
    os.makedirs(filename)
# Creating a copy of the Conditions file for book-keeping and analyses:
shutil.copyfile(conditionsFileName, filename + os.sep + conditionsFileName)

# Annoyingly, the right side of the following appears everywhere. More efficient to
#   store this as a variable since it is fixed:
stimOffset = (preStimInterval + (stimDuration-win.monitorFramePeriod*0.75))
# ====================================================================================

for trialN in range(nTrialsPerStair):
    shuffle(stairs) # randomizing the appearance of the stairs for each trial
    for thisStair in stairs:
        # Based on the current staircase, assigning the current contrast value and
        #  other variables:
        thisIntensity = thisStair.next() # contrast value
        thisTargDir = thisStair.extraInfo['randCondCombi'][trialN,0]
        thisTargSize = thisStair.extraInfo['targSize']
        if expInfo['session']=='01': #expt.1a
            thisTargLoc = thisStair.extraInfo['targLoc']
            thisTargCorrAns = thisStair.extraInfo['targCorrAns']
        elif expInfo['session']=='02': #expt.1b
            thisTargLoc = thisStair.extraInfo['randCondCombi'][trialN,2]
            if thisTargLoc==1: thisTargCorrAns='up'
            elif thisTargLoc==-1: thisTargCorrAns='down'
        thisTargVertices = thisStair.extraInfo['targVertices']
        thisTargSpeed = thisStair.extraInfo['targSpeed']
        thisTargColour = thisStair.extraInfo['targColour']
        thisMaskVertices = thisStair.extraInfo['maskVertices']
        thisMaskSize = thisStair.extraInfo['maskSize']
        thisMaskSpeed = thisStair.extraInfo['maskSpeed']
        thisMaskColRed = thisStair.extraInfo['maskColRed']
        thisMaskColGreen = thisStair.extraInfo['maskColGreen']
        thisMaskColYellow = thisStair.extraInfo['maskColYellow']
        thisMaskColBlue = thisStair.extraInfo['maskColBlue']
        thisMaskColGrey = thisStair.extraInfo['maskColGrey']
        # What changes from trial to trial (will be different for dif expts)?
        print '### Trial ' + str(trialN) + ' ###'
        print 'thisIntensity (contrast): start=%.2f, current=%.3f' \
            %(thisStair.extraInfo['startVal'], thisIntensity)
        print 'thisTargLoc: ' + str(thisTargLoc)
        print 'thisMaskSpeed: ' + str(thisMaskSpeed)
        print 'thisTargDir: ' + str(thisTargDir)
        #print 'thisCondition: ' + str(thisCondition)
        # Setting up the size specifications:
        target.size = [thisTargSize, thisTargSize] # target size
        mask.sizes = [thisMaskSize, thisMaskSize] # mask size
        # Maximum travel distance from the initial position:
        maxTravDist = (windowSize - thisTargSize/1) / 2
        # Based on the above max travel distance, setting the initial target position,
        #   thereby finishing condition setup for the trial:
        thisTargInitPos = thisStair.extraInfo['randCondCombi'][trialN,1]*maxTravDist
        print 'thisTargInitPos: ' + str(thisTargInitPos)
        # Resetting the starting positions of mask elements - 
        #  (assuming that the mask is different for every trial):
        maskInitPos = (np.random.rand(nMaskElements,2)*2-1)*maxTravDist

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
        maskColAll = np.array([[1,-1,-1], [-1,-1,1], [-1,1,-1], [1,1,-1]])
        maskColCurSet = maskColAll[maskColIDs==1]
        maskColNumReps = nMaskElements/np.shape(maskColCurSet)[0]
        maskColCurSetRepd = np.repeat(maskColCurSet, maskColNumReps, 0)
        maskColours = np.random.permutation(maskColCurSetRepd)
        mask.colors = maskColours
        
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        tMaskMove = 0
        key_pressed = False
        key_pause = False
        windowLeft.lineColor = 'white'
        windowRight.lineColor = 'white'
        # Vertical offset of the target (dependent on the type of trial):
        if expInfo['session']=='01': #expt.1a
            if thisTargLoc == 'above':
                targOffsetY = windowOffsetY + targVertOffset
            elif thisTargLoc == 'below':
                targOffsetY = windowOffsetY - targVertOffset
            else:
                print 'Error! Please check your target location values.'
        elif expInfo['session']=='02': #expt.1b
            targOffsetY = windowOffsetY + thisTargLoc*targVertOffset
        # update component parameters for each repeat
        target.edges = thisTargVertices # updating the shape of the target
        target.setFillColor(thisTargColour)
        target.setLineColor(thisTargColour)
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
#            if windowLeft.status == STARTED and t >= stimOffset:
#                windowLeft.setAutoDraw(False)
#                fixationLeft.setAutoDraw(False)
#                blackBoxLeft.setAutoDraw(False)
            
            # *windowRight* updates
            if windowRight.status == NOT_STARTED:
                # keep track of start time/frame for later
                windowRight.tStart = t  # underestimates by a little under one frame
                windowRight.frameNStart = frameN  # exact frame index
                windowRight.setAutoDraw(True)
                fixationRight.setAutoDraw(True)
                blackBoxRight.setAutoDraw(True)
#            if windowRight.status == STARTED: #and t >= stimOffset:
#                windowRight.setAutoDraw(False)
#                fixationRight.setAutoDraw(False)
#                blackBoxRight.setAutoDraw(False)

            # if the target has already disappeared, yet the key is still not pressed\
            #   continue, the trial with the yellow boxes:
            if ~key_pressed and t > stimOffset:
                windowLeft.lineColor = 'yellow'
                windowRight.lineColor = 'yellow'

            # pause text (after the response is made):
            if key_pressed and ~key_pause and t > stimOffset:
                pauseTextLeft.setAutoDraw(True)
                pauseTextRight.setAutoDraw(True)
                windowLeft.lineColor = 'white'
                windowRight.lineColor = 'white'

            # *mask* updates
            if mask.status == NOT_STARTED and t > preStimInterval:
                mask.tStart = t
                mask.frameNStart = frameN
                # setting the initial positions for the mask elements
                mask.xys = maskInitPos 
                mask.fieldPos = [maskOffsetX, windowOffsetY]
                mask.setAutoDraw(True)
                maskMoveClock.reset()
            if mask.status == STARTED and t > preStimInterval and ~key_pressed:
                if tMaskMove == 0:
                    tMaskMove = frameDur # maskMoveClock.getTime()
                    tMaskRec = maskMoveClock.getTime()
                    maskMovePos = maskInitPos
                else:
                    tMaskMove = maskMoveClock.getTime() - tMaskRec
                    tMaskRec = maskMoveClock.getTime()
                maskMovePos = np.array(maskMovePos) + np.array(maskDirs) * \
                    thisMaskSpeed * tMaskMove
                maskElemsOutside = np.where(abs(maskMovePos)>maxTravDist)
                maskMovePos[maskElemsOutside] = -maxTravDist * \
                    maskMovePos[maskElemsOutside] / abs(maskMovePos[maskElemsOutside])
                mask.xys = maskMovePos
            if mask.status == STARTED and t >= stimOffset and key_pressed:
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
                if curFrameN < fadeInNofFrames:
                    target.opacity = thisIntensity * (curFrameN / fadeInNofFrames)
                else:
                    target.opacity = thisIntensity
                tMove = moveClock.getTime()
                if edgeReached: # if the edge is reached, start from the other edge:
                    travDist = tMove*thisTargSpeed-maxTravDist
                else: # otherwise, start from the initial target position:
                    # note that this is only for the first cycle!
                    travDist = tMove*thisTargSpeed+thisTargInitPos
                # if the target has already moved beyond max allowed travel distance:
                if travDist > maxTravDist:
                    edgeReached = True
                    moveClock.reset() # reset the movement clock (set it to zero)
                    tMove = moveClock.getTime() # get the time
                    # use that reset time for new travDist, but start from the edge:
                    travDist = tMove*thisTargSpeed-maxTravDist
                # target movement:
                target.pos = [targOffsetX+thisTargDir*travDist, \
                    targOffsetY]
            if target.status == STARTED and t >= stimOffset:
                target.setAutoDraw(False)

            # *key_space* updates
            if ~key_pause and key_pressed and t >= stimOffset:
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
                theseKeys = event.getKeys(keyList=['up', 'down'])
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_upDown.keys = theseKeys[-1]  # just the last key pressed
                    key_upDown.rt = key_upDown.clock.getTime()
                    key_pressed = True
                    # was this 'correct'?
                    if (key_upDown.keys == str(thisTargCorrAns)) or \
                            (key_upDown.keys == thisTargCorrAns):
                        print 'correct response'
                        key_upDown.corr = 1
                    else:
                        print 'incorrect response'
                        key_upDown.corr = 0
#                    ########
#                    # Printing for debug:
#                    print 'RT: %.3f' %(key_upDown.rt)
#                    print thisStair.data

            # if key is not pressed, do nothing
            # if key is pressed, wait for the presentation time to pass to terminate\
            #   the trial:
            if key_pressed and key_pause and t >= stimOffset:
                # update staircase with the last response:
                thisStair.addData(key_upDown.corr)
                thisStair.addOtherData('key_upDown.rt', key_upDown.rt)
                # a response ends the routine
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
            else:  # this Routine was not non-slip safe so reset non-slip timer
                stairFilename = filename + os.sep + '%s_%s_%s_%s_%s' %(expName, \
                    expInfo['participant'], expInfo['domEye'], expInfo['session'], \
                    expInfo['date'] + '_cond_' + thisStair.extraInfo['label'])
                thisStair.saveAsPickle(stairFilename)
                routineTimer.reset()
        
        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        thisExp.nextEntry()
    
# Writing the separate outputs for the staircases:
#dateStr = time.strtime("%b_%d_%H%M", time.localtime())
#condN = 0 # the conditions are simply defined by their numbers
for thisStair in stairs:
#    condN += 1
    print 'reversals:'
    print thisStair.reversalIntensities
    print 'mean of final 6 reversals = %.3f' \
        %(np.average(thisStair.reversalIntensities[-6:]))
    stairFilename = filename + os.sep + '%s_%s_%s_%s_%s' %(expName, \
        expInfo['participant'], expInfo['domEye'], expInfo['session'], \
        expInfo['date'] + '_cond_' + thisStair.extraInfo['label']) #str(condN))
    thisStair.saveAsPickle(stairFilename)
    thisStair.saveAsText(stairFilename)

win.close()
core.quit()
