import tellurium as te
import matplotlib.pylab as plt

# injecting sign wave into the model
r = te.loada ('''
      # Reactions: 
      amplitude = 2
      Xo := amplitude*sin(time) + 1

      $Xo -> S; k1*Xo
      S -> $X1; k2*S


      # Species initializations: 
      k1 = 0.1; k2 = 0.2;
      S = 0;
''')

#result = r.simulate(0, 10, 50, ['Time', '[S4]'])
# note that plot only shows var species not const
result = r.simulate(0, 10, 50)

print(result)

r.plot (result)

