import numpy as np
import matplotlib.pyplot as plt
from galpy.orbit import Orbit
from galpy.potential import MWPotential2014
import astropy.units as u


o = Orbit(vxvv=[8.0*u.kpc, 0*u.km/u.s, 220*u.km/u.s,
                0*u.kpc, 0*u.km/u.s, 0*u.rad],
          ro=8*u.kpc, vo=220*u.km/u.s)


ts = np.linspace(0, 1, 1000) * u.Gyr


o.integrate(ts, MWPotential2014)


x = o.x(ts)
y = o.y(ts)


plt.figure(figsize=(6,6))
plt.plot(x, y, color='yellow')
plt.scatter(0, 0, color='black', label='Galactic Center')
plt.scatter(x[0], y[0], color='blue', label='Sun')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Orbit of the Sun around Milky Way")
plt.axis("equal")
plt.legend()
plt.grid()
plt.show()
