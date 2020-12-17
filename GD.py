# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 14:30:34 2020

@author: hungnd
"""

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

def compute_gradient(W):
    return np.array([8 * W[0], 2 * W[1]])

def f(W):
    return 4*W[0]**2 + W[1]**2

def update(W, alpha, grad, cache):
    return W - alpha * grad, cache #vanilla update

w0_grid = np.linspace(-6, 6, 30)
w1_grid = np.linspace(-12, 12, 30)

W_grid = np.meshgrid(w0_grid, w1_grid)
Z = f(W_grid)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(W_grid[0], W_grid[1], Z, 50, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');

ax.view_init(60, 35)

W = np.array([5, 10])

trajectory = [np.append(W, f(W))]

alpha = 0.2
#alpha = 0.05
tolerance = 10E-9
e = 1
cache = []

while e > tolerance:
    grad = compute_gradient(W)
    W, cache =  update(W, alpha, grad, cache)
    trajectory = np.append(trajectory, [np.append(W, f(W))], axis=0)
    e = np.amax(np.absolute(grad))

print(W)
print(len(trajectory))

ax.scatter3D(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], c='red', cmap='Reds');
ax.plot3D(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], 'red')

plt.show()