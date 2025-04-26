import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

def heart_3d(t, v):
    x = 16 * (np.sin(t)**3)
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    z = (np.sin(v) * 8) 
    return x, y, z
    
t = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
t, v = np.meshgrid(t, v)
x, y, z = heart_3d(t, v)

n_particles = 300
particles_x = 16 * (np.random.rand(n_particles) * 2 - 1)**3
particles_y = 13 * np.random.rand(n_particles) - 5 * np.random.rand(n_particles) - 2 * np.random.rand(n_particles) - np.random.rand(n_particles)
particles_z = 8 * (np.random.rand(n_particles) * 2 - 1)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')
fig.patch.set_facecolor('black')

heart_surface = ax.plot_surface(x, y, z, color='red', alpha=0.7, edgecolor='pink')
particles = ax.scatter(particles_x, particles_y, particles_z, color='white', s=10)

def update(frame):
    ax.view_init(elev=30, azim=frame)
    return fig,
    
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)
plt.axis('off') 
plt.show()
