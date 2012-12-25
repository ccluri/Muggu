import numpy as np
import pylab as pl

class Pendulum():
    '''Here is a pendulum under zero gravity, The idea is to attach multiple pendulums to each others end to obtain spirograph like figures.'''
    def __init__(self,pivot_x,pivot_y,length):
        self.pivot_x = pivot_x
        self.pivot_y = pivot_y
        self.length = length
        self.current_x = pivot_x + length
        self.current_y = 0.0

    def getCurrent(self):
        return self.current_x,self.current_y

    def updatePivot(self,pivot_x,pivot_y):
        self.pivot_x = pivot_x
        self.pivot_y = pivot_y
        
    def stepAngle(self,angle=0.1):
        temp_x = (self.current_x - self.pivot_x)*np.cos(angle) - \
                 (self.current_y - self.pivot_y)*np.sin(angle) + \
                 self.pivot_x
        temp_y = (self.current_x - self.pivot_x)*np.sin(angle) + \
                 (self.current_y - self.pivot_y)*np.cos(angle) + \
                 self.pivot_y
        self.current_x = temp_x
        self.current_y = temp_y
        return self.current_x,self.current_y

if __name__ == '__main__':
    iterations = 50
    stepAngle = 0.01

    posValues_x1 = np.zeros([iterations])
    posValues_y1 = np.zeros([iterations])

    posValues_x2 = np.zeros([iterations])
    posValues_y2 = np.zeros([iterations])

    pend1 = Pendulum(0.0,0.0,0.5) # having a single Pendulum works just fine, attaching another spirals out the second one blizzardly
    pend1_x,pend1_y = pend1.getCurrent()
    pend2 = Pendulum(pend1_x,pend1_y,0.3)
    
    for ii in range(iterations):
        posValues_x1[ii],posValues_y1[ii] = pend1.stepAngle()
        pend2.updatePivot(posValues_x1[ii],posValues_y1[ii])
        posValues_x2[ii],posValues_y2[ii] = pend2.stepAngle()

    pl.figure(figsize=[10,10])
    pl.subplot(1,1,1)
    pl.plot(posValues_x1,posValues_y1)
    pl.hold(True)
    pl.plot(posValues_x2,posValues_y2)
    pl.show()
