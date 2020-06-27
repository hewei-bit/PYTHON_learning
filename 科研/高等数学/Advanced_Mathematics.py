from sympy import *

# x = symbols('x')
x, y = symbols('x y')

# 求导
print(diff(x ** 8, x, 1))

# 不定积分
print(integrate(2 * x ** 2 - x + 1, x))

# 定积分
print(integrate(2 * x ** 2 - x + 1, (x, -1, 1)))

# 多重积分

# 求极限
