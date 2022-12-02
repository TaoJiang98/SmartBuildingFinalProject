import matplotlib.pyplot as plt

time = ["14/08-12", "14/12-16", "14/16-20", "14/20-24", "15/08-12", "15/12-16", "15/16-20", "15/20-24", "16/08-12", "16/12-16", "16/16-20", "16/20-24", "17/08-12", "17/12-16", "17/16-20", "17/20-24", "18/08-12", "18/12-16", "18/16-20", "18/20-24"]

# Temperature
NW = [21.11, 21.47, 21.47, 21.49, 20.55, 21.32, 21.59, 21.63, 20.53, 21.65, 21.97, 21.75, 20.77, 21.49, 21.8, 21.57, 20.55, 21.34, 21.7, 21.88]
NE = [21.03, 21.02, 21.07, 21.17, 20.53, 20.69, 20.86, 20.95, 20.25, 20.89, 21.39, 21.4, 20.57, 20.83, 21.19, 21.41, 20.28, 20.86, 21.26, 21.34]
SE = [14.3, 16.29, 19.12, 18.82, 19.15, 17.08, 18.38, 18.33, 16.39, 18.53, 20.29, 19.9, 15.28, 18.96, 20.64, 20.18, 14.62, 17.75, 20.41, 19.74]
SW = [20.67, 20.65, 20.64, 20.54, 20.91, 20.66, 20.59, 20.78, 20.73, 20.77, 20.73, 20.89, 19.8, 20.61, 20.85, 20.64, 19.89, 20.43, 20.73, 20.81]

plt.plot(time, NW, 'o-', color='r', label='NW')
plt.plot(time, NE, 'o-', color='g', label='NE')
plt.plot(time, SW, 'o-', color='b', label='SW')
plt.plot(time, SE, 'o-', color='orange', label='SE')
plt.tick_params(axis='x', labelrotation=90)
plt.title('Temperature in LinkLab from 11/14 - 11/18')

plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.legend(loc = "best")

plt.show()

# Humidity

NW = [27.78, 23.93, 22.15, 21.66, 24.75, 23.53, 26.23, 28.01, 29.82, 30.51, 27.67, 24.78, 24.98, 20.46, 19.09, 18.81, 20.62, 18.99, 18.99, 19.16]
NE = [21.33, 18.69, 17.24, 17.05, 19.57, 19.84, 22.57, 24.11, 24.44, 24.81, 23.19, 20.24, 20.88, 16.5, 15.5, 15.17, 16.8, 15.42, 16.39, 16.24]
SE = [38.84, 34.29, 24.85, 25.68, 24.85, 35.17, 37.35, 39.94, 42.49, 42.57, 29.6, 27.37, 31.0, 23.16, 19.29, 20.4, 29.56, 22.5, 18.23, 20.26]
SW = [28.63, 24.26, 22.84, 22.25, 25.7, 25.2, 28.36, 30.62, 30.94, 31.9, 28.28, 25.88, 25.61, 20.69, 19.68, 19.44, 20.91, 19.92, 19.97, 20.36]

plt.plot(time, NW, 'o-', color='r', label='NW')
plt.plot(time, NE, 'o-', color='g', label='NE')
plt.plot(time, SW, 'o-', color='b', label='SW')
plt.plot(time, SE, 'o-', color='orange', label='SE')
plt.tick_params(axis='x', labelrotation=90)
plt.title('Humidity in LinkLab from 11/14 - 11/18')

plt.xlabel("Time")
plt.ylabel("Humidity")
plt.legend(loc = "best")

plt.show()

# spl_a

NE = [52.34, 53.21, 53.29, 53.5, 52.44, 52.81, 55.75, 53.0, 52.03, 52.5, 56.37, 58.02, 52.38, 53.21, 53.99, 55.96, 52.62, 53.49, 55.91, 55.38]
SE = [52.48, 50.64, 51.78, 53.13, 52.38, 53.03, 52.99, 52.61, 51.82, 51.37, 52.19, 53.57, 52.31, 52.32, 53.29, 52.99, 55.34, 52.94, 51.6, 49.72]

plt.plot([], [], color='r', label='NW Unavailable')
plt.plot(time, NE, 'o-', color='g', label='NE')
plt.plot([], [], color='b', label='SW Unavailable')
plt.plot(time, SE, 'o-', color='orange', label='SE')

plt.tick_params(axis='x', labelrotation=90)
plt.title('Noise Level in LinkLab from 11/14 - 11/18')

plt.xlabel("Time")
plt.ylabel("Noise Level  (spl_a)")
plt.legend(loc = "best")

plt.show()

# awair_score

NW = [88.08, 88.77, 88.21, 88.05, 88.15, 88.41, 88.04, 90.51, 89.98, 91.45, 84.31, 88.72, 87.81, 86.67, 71.27, 82.02, 84.88, 86.38, 86.27, 86.91]
NE = [88.88, 89.22, 88.55, 88.37, 88.15, 89.46, 88.98, 91.08, 89.87, 91.99, 87.32, 84.94, 86.8, 87.68, 80.91, 83.45, 85.86, 86.62, 84.43, 84.57]
SE = [84.21, 81.8, 82.6, 82.81, 83.35, 83.86, 84.45, 85.58, 84.81, 84.53, 84.11, 83.84, 83.01, 79.76, 77.88, 80.17, 80.73, 78.79, 80.5, 82.5]

plt.plot(time, NW, 'o-', color='r', label='NW')
plt.plot(time, NE, 'o-', color='g', label='NE')
plt.plot([], [], color='b', label='SW Unavailable')
plt.plot(time, SE, 'o-', color='orange', label='SE')
plt.tick_params(axis='x', labelrotation=90)
plt.title('Air Quality in LinkLab from 11/14 - 11/18')

plt.xlabel("Time")
plt.ylabel("Air Quality")
plt.legend(loc = "best")

plt.show()

#Illumination_lx

NE = [0.0, 17.86, 11.07, 78.33, 0.0, 36.62, 195.62, 123.98, 0.0, 17.35, 226.97, 235.34, 0.0, 24.29, 197.61, 157.82, 0.0, 43.57, 142.92, 132.41]
SE = [0.68, 1414.76, 254.54, 51.61, 0.03, 50.41, 113.0, 27.08, 0.14, 1439.63, 265.7, 81.29, 0.05, 1505.07, 311.74, 59.19, 0.75, 1126.8, 217.44, 44.31]

plt.plot([], [], color='r', label='NW Unavailable')
plt.plot(time, NE, 'o-', color='g', label='NE')
plt.plot([], [], color='b', label='SW Unavailable')
plt.plot(time, SE, 'o-', color='orange', label='SE')
plt.tick_params(axis='x', labelrotation=90)
plt.title('Light Level in LinkLab from 11/14 - 11/18')

plt.xlabel("Time")
plt.ylabel("Light Level")
plt.legend(loc = "best")

plt.show()