"""
1) Case where graph has global maximum.
2) The lower and upper Limits must be defined because there is a possiblity
   that the function's global maximum is not defined when f(x) --> infinity
   as x --> infinity.
   Another reason for defining limits is f(x) changes its shape (which could
   produce maxima and minima) in particular interval. Otherwise f(x) will move
   towards infinity in increasing or decreasing direction.
3) alpha is the step rate.
4) Input:
   f(x) = x^4 + 3x^3 - 9x^2 - 23x - 1
   Slope = 4x^3 + 9x^2 - 18x - 23

"""
import random
def hillClimb(func, lowerLimit, upperLimit, alpha):
    # Calculate the Slope of Polynomial function
    slopeFunc = []
    for i in range(len(func)):
        if i != 0:
            slopeFunc.append(i * func[i])
    # Any Random Start
    x = round(random.uniform(lowerLimit, upperLimit), 4)
    print("Starting at :",x)
    while True:
        slope = 0
        for i in range(len(slopeFunc)):
            slope = round(slope + (x**i) * slopeFunc[i], 4)
##        print("Slope :",slope)
        if abs(slope) <= 0.001:
            break
        x = round(x + alpha*slope, 5)
##        print("x", x)
    return round(x, 1)


##p = [-1, -23, -9, 3, 1]
##lL = -3.103
##uL = 1.853

##p = [5, 5, -1]
##uL = 6
##lL = -1
n = int(input("Enter Highest degree in the polynomial : "))
p = list(map(int, input("Enter the coeficients : ").split()))
p.reverse()
lL = float(input("Enter Lower limit of function : "))
uL = float(input("Enter Upper limit of function : "))
print("Peak :", hillClimb(p, lL, uL, 0.01))
