from math import radians
from math import cos
from math import sin
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
g = 9.81
t = 0
u = int(input("Enter speed of throw(in m/s): "))
ang_deg = int(input("Enter angle of throw(in degree): "))
ang_rad = radians(ang_deg)
x = u * cos(ang_rad) * t
y = (u * sin(ang_rad) * t) - (1/2 * g * t**2)
range = (u**2 * sin(2*ang_rad)) / g
x_coordinates = []
y_coordinates = []
while x < range:
    x = u * cos(ang_rad) * t
    y = (u * sin(ang_rad) * t) - (1/2 * g * t**2)
    x_coordinates.append(x)
    y_coordinates.append(y)
    if u > 30:
        t += 0.3
    elif u > 20:
        t += 0.2
    else:
        t += 0.1

plt.figure(figsize=(10, 6))
plt.title('Projectile Motion Animation from Coordinate List')
plt.xlabel('Horizontal Distance (x)')
plt.ylabel('Vertical Height (y)')
plt.grid(True, linestyle='--')

if x_coordinates and y_coordinates:
    plt.xlim(min(x_coordinates) * 0.9, max(x_coordinates) * 1.1)
    plt.ylim(min(y_coordinates) * 0.9, max(y_coordinates) * 1.2)
else:
    print("Coordinate lists are empty!")
    exit()
    
plt.ion() 

for i, (x_instant, y_instant) in enumerate(zip(x_coordinates, y_coordinates)):
    
    plt.clf() 
    
    plt.title(f'Projectile Motion Animation (t={i * 0.3:.2f} s)')
    plt.xlabel('Horizontal Distance (x)')
    plt.ylabel('Vertical Height (y)')
    plt.grid(True, linestyle='--')
    plt.xlim(min(x_coordinates) * 0.9, max(x_coordinates) * 1.1)
    plt.ylim(min(y_coordinates) * 0.9, max(y_coordinates) * 1.2)
    
    plt.plot(x_coordinates[:i+1], y_coordinates[:i+1], 'b--', linewidth=1, label='Path Trace')
    
    plt.plot(x_instant, y_instant, 'ro', markersize=8, label='Projectile') 
    
    plt.legend(loc='upper left')
    plt.gcf().canvas.draw() 
    plt.pause(0.01) 

plt.ioff()
plt.title(f'Projectile Motion (Complete Trajectory)')
plt.show()
