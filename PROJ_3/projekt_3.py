import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

"""###Set dx and approximation range"""

#@title Set step { run: "auto" }
# dx = 0.33 #@param {type:"slider", min:0.01, max:0.5, step:0.01}
# approx_range = 16 #@param {type:"slider", min:2, max:50, step:1}

dx = float(input("dx: "))
approx_range = int(input("range: "))

# Starting point
x0 = 1
y0 = 1


def exact_function(x):
    return np.sqrt((4*np.power(x, 2))/(np.power(x, 2)+1) - 1)

# derivative approximation
def approximate_dx_dy(y, x):
    return ((np.power(y,2)+1)/((np.power(x,2)+1)*x*y))


def midpoint(y, x, dx):
    h = dx
    k1 = approximate_dx_dy(y, x)
    k2 = approximate_dx_dy(y + h/2 * k1, x + h/2)
    return y + h*k2

"""###Value calculation"""

X = [x for x in np.arange(x0, approx_range, dx)] # list of x values
Y = [y0]                                         # list of approximated y values
Y_exact = [y0]                                   # list of exact y values
yerr = [0]                                       # list of errors

# calculate Y and error values
for i, x in enumerate(X[1:]):
    Y.append(midpoint(Y[i], x, dx))
    Y_exact.append(exact_function(x))
    yerr.append(Y_exact[i] - Y[i])

"""###Midpoint function plotting"""

sns.set_style("darkgrid")

fig, ax = plt.subplots()
fig.set_size_inches(10, 4, True)
ax.set_title("Function approximation using Midpoint method")

ax.plot(X, Y, label='Approximation')
ax.plot(X, Y_exact, label='Exact')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

ax.fill_between(X, Y, Y_exact, facecolor='red', alpha=0.1)

for i in range(0, len(X), (len(X))//2-1):
    t = ax.text(1.02*X[i], 0.98*Y[i], "error ~= {}".format(np.round(yerr[i],7)))
    t.set_bbox(dict(facecolor='gray', alpha=0.1, edgecolor='black'))
    ax.plot([X[i], X[i]], [Y[i], Y_exact[i]], "--")

plt.show(block=False)


def runge_kutta(y, x, dx):
    h = dx
    k1 = approximate_dx_dy(y, x)
    k2 = approximate_dx_dy(y + h/2 * k1, x + h/2)
    k3 = approximate_dx_dy(y + h/2 * k2, x + h/2)
    k4 = approximate_dx_dy(y + h*k3, x + h)
    return y + h * (k1 + 2*k2 + 2*k3 + k4) / 6

"""###Value calculation"""

X = [x for x in np.arange(x0, approx_range, dx)] # list of x values
Y = [y0]                                         # list of approximated y values
Y_exact = [y0]                                   # list of exact y values
yerr = [0]                                       # list of errors

# calculate Y and error values
for i, x in enumerate(X[1:]):
    Y.append(runge_kutta(Y[i], x, dx))
    Y_exact.append(exact_function(x))
    yerr.append(Y_exact[i] - Y[i])

"""###Runge-Kutta function plotting"""

sns.set_style("darkgrid")

fig, ax = plt.subplots()
fig.set_size_inches(10, 4, True)
ax.set_title("Function approximation using Runge-Kutta method")


ax.plot(X, Y, label='Approximation')
ax.plot(X, Y_exact, label='Exact')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

ax.fill_between(X, Y, Y_exact, facecolor='red', alpha=0.1)

for i in range(0, len(X), (len(X))//2-1):
    t = ax.text(1.02*X[i], 0.98*Y[i], "error ~= {}".format(np.round(yerr[i],7)))
    t.set_bbox(dict(facecolor='gray', alpha=0.1, edgecolor='black'))
    ax.plot([X[i], X[i]], [Y[i], Y_exact[i]], "--")

plt.show()
