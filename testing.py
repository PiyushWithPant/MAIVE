# This file is created to test the MAIVE package

# from maive.maive import Maive

# import maive 

from maive.maive import Maive

m = Maive()

test = m.P_conditionalProbability(a=[1,2,3,4,5,6,7,8,9,10,11],
                                  b = [1,2,13,14,15,16],
                                  s = 36)



print(test)



