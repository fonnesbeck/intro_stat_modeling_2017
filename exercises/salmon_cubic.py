sum_squares_cubic = lambda theta, x, y: np.sum((y - theta[0] - theta[1]*x - theta[2]*(x**2) 
                                  - theta[3]*(x**3)) ** 2)
                                  
plt.plot(salmon.spawners, salmon.recruits, 'r.')
b0,b1,b2,b3 = fmin(sum_squares_cubic, [0,1,-1,0], args=(salmon.spawners, salmon.recruits))
xvals = np.arange(500)
plt.plot(xvals, b0 + b1*xvals + b2*(xvals**2) + b3*(xvals**3))