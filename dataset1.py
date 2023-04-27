import numpy as np
import matplotlib
import matplotlib.font_manager as font_manager
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_prop = font_manager.FontProperties(fname = font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()

def true_function(x):
    return np.sin(np.pi * x * 0.8)*10


def test_true_function():
    assert true_function(np.array([0])) == np.array([0])

x = np.arange(-1,1,0.01)

y = true_function(x)

import matplotlib.pyplot as plt

plt.scatter(x, y, color="black") # 점을 나타낸다
plt.xlabel('x')
plt.ylabel('y')
plt.xticks(())
plt.savefig("ex1.1.png")
plt.show()