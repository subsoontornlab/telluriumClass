import tellurium as te
import pylab as plt

# Example showing how to embellish a graph, change title, axes labels.
# Example also uses an event to pulse S1
r = te.loada ('''
    $Xo -> S1; k1*Xo;
    S1 -> $X1; k2*S1;
    k1 = 0.2; k2 = 0.4; Xo = 1; S1 = 0.5;
    at (time > 20): S1 = S1 + 0.35
 ''')

 # Simulate the first part up to 20 time units



m = r.simulate (0, 50, 100, ["time", "S1"]);
plt.ylim ((0,1))
plt.xlabel ('Time')
plt.ylabel ('Concentration')
plt.title ('My First Plot ($y = x^2$)')
r.plot (m)
