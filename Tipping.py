import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *

data = np.loadtxt("tips.csv", delimiter=",", dtype = str)

x = data[1:, 0].astype(np.float32)
y = data[1:, 1].astype(np.float32)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]

print_equation(slope,intercept,"$","$")
#Output was: The equation of the line is y = 0.18221473222560391 $/$ x + -0.2922674195507699 $

fig = plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(x, slope, intercept),label='Linear Fit') 
plt.legend(loc='best')
plt.xlabel("Bill($)") 
plt.ylabel("Tips($)")  
plt.show()
fig.savefig('Bills_VS_Tips.png')

pcttip = data[1:, 6].astype(np.float32)
params1, params_cov1 = scipy.optimize.curve_fit(linear,x,pcttip)
new_slope = params1[0]
new_intercept = params1[1]
print_equation(new_slope,new_intercept,"$","%")
#Output was: The equation of the line is y = 0.04881243455874584 %/$ x + 15.509648238069316 %

fig = plt.figure()
plt.scatter(x, pcttip, label='Data')
plt.plot(x, linear(x, new_slope, new_intercept),label='Linear Fit') 
plt.legend(loc='best')
plt.xlabel("Bill($)") 
plt.ylabel("Percent Tip(%)")  
plt.show()
fig.savefig('Bills_VS_Percent_Tip.png')
