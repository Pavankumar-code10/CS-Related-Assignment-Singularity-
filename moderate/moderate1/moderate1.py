import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

omega0 = 2.0
k = 0.03
t_max = 200
dt = 1

t = np.arange(0, t_max, dt)

omega = omega0 * np.exp(-k * t)

df = pd.DataFrame({
    "Time (days)": t,
    "Angular velocity (rad/day)": omega
})

threshold = 0.01


lock_data = df[df["Angular velocity (rad/day)"] <= threshold]

if not lock_data.empty:
    lock_time = lock_data.iloc[0]["Time (days)"]
    print("Approx tidal locking time:", lock_time, "days")
else:
    print("Tidal locking not reached in given time range")

plt.plot(df["Time (days)"], df["Angular velocity (rad/day)"])
plt.axhline(threshold, color='r', linestyle='--', label='Locking threshold')

plt.xlabel("Time (days)")
plt.ylabel("Angular velocity (radins/day)")
plt.title("Tidal Locking: Angular velocity vs Time")
plt.legend()
plt.grid()
plt.show()
