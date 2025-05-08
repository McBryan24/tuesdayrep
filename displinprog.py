import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)
y = 2.5 *x + np.random.random(50) * 2

A = np.vstack( [x, np.ones(len(x))]).T
slope, intercept = np. linalg. lstsq(A, y, rcond=None) [0]

y_pred = slope * x + intercept

plt.scatter(x, y, label='Data')
plt.plot(x, y_pred, color="red", label="Best Fit Line")
plt. legend()
plt.title("Simple Linear Regression with Numpy")
plt.xlabel("X")
plt.ylabel("Y")
plt. show()

print(f"Slope: {slope :.2f}, Intercept: {intercept :.2f}")