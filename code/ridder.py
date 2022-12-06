import math
import matplotlib.pyplot as plt
from numpy import sign

# Approximate Earth-Moon system scaled values for CR3BP model
U_1 = 0.98785
U_2 = 1 - U_1


def f(x):
    return x - U_1 * (x + U_2) / (abs(x + U_2)) ** 3 - U_2 * (x - U_1) / (abs(x - U_1)) ** 3

def g(x):
    return x * math.exp(x) - 10

def h(x, a):
    return f(x)*math.exp(a*x)

def method(array, tolerance):
    lagrange = [[], [], []]

    for i in range(3):
        error = 1000
        x_0 = array[i][0]
        x_1 = array[i][1]
        x_2 = 0
        x_3 = 0
        t = 0
        print("Bound {}:".format(i+1))
        while(error > tolerance and t < 50):
            x_2 = (x_0 + x_1)/2

            fx_0 = f(x_0)
            fx_1 = f(x_1)
            fx_2 = f(x_2)
            d = (math.sqrt(fx_2**2 - fx_0*fx_1))
            if d == 0:
                return None
            dx = (x_2 - x_0)*fx_2/d
            if (x_0 - x_1) < 0.0: dx = -dx 
            x_3 = x_2 + dx
            fx_3 = f(x_3)
            
            if sign(fx_2) == sign(fx_3):
                if sign(fx_0) != sign(fx_3):
                    x_1 = x_3
                else:
                    x_0 = x_3
            else:
                x_0 = x_2
                x_1 = x_3

            error = abs(f(x_3))
            print("Iteration {}: error = {} at x_3 = {}".format(t+1, error, x_3))
            t += 1
            lagrange[i].append(error)
            
        print("val of root: ", x_3)
    return lagrange

def method_2(array, tolerance):
    error = 1000
    x_0 = array[0]
    x_1 = array[1]
    x_2 = 0
    x_3 = 0
    t = 0
    while(error > tolerance and t < 10):
        x_2 = (x_0 + x_1)/2

        fx_0 = g(x_0)
        fx_1 = g(x_1)
        fx_2 = g(x_2)
        d = (math.sqrt(fx_2**2 - fx_0*fx_1))
        if d == 0:
            return None
        dx = (x_2 - x_0)*fx_2/d
        if (fx_0 - fx_1) < 0.0: dx = -dx 
        x_3 = x_2 + dx
        fx_3 = g(x_3)

        # print("y vals of the set: {} {} {} {}".format(fx_0, fx_1, fx_2, fx_3))
        
        if sign(fx_2) == sign(fx_3):
            if sign(fx_0) != sign(fx_3):
                print("1")
                x_1 = x_3
            else:
                print("2")
                x_0 = x_3
        else:
            print("3")
            x_0 = x_2
            x_1 = x_3

        error = abs(g(x_3))
        print("Iteration {}: error = {} at x_3 = {}".format(t, error, x_3))
        
        t += 1
    print("val of root: ", x_3)

def main():
    tolerance = 1E-5

    bounds_1 = [[-2*U_1, -U_2 - tolerance], [-U_2 + tolerance, U_1 - tolerance], [U_1 + tolerance, 2*U_1]]
    bounds_2 = [[-1.1, -0.9], [0.75, 0.95], [1.05, 1.15]]
    print("original, guessed bounds: ")
    original_result = method(bounds_1, tolerance)
    print("approximated bounds: ")
    bounded_result = method(bounds_2, tolerance)
    
    plt.plot(original_result[0])
    plt.plot(original_result[1])
    plt.plot(original_result[2])
    
    plt.xlabel('iterations')
    plt.ylabel('log error')
    plt.yscale('log')

    plt.legend(["Between [-1.975, -0.01251]", "Between [0.01251, 0.98749]", " Between [0.98751, 1.975]"])
    
    plt.title('Ridder\'s Method Approximation with Original Bounds')
    
    plt.show()

    plt.plot(bounded_result[0])
    plt.plot(bounded_result[1])
    plt.plot(bounded_result[2])
    
    plt.xlabel('iterations')
    plt.ylabel('log error')
    plt.yscale('log')  
    
    plt.legend(["Between [-1.1, -0.9]", "Between [0.75, 0.95]", " Between [1.05, 1.15]"])

    plt.title('Ridder\'s Method Approximation with New Bounds')
    
    plt.show()


    

main()
