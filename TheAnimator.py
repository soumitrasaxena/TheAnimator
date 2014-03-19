import maya.cmds as cmds

class WalkCycle:
	def __init__(self , *pArgs):
		self.startTime = 1
		self.endTime = 25
		self.height = -0.165
		self.currentSelection()
		
	def currentSelection(self , *pArgs):
		self.selection = cmds.ls(selection = True)
		
	
	def getSelection(self , *pArgs):
		self.selection = cmds.ls(selection = True)
				
		if len(self.selection) == 0 :
			return 'Select something'
		else:	
			return self.selection[0]
	
	def setCheck(self , value):
		self.check = value
			
	
	def setEndTime(self ,endTimeField,  *pArgs):
		self.endTime = cmds.intField(endTimeField , query = True , value = True)
			
	def getEndTime(self):
		return self.endTime
	
	def setHeight(self , value):
		self.height = value
		
	def animate(self, *pArgs):		
		if self.check == 1:
			print 'Animate left ankle'
			self.animateLeftAnkle()
		if self.check == 2:
			print 'Animate right ankle'
			self.animateRightAnkle()
		if self.check == 3:
			print 'Animate left wrist'
			self.animateLeftWrist()
		if self.check == 4:
			print 'Animate right wrist'
			self.animateRightWrist()
		if self.check == 5:
			print 'Animate body Height control'
			self.animateHeightControl()	
		
		
	def animateLeftAnkle(self):
		self.currentSelection()
		
		bodyControl = self.selection[0]
		
		#Keyraming Y translation
		cmds.cutKey(bodyControl ,  attribute= 'translateY')		
		cmds.setKeyframe(bodyControl , time = self.startTime , attribute = 'translateY' , value = 0)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.16) , attribute = 'translateY' , value = -0.025)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.4) , attribute = 'translateY' , value = -0.17)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.52) , attribute = 'translateY' , value = 0.448)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.64) , attribute = 'translateY' , value = 0.49)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.76) , attribute = 'translateY' , value = 0.545)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*1) , attribute = 'translateY' , value = 0)		
		cmds.selectKey(bodyControl , time = (self.startTime , self.endTime) , attribute = 'translateY')
		cmds.keyTangent( inTangentType = "linear" , outTangentType = "linear")   
    
		#Keyraming Z translation
		cmds.cutKey(bodyControl , attribute= 'translateZ')		
		cmds.setKeyframe(bodyControl , time = self.startTime , attribute = 'translateZ' , value = 1.334)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.16) , attribute = 'translateZ' , value = 0.803)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.4) , attribute = 'translateZ' , value = -1.346)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.52) , attribute = 'translateZ' , value = -1.572)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.64) , attribute = 'translateZ' , value = -0.727)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.76) , attribute = 'translateZ' , value = -0.22)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*1) , attribute = 'translateZ' , value = 1.334)		
		cmds.selectKey(bodyControl , time = (self.startTime , self.endTime) , attribute = 'translateZ')
		cmds.keyTangent( inTangentType = "linear" , outTangentType = "linear")   
		
		#Keyraming X Rotation
		cmds.cutKey(bodyControl ,  attribute= 'rotateX')		
		cmds.setKeyframe(bodyControl , time = self.startTime , attribute = 'rotateX' , value = -46.373)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.16) , attribute = 'rotateX' , value = 0)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.4) , attribute = 'rotateX' , value = 11.462)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.52) , attribute = 'rotateX' , value = 28.861)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.64) , attribute = 'rotateX' , value = 35.62)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.76) , attribute = 'rotateX' , value = 14.361)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*1) , attribute = 'rotateX' , value = -46.373)		
		cmds.selectKey(bodyControl , time = (self.startTime , self.endTime) , attribute = 'rotateX')
		cmds.keyTangent( inTangentType = "linear" , outTangentType = "linear")  
	
	def animateRightAnkle(self):
		
		self.currentSelection()
		
		bodyControl = self.selection[0]
		
		#Keyraming Y translation
		cmds.cutKey(bodyControl ,  attribute= 'translateY')		
		cmds.setKeyframe(bodyControl , time = self.startTime , attribute = 'translateY' , value = 0.525)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.16) , attribute = 'translateY' , value = 0.729)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.4) , attribute = 'translateY' , value = 0.225)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.52) , attribute = 'translateY' , value = 0)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.64) , attribute = 'translateY' , value = -0.044)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.76) , attribute = 'translateY' , value = -0.073)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*1) , attribute = 'translateY' , value = 0.525)		
		cmds.selectKey(bodyControl , time = (self.startTime , self.endTime) , attribute = 'translateY')
		cmds.keyTangent( inTangentType = "linear" , outTangentType = "linear")   
    
		#Keyraming Z translation
		cmds.cutKey(bodyControl ,  attribute= 'translateZ')		
		cmds.setKeyframe(bodyControl , time = self.startTime , attribute = 'translateZ' , value = -1.703)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.16) , attribute = 'translateZ' , value = -0.431)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.4) , attribute = 'translateZ' , value = 1.272)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.52) , attribute = 'translateZ' , value = 1.334)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.64) , attribute = 'translateZ' , value = 0.859)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.76) , attribute = 'translateZ' , value = -0.142)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*1) , attribute = 'translateZ' , value = -1.681)		
		cmds.selectKey(bodyControl , time = (self.startTime , self.endTime) , attribute = 'translateZ')
		cmds.keyTangent( inTangentType = "linear" , outTangentType = "linear")   
		
		#Keyraming X Rotation
		cmds.cutKey(bodyControl ,attribute= 'rotateX')		
		cmds.setKeyframe(bodyControl , time = self.startTime , attribute = 'rotateX' , value = 38.644)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.16) , attribute = 'rotateX' , value = 50.636)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.4) , attribute = 'rotateX' , value = -21.223)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.52) , attribute = 'rotateX' , value = -46.373)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.64) , attribute = 'rotateX' , value = 0)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.76) , attribute = 'rotateX' , value = 0)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*1) , attribute = 'rotateX' , value = 38.644)		
		cmds.selectKey(bodyControl , time = (self.startTime , self.endTime) , attribute = 'rotateX')
		cmds.keyTangent( inTangentType = "linear" , outTangentType = "linear")  
    
   	def animateHeightControl(self):
		
		self.currentSelection()
		
		bodyControl = self.selection[0]
	 	
	 	#Keyraming Y translation
		cmds.cutKey(bodyControl , attribute= 'translateY')		
		cmds.setKeyframe(bodyControl , time = self.startTime , attribute = 'translateY' , value = self.height)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.16) , attribute = 'translateY' , value = self.height*2)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.4) , attribute = 'translateY' , value = -1*self.height/2)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.52) , attribute = 'translateY' , value = self.height)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.64) , attribute = 'translateY' , value = self.height*2)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.76) , attribute = 'translateY' , value = self.height/2)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*1) , attribute = 'translateY' , value = self.height)		
		cmds.selectKey(bodyControl , time = (self.startTime , self.endTime) , attribute = 'translateY')
		cmds.keyTangent( inTangentType = "linear" , outTangentType = "linear")   
    
	def animateRightWrist(self):
		
		self.currentSelection()
		
		bodyControl = self.selection[0]
		
		#Keyraming X translation
		cmds.cutKey(bodyControl ,  attribute= 'translateX')		
		cmds.setKeyframe(bodyControl , time = self.startTime , attribute = 'translateX' , value = -2)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.52) , attribute = 'translateX' , value = -2)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*1) , attribute = 'translateX' , value = -2)		
		cmds.selectKey(bodyControl , time = (self.startTime , self.endTime) , attribute = 'translateY')
		cmds.keyTangent( inTangentType = "linear" , outTangentType = "linear")   
    
    	#Keyraming Y translation
		cmds.cutKey(bodyControl ,  attribute= 'translateY')		
		cmds.setKeyframe(bodyControl , time = self.startTime , attribute = 'translateY' , value = -3.692)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.52) , attribute = 'translateY' , value = -3.692)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*1) , attribute = 'translateY' , value = -3.692)		
		cmds.selectKey(bodyControl , time = (self.startTime , self.endTime) , attribute = 'translateY')
		cmds.keyTangent( inTangentType = "linear" , outTangentType = "linear")   
    
    	#Keyraming Z translation
		cmds.cutKey(bodyControl ,  attribute= 'translateZ')		
		cmds.setKeyframe(bodyControl , time = self.startTime , attribute = 'translateZ' , value = -1.328)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.52) , attribute = 'translateZ' , value = 0.766)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*1) , attribute = 'translateZ' , value = -1.328)		
		cmds.selectKey(bodyControl , time = (self.startTime , self.endTime) , attribute = 'translateZ')
		cmds.keyTangent( inTangentType = "linear" , outTangentType = "linear")   
		
		#Deleting any keyframes of rotateX
		cmds.cutKey(bodyControl ,  attribute= 'rotateX')	
		
		#Keyraming Y rotation
		cmds.cutKey(bodyControl ,  attribute= 'rotateY')		
		cmds.setKeyframe(bodyControl , time = self.startTime , attribute = 'rotateY' , value = 39.6)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.52) , attribute = 'rotateY' , value = 0)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*1) , attribute = 'rotateY' , value = 39.6)		
		cmds.selectKey(bodyControl , time = (self.startTime , self.endTime) , attribute = 'rotateY')
		cmds.keyTangent( inTangentType = "linear" , outTangentType = "linear")   
     
     	#Keyraming Z rotation
		cmds.cutKey(bodyControl ,  attribute= 'rotateZ')		
		cmds.setKeyframe(bodyControl , time = self.startTime , attribute = 'rotateZ' , value = -105.923)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.52) , attribute = 'rotateZ' , value = 0)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*1) , attribute = 'rotateZ' , value = -105.923)		
		cmds.selectKey(bodyControl , time = (self.startTime , self.endTime) , attribute = 'rotateZ')
		cmds.keyTangent( inTangentType = "linear" , outTangentType = "linear")   
        
	def animateLeftWrist(self):
		
		self.currentSelection()
		
		bodyControl = self.selection[0]
		
		#Keyraming X translation
		cmds.cutKey(bodyControl ,  attribute= 'translateX')		
		cmds.setKeyframe(bodyControl , time = self.startTime , attribute = 'translateX' , value = -2)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.52) , attribute = 'translateX' , value = -2)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*1) , attribute = 'translateX' , value = -2)		
		cmds.selectKey(bodyControl , time = (self.startTime , self.endTime) , attribute = 'translateY')
		cmds.keyTangent( inTangentType = "linear" , outTangentType = "linear")   
    
    	#Keyraming Y translation
		cmds.cutKey(bodyControl ,  attribute= 'translateY')		
		cmds.setKeyframe(bodyControl , time = self.startTime , attribute = 'translateY' , value = -3.695)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.52) , attribute = 'translateY' , value = -3.695)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*1) , attribute = 'translateY' , value = -3.695)		
		cmds.selectKey(bodyControl , time = (self.startTime , self.endTime) , attribute = 'translateY')
		cmds.keyTangent( inTangentType = "linear" , outTangentType = "linear")   
    
    	#Keyraming Z translation
		cmds.cutKey(bodyControl ,  attribute= 'translateZ')		
		cmds.setKeyframe(bodyControl , time = self.startTime , attribute = 'translateZ' , value = -0.651)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.52) , attribute = 'translateZ' , value = 1.259)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*1) , attribute = 'translateZ' , value = -0.651)		
		cmds.selectKey(bodyControl , time = (self.startTime , self.endTime) , attribute = 'translateZ')
		cmds.keyTangent( inTangentType = "linear" , outTangentType = "linear")   
		
		#Deleting any keyframes of rotateX
		cmds.cutKey(bodyControl ,  attribute= 'rotateX')	
		
		#Keyraming Y rotation
		cmds.cutKey(bodyControl ,  attribute= 'rotateY')		
		cmds.setKeyframe(bodyControl , time = self.startTime , attribute = 'rotateY' , value = 16.745)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.52) , attribute = 'rotateY' , value = -40.855)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*1) , attribute = 'rotateY' , value = 16.745)		
		cmds.selectKey(bodyControl , time = (self.startTime , self.endTime) , attribute = 'rotateY')
		cmds.keyTangent( inTangentType = "linear" , outTangentType = "linear")   
     
     #Keyraming Z rotation
		cmds.cutKey(bodyControl ,  attribute= 'rotateZ')		
		cmds.setKeyframe(bodyControl , time = self.startTime , attribute = 'rotateZ' , value = -75.98)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*0.52) , attribute = 'rotateZ' , value = 0)
		cmds.setKeyframe(bodyControl, time = int((self.endTime-self.startTime+1)*1) , attribute = 'rotateZ' , value = -75.98)		
		cmds.selectKey(bodyControl , time = (self.startTime , self.endTime) , attribute = 'rotateZ')
		cmds.keyTangent( inTangentType = "linear" , outTangentType = "linear")   
        
def displaySelected(walk , selectedField):
	selection = walk.getSelection()
	cmds.textField( selectedField , edit = True , text = selection )
		
def printV(value):
	print value


def createUI( pWindowTitle , walk):
	
	windowID = 'myWindowID'
	
	if cmds.window(windowID , exists = True):
		cmds.deleteUI(windowID)
		
	cmds.window(windowID , title = pWindowTitle , sizeable = False , resizeToFitChildren = True)
	
	cmds.rowColumnLayout( numberOfColumns = 3 , columnWidth =[(1,200) , (2,200) , (3,200)])
	
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
	
	cmds.separator ( h = 20 , style = 'none')
	cmds.text( label = 'Select the corresponding control')
	cmds.separator ( h = 20 , style = 'none')	
	
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
	cmds.separator ( h = 30 , style = 'none')
		
	cmds.radioCollection()
	cmds.radioButton(label = 'Left Ankle Control' , onCommand = lambda x : walk.setCheck(1))
	cmds.radioButton(label = 'Right Ankle Control' , onCommand = lambda x : walk.setCheck(2))
	cmds.radioButton(label = 'Left Wrist Control' , onCommand = lambda x : walk.setCheck(3))
	cmds.radioButton(label = 'Right Wrist Control' , onCommand = lambda x : walk.setCheck(4))
	cmds.radioButton(label = 'Control to change body height' , onCommand = lambda x : walk.setCheck(5))
	cmds.separator ( h = 10 , style = 'none')
	
	
	cmds.separator ( h = 30 , style = 'doubleDash')
	cmds.separator ( h = 30 , style = 'doubleDash')
	cmds.separator ( h = 30 , style = 'doubleDash')
	
	cmds.text( label = 'Set End Frame ( Pace )')
	endTimeField = cmds.intField(value = 25)
	cmds.button(label = 'Apply Pace' , command = lambda x : walk.setEndTime(endTimeField))
	
	cmds.separator ( h = 20 , style = 'none')
	cmds.separator ( h = 20 , style = 'none')
	cmds.separator ( h = 20 , style = 'none')
	
	cmds.text( label = 'Set walk height')
	cmds.floatSlider(min = -0.165 , max = -0.001 , value = -0.165 , step = 0.001 , w = 100 , dragCommand = lambda w : walk.setHeight(w))
	cmds.separator ( h = 10 , style = 'none')
	
	cmds.separator ( h = 30 , style = 'doubleDash')
	cmds.separator ( h = 30 , style = 'doubleDash')
	cmds.separator ( h = 30 , style = 'doubleDash')
		
	cmds.button(label = 'Animate' , command = walk.animate)
	cmds.separator ( h = 10 , style = 'none')
	cmds.button(label = 'Reset to Default' , command = walk.__init__)
	
	cmds.separator ( h = 30 , style = 'doubleDash')
	cmds.separator ( h = 30 , style = 'doubleDash')
	cmds.separator ( h = 30 , style = 'doubleDash')
	
	cmds.separator ( h = 30 , style = 'none')
	selectedField = cmds.textField( text = 'Nothing Selected' )
	cmds.separator ( h = 30 , style = 'none')
	
	cmds.separator ( h = 10 , style = 'none')
	cmds.button(label = 'Current Selection' , command = lambda x : displaySelected(walk , selectedField))
	cmds.separator ( h = 10 , style = 'none')
	
	cmds.separator ( h = 30 , style = 'doubleDash')
	cmds.separator ( h = 30 , style = 'doubleDash')
	cmds.separator ( h = 30 , style = 'doubleDash')
	
	
	
	
	cmds.showWindow()


		
walk = WalkCycle()
createUI('The Animator' , walk)