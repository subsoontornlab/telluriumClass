# Simple constitutive gene expression model
import tellurium as te
import numpy as np
import pylab as plt

# set simulation time
timeBegin = 0
timeEnd = 10
timePoint = 100

r = te.loada ('''
     J1: $G -> $G + X1; a1*G; 
     J2: X1  -> ; b1*X1;
     # set parameter     
     X1 = 0; G = 1; a1 = 1; b1 = 1;
 ''')

###################################
# default simulation
result = r.simulate(timeBegin, timeEnd, timePoint)
Time = result[:, 0]
X1 = result[:, 1]

###################################
## tuned simulation
r.reset()
## try one of the following three options
## option-1: production x 2
r.a1 = 2
# option-2: degradation x 0.5
#r.b1 = 0.5
## option-1: production x 2 and degradation x 2
r.a1 = 2; r.b1 = 2

# running simulation
result_tune = r.simulate(timeBegin, timeEnd, timePoint)
Time_tune = result_tune[:, 0]
X1_tune = result_tune[:, 1]


plt.plot(Time, X1, color = 'b', label = 'default')
plt.plot(Time_tune, X1_tune, color = 'r', label = 'tuned')


#######################
# set axis limit
#plt.ylim(-0.1, 1.5)
#plt.xlim(-0.1, 10)


plt.legend(loc = 'upper right')
plt.xlabel('time')
plt.ylabel('concentration')
#plt.title('k1 scan')
plt.show()
