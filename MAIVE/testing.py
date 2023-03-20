# This file is created to test the MAIVE package

from index import Maive as M

maive = M()

test = maive.QE_roots(a=1, b=5, c=14)


print(test[0], test[1])


