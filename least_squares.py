import math

def sum_x(x):
    s = 0
    for i in x:
        s += i

    return s

def sum_x_sqr(x):
    s = 0
    for i in x:
        s += math.pow(i, 2)

    return s

def sum_y(y):
    s = 0
    for i in y:
        s += i

    return s

def sum_xy(x, y):
    s = 0
    for i in range(0, len(x)):
        s += x[i]*y[i]

    return s

def sum_x_cube(x):
    s = 0
    for i in x:
        s += math.pow(i,3)

    return s

def sum_x_4(x):
    s = 0
    for i in x:
        s += math.pow(i, 4)

    return s

def sum_xy_sqr(x, y):
    s = 0
    for i in range(0,len(x)):
        s += y[i]*x[i]*x[i]

    return s

def m(x, y):
    return (sum_xy(x, y)*len(x) - sum_x(x)*sum_y(y))/(sum_x_sqr(x)*len(x) - sum_x(x)*sum_x(x))

def b(x, y):
    return (sum_y(y) - sum_x(x)*m(x, y))/len(x)


def f(x):
    return -194.1382407320968 + 72.08451769539681*x

def error(x, y):
    s = 0
    for i in range(0, len(x)):
        s += math.pow(f(x[i]) - y[i], 2)

    return math.sqrt(s/len(x))

x = [4, 4.2, 4.5, 4.7, 5.1, 5.5, 5.9, 6.3, 6.8, 7.1]
y = [102.56, 113.18, 130.11, 142.05, 167.53, 195.14, 224.87, 256.73, 299.5, 326.72]
print(error(x,y))