import tellurium as te
import matplotlib.pylab as plt

# Single gene expressing protein and protein undergoing degradation
r = te.loada ('''
      # Reactions: 
      J1: G  -> G + P; A
      J2: P ->  ; B*P 

      # Species initializations: 
      P = 0;  G = 1;  A = 1; B = 1;  
      K = 1; n = 2; 
''')

result = r.simulate(0, 10, 50, ['Time', 'P'])
#result = r.simulate(0, 10, 50)

r.plot (result)

