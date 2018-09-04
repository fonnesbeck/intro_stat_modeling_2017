lsd_and_math.loc[7] = [6, 70]
x, y = lsd_and_math.T.values

b0_ss, b1_ss = fmin(sum_of_squares, [0,1], args=(x,y))
b0_abs, b1_abs = fmin(sum_of_absval, [0,0], args=(x,y))

ax = lsd_and_math.plot(x='Drugs', y='Score', style='ro', legend=False, xlim=(0,8))
ax.plot([0,10], [b0_ss, b0_ss+b1_ss*10])
ax.plot([0,10], [b0_abs, b0_abs+b1_abs*10], 'r--')