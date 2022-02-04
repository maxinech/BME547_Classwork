# print("This is the database module and python calls it {}".format(__name__))

# from blood_calculator import *
# from numpy import *
# import analysis
# numpy.check_HDL()
import blood_calculator as bc
HDL_value = 55
classification = bc.check_HDL(HDL_value)
# otheranswer analysis.check_HDL()
print("55 is {}".format(classification))
x = bc.check_LDL(200)
