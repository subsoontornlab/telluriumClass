# Simple constitutive gene expression model
import tellurium as te
import numpy as np
import pylab as plt

# set simulation time
timeBegin = 0
timeEnd = 50
timePoint = 100

r = te.loada ('''
     J1: G -> G + X1; a1*G; 
     J2: X1  -> ; b1*X1;
     J3: R1 + G -> R1G; kf_rg*R1*G
     J4: R1G -> G + R1; kr_rg*R1G

     # set parameter     
     X1 = 0; G = 1; a1 = 1; b1 = 1;
     kf_rg = 1; kr_rg = 0.0001;
     R1 = 0; R1G = 0;

     at time > 20: R1 = 2; 

 ''')

###################################
# default simulation
result = r.simulate(timeBegin, timeEnd, timePoint)
print(result)
Time = result[:, 0]
X1 = result[:, 2]
R1 = result[:, 3]
R1G = result[:, 4]
R1tot = R1 + R1G

###################################
## tuned simulation
r.reset()
## try one of the following options
## option-1: production x 2
#r.kr_rg = 1
## option-2: production x 2 and degradation x 2
r.a1 = 10; r.b1 = 10

# running simulation
result_tune = r.simulate(timeBegin, timeEnd, timePoint)
Time_tune = result_tune[:, 0]
X1_tune = result_tune[:, 2]

plt.subplot(211)
plt.plot(Time, X1, color = 'b', label = 'default')    
plt.plot(Time_tune, X1_tune, color = 'r', label = 'tuned')
plt.legend(loc = 'upper right')
plt.ylabel('concentration')


plt.subplot(212)
plt.plot(Time, R1tot, color = 'k', ls = '--', label = 'input')
plt.legend(loc = 'upper right')
plt.xlabel('time')
plt.ylabel('concentration')

#######################
# set axis limit
#plt.ylim(-0.1, 1.5)
#plt.xlim(-0.1, 10)




#plt.title('k1 scan')
plt.show()
