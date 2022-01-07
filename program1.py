from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

parametr = 1.120
T=2
w=np.pi

#A
print("zadanie A")

def f(t):
  return parametr*t**2

def fa1(t):
  return f(t)*np.cos(w*t)

def fa2(t):
  return f(t)*np.cos(2*w*t)

a0=1/T*quad(f, -1, 1)[0]
a1=2/T*quad(fa1, -1, 1)[0]
a2=2/T*quad(fa2, -1, 1)[0]


print("a0=",a0)
print('a1=',a1)
print('a2=',a2)

def F(t):
  return a0+a1*np.cos(np.pi*t)+a2*np.cos(2*np.pi*t)

t=np.linspace(-1, 1, 100)
fig, ax=plt.subplots()
ax.plot(t,f(t),t,F(t))
ax.grid(True)
plt.show()

#B
print("zadanie B")

a, b, c, t = symbols('a b c t')
A,B,C=a0, a1, a2

expr = (a*t**2+2*b*t+c -(A+B*cos(w*t)+C*cos(2*w*t)))*t**2
sol1 = integrate(expr, (t, -1, 1))
expr = (a*t**2+2*b*t+c -(A+B*cos(w*t)+C*cos(2*w*t))) * t
sol2 = integrate(expr, (t, -1, 1))
expr = (a*t**2+2*b*t+c -(A+B*cos(w*t)+C*cos(2*w*t)))
sol3 = integrate(expr, (t,-1,1))

equations = [
  Eq(sol1,  0 ),
  Eq(sol2, 0 ),
  Eq(sol3,0)
]
print(solve(equations))
