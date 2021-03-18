def factorial(n:int) -> int:
    if n == 0:
        return 1
    return n*factorial(n-1)

def power_integer(x:float,y:int)-> float:
    if y==0:
        return 1
    ans=x
    for i in range(1,y):
        ans=ans*x
    return ans   

def exponent(x:float ,n:int=300) ->float: 
    sum = 1.0 
    for i in range(n, 0, -1): 
        sum = 1 + x * sum / i 
    return sum


def absolute_value(num: float) ->float:
    if num < 0:
        return num*-1
    return num

def ln_expression(x:float , y:float)-> float:
    val = y + 2*(x - exponent(y)) / (x + exponent(y))
    return val

def Ln(x):
    if x <= 0 :
        return 0
    eps = 0.001
    y_0 = x - 1
    y_1 = ln_expression(x,y_0)
    while absolute_value(y_0 - y_1)>eps:
        y_0,y_1 = y_1 , ln_expression(x,y_1)
    return y_1

def XtimesY(x:float , y:float)->float:
    if x<=0:
        return 0
    return float('%0.6f' % exponent(y*Ln(x)))

def sqrt(x:float,y:float) -> float:
    if x ==	0 or y<0:
        return 0
    return XtimesY(y, 1/x)

def calculate(x:float) -> float:
    return exponent(x)*XtimesY(7, x)*XtimesY(x, -1)*sqrt(x,x)
