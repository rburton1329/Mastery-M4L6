"""
cube_plot.py

This program generates cubic numbers (numbers multiplied by themselves three times).
- It first makes a chart of the first 5 cubes.
- Then it makes a larger chart of the first 5,000 cubes.
- It uses matplotlib to plot these as scatter graphs.
Plain-English: It shows how cubes grow really fast when numbers get bigger.
"""

# CUBE.PY
# Plots the first 5 and first 5000 cubic numbers with a colormap

import matplotlib.pyplot as plt
import numpy as np

# First 5 cubic numbers
x_small = np.arange(1, 6)
y_small = x_small ** 3

plt.figure(figsize=(6, 4))
plt.plot(x_small, y_small, marker='o', color='blue')
plt.title("First 5 Cubic Numbers")
plt.xlabel("Number")
plt.ylabel("Cube")
plt.grid(True)
plt.show()

# First 5000 cubic numbers with colormap
x_large = np.arange(1, 5001)
y_large = x_large ** 3

plt.figure(figsize=(10, 6))
# Apply a colormap by mapping each point to a color
colors = plt.cm.viridis(np.linspace(0, 1, len(x_large)))
plt.scatter(x_large, y_large, c=colors, s=10)
plt.title("First 5000 Cubic Numbers with Colormap")
plt.xlabel("Number")
plt.ylabel("Cube")
plt.grid(True)
plt.show()
