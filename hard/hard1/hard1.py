import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image

bg = Image.open("background2.jpg")
bg = np.array(bg)

fig, ax = plt.subplots()

ax.imshow(bg, extent=[-2, 2, -2, 2])  

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')


body, = ax.plot([], [], 'o', markersize=15)

radius = 1.0

def update(frame):
    angle = np.radians(frame)

    x = radius * np.cos(angle)
    y = radius * np.sin(angle)

    body.set_data([x], [y])
    return body,

ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=30)

plt.show()
