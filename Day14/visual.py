from matplotlib import pyplot as plt
from p2 import solve


_, pos, w, h = solve()
plt.rcParams["figure.figsize"] = [7.00, 7.00]
plt.rcParams["figure.autolayout"] = True
x = [i[0] for i in pos]
y = [i[1] for i in pos]
plt.xlim(0, w - 1)
plt.ylim(0, h - 1)
plt.grid()
plt.scatter(x, y)
plt.show()
