import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, lambdify

def derivative():
    function_input = input("Enter a polynomial function ex. 3x^4 would be 3*x**4: ")
    x = symbols('x')

    try:
        derivative_exp = diff(function_input, x)
        function = lambdify(x, derivative_exp, 'numpy')
        x = np.linspace(-100, 100)
        y = function(x)

        plt.plot(y, linewidth = '5')
        plt.xlabel('x')
        plt.ylabel("f'(x)")
        plt.title(f"Derivative of {function_input} ")
        plt.grid(True)
        plt.show()

    except:
        print("enter a valid function.")
        return
    
while True:
    derivative()

 