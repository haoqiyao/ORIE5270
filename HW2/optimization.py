import numpy as np
import scipy.optimize as op

def rosen(X):
    #this is the rosenbrock function
    x = X[0]
    y = X[1]
    z = X[2]
    return (1-x)**2+100*(y-x**2)**2+(1-y)**2+100*(z-y**2)**2

def grad(X):
    # this is the gradient of the rosenbrock function
    x = X[0]
    y = X[1]
    z = X[2]
    return np.array([400*x**3-2*(1-x)-400*x*y, 200*(y-x**2)+400*y**3-2*(1-y)-400*y*z, 200*(z-y**2)])

#different starting point
trial1 = [5, 2, 7]
trial2 = [-1, 1, 1]
trial3 = [8, 2, 9]
trials = [trial1, trial2, trial3]

result = []
for i in trials:
    #optimization product
    result.append(op.minimize(rosen, i, method='BFGS', jac=grad).fun)
print(min(result))
