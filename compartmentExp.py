import tellurium as te
import matplotlib.pylab as plt

# Single gene expressing protein and protein undergoing degradation
r = te.loada ('''
      # Reactions: 
      compartment cytoplasm = 1.5, mitochondria = 2.6
      const S1 in mitochondria
      var S2 in cytoplasm
      var S3 in cytoplasm
      var S4 in cytoplasm

      S1 -> S2; k1*S1
      S2 -> S3; k2*S2
      S3 -> S4; k3*S3

      # Species initializations: 
      S1 = 10;  S2 = 0;  S3 = 0; S4 = 0;  
      k1 = 1; k2 = 1; k3 = 1; 
''')


te.saveToFile ('mySBMLModel.xml', r.getCurrentSBML())

#result = r.simulate(0, 10, 50, ['Time', '[S4]'])
# note that plot only shows var species not const
result = r.simulate(0, 10, 50)



print(result)

r.plot (result)

