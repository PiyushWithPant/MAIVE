# This file is created to test the MAIVE package

from index import Maive as M

maive = M()

test = maive.QE_roots(a=3, b=-2, c=1/3)

print(test)
# print(float(test["alpha"]))



