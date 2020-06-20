from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
 
def func(x, a, b, c, d):
    return a * np.exp(b * x + c) + d
 
x = np.array([0,2,4,6,8,10,12,14,16,18,20,25,30,35,40,45,50,55,60])
y = np.array([20.325,17.802,14.519,11.484,8.646,6.532,4.427,2.617,0.975,-0.454,-2.066,-4.295,-6.276,-7.597,-8.643,-9.420 ,-9.965,-10.367,-10.699])
popt, pcov = curve_fit(func, x, y, p0=[2.5,-0.03,1.9,4.8], maxfev=10000)
a=popt[0] # popt里面是拟合系数，读者可以自己help其用法
b=popt[1]
c=popt[2]
d=popt[3]
yvals=func(x,a,b,c,d)
calc_ydata = [func(i, a,b,c,d) for i in x]
res_ydata  = np.array(y) - np.array(calc_ydata)
ss_res     = np.sum(res_ydata**2)
ss_tot     = np.sum((y - np.mean(y))**2)
r  = 1 - (ss_res / ss_tot)
print(a,b,c,d)
print(r)
plot1=plt.plot(x, y, '*',label='original values')
plot2=plt.plot(x, yvals, 'r',label='curve_fit values')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(loc=4) # 指定legend的位置,读者可以自己help它的用法
plt.title('curve_fit')
plt.show()