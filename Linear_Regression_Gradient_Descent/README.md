# Gradient Descent Example for Linear Regression

This example project demonstrates how the gradient descent algorithm may be used to solve a linear regression problem. A more detailed description of this example can be found here.

## Code Requirements

The example code is in Python (version 2.6 or higher will work). The only other requirement is NumPy.

## Description

This code demonstrates how a gradient descent search may be used to solve the linear regression problem of fitting a line to a set of points. In this problem, we wish to model a set of points using a line. The line model is defined by two parameters - the line's slope m, and y-intercept b. Gradient descent attemps to find the best values for these parameters, subject to an error function.

The code contains a main function called run. This function defines a set of parameters used in the gradient descent algorithm including an initial guess of the line slope and y-intercept, the learning rate to use, and the number of iterations to run gradient descent for.

## Overview

Here are some helpful links:

#### Gradient descent visualization
https://raw.githubusercontent.com/mattnedrich/GradientDescentExample/master/gradient_descent_example.gif

#### Sum of squared distances formula (to calculate our error)
https://spin.atomicobject.com/wp-content/uploads/linear_regression_error1.png

#### Partial derivative with respect to b and m (to perform gradient descent)
https://spin.atomicobject.com/wp-content/uploads/linear_regression_gradient1.png

## Dependencies

* numpy

Python 2 and 3 both work for this. Use [pip](https://pip.pypa.io/en/stable/) to install any dependencies.

## Execution

Just run ``python gradient_descent.py`` to see the results:

   ```
Starting gradient descent at b = 0, m = 0, error = 5565.107834483211
Running...
After 1000 iterations b = 0.08893651993741346, m = 1.4777440851894448, error = 112.61481011613473
   ```

## Credits

Credits for this code go to [mattnedrich](https://github.com/mattnedrich). I've merely created a wrapper to get people started. 

