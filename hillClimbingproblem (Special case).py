"""
1) Case where graph has 2 maxima's.
2) The lower and upper Limits must be defined because there is a possiblity
   that the function's global maximum is not defined when f(x) --> infinity
   as x --> infinity.
   Another reason for defining limits is f(x) changes its shape (which could
   produce maxima and minima) in particular interval. Otherwise f(x) will move
   towards infinity in increasing or decreasing direction.
3) alpha is step rate.
4) Inputs:
   f(x) = x^2(1-x^2)^(1/2)
   slope = (2x - 3x^3)/(1 - x^2)^(1/2)

"""
import random
def hillClimb(lowerLimit, upperLimit, alpha):
    x = round(random.uniform(lowerLimit, upperLimit), 4)
    print("Starting at :",x)
    while True:
        slope = round((2*x - 3*x**3)/((1-x**2)**0.5), 4)
        if abs(slope) <= 0.001 :
            break
        x = round(x + alpha*slope, 5)
    return round(x)

print("Peak : ", hillClimb(-1, 1, 0.01))
