print("This is the database module and python calls it {}".format(__name__))

from blood_calculator import *
from numpy import *

check_HDL()

numpy.check_HDL()

import analysis

HDL_value = 55

classification = bc.check_HDL(HDL_value)
otheranswer analysis.check_HDL()
print("55 is {}".format(classification))
x = check_LDL(200)


