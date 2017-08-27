import tellurium as te

rr = te.loada('''
   $Xo -> S1; k1*Xo
   S1  -> $X1; k2*S1;

   Xo = 10; k1 = 0.3; k2 = 0.15;

   at time > 40: S1 = S1*1.6
 ''')
# let the reaction run for 40 time unit
m = rr.simulate(0, 80, 200)

rr.plot()

