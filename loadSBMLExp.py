import roadrunner
r = roadrunner.RoadRunner("mySBMLModel.xml")

result = r.simulate(0, 10, 50)

print(result)

r.plot (result)

