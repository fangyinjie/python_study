from z3 import *
import numpy as np

x = Int('x')
print( "1st child:", arg(0))
print( "2nd child:", np.arg(1))
print( "operator: ", np.decl())
print( "op name:  ", np.decl().name())
