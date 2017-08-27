# Parameter Scan
 # This code will run five simulations, each simulation
 # having a different values for a rate constant
import tellurium as te
import numpy as np
import pylab as plt
r = te.loada ('''
     J1: $X0 -> S1; k1*X0;
     J2: S1 -> $X1; k2*S1;
     X0 = 1.0; S1 = 0.0; X1 = 0.0;
     k1 = 0.4; k2 = 2.3;
 ''')

## somehow setHold doesn't work
#te.setHold (True)

mm = -np.ones((100,2,5))
ind = 0
for r.k1 in np.linspace (0.4, 5, 5):
    r.reset() # reset all concentrations back to the beginning
    m = r.simulate (0, 4, 100, ["Time", "S1"])
    timePts = m[:, 0]
    S1Pts = m[:, 1]
    #np.concatenate([mm, m], axis = 1)
    print(m.shape)
    mm[:,:,ind ] = m
    #te.plotArray (m, label='k1 = ' + str (r.k1))
    plt.plot(timePts, S1Pts, label = str(r.k1))
    ind += 1
#pylab.legend()
#te.setHold (False)
print(mm)
plt.ylim(-0.1, 2.5)
plt.xlim(-0.1, 4.5)
plt.legend(loc = 'upper right')
plt.xlabel('time')
plt.ylabel('concentration')
plt.title('k1 scan')
plt.show()
