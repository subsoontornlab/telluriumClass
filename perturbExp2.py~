import numpy
import tellurium as te

rr = te.loada('''
   $Xo -> S1; k1*Xo
   S1  -> $X1; k2*S1;

   Xo = 10; k1 = 0.3; k2 = 0.15;
 ''')
# let the reaction run for 40 time unit
m1 = rr.simulate(0, 40, 50)

# perturb by increasing S1 60%
rr.S1 = rr.S1*1.6

# let the reaction run for additional 40 time unit
m2 = rr.simulate(40, 80, 50)

# merge the result
m = numpy.vstack((m1,m2))

te.plotArray(m)

