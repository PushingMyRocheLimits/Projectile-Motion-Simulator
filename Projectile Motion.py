from vpython import *
import math

# Creates the canvas and the axes for reference
scene = canvas(title='<b>Projectile Motion Simulation</b>', width=640, height=480,
               caption='The <b>blue ball</b> experiences the effects of drag.'
                       ' The <b>orange ball</b> does not have any drag.')
x_axis = cylinder(pos=vector(0, 0, 0), axis=vector(1, 0, 0), size=vector(50, 0.1, 0.1), color=color.white, opacity=0.5)
y_axis = cylinder(pos=vector(0, 0, 0), axis=vector(0, 1, 0), size=vector(50, 0.1, 0.1), color=color.white, opacity=0.5)
scene.camera.pos = vector(5, 0, -15)

# Creates graph for precise reference
graph(title='<b>Position vs. Time Graph</b>', xtitle='Time (Seconds)', ytitle='Position (Meters)')
x_graph1 = gcurve(color=color.red, label="X Velocity of Ball 1")
y_graph1 = gcurve(color=color.orange, label="Y Velocity of Ball 1")
x_graph2 = gcurve(color=color.blue, label="X Velocity of Ball 2")
y_graph2 = gcurve(color=color.cyan, label="Y Velocity of Ball 2")

# Creates the two spheres
radius = 0.2  # Adjust this value for different sized spheres
ball1 = sphere(pos=vector(0, radius, 0), make_trail=True, radius=radius, color=color.orange, trail_radius=0.05)
ball2 = sphere(pos=vector(0, radius, 0), make_trail=True, radius=radius, color=color.cyan, trail_radius=0.05)
ball_mass = float(input('Enter mass of ball in kilograms: '))
theta = math.radians(float(input('Enter angle theta in degrees: ')))
magnitude = float(input('Enter the velocity in m/s: '))

# Initial parameters
grav = 9.81
drag_coefficient = 0.47  # Drag Coefficient of a Sphere
ball_vel1 = vector(magnitude * math.cos(theta), magnitude * math.sin(theta), 0)
ball_vel2 = vector(magnitude * math.cos(theta), magnitude * math.sin(theta), 0)
time = 0
delta_t = 0.01

scene.pause("Click to begin simulation: ")
while True:
    rate(200)

    # Simulates ball without the effect of drag
    if ball1.pos.y >= 0:
        force1 = -ball_mass * grav * vector(0, 1, 0)  # No drag in this so F=W
        ball_vel1 = ball_vel1 + force1 / ball_mass * delta_t  # V = V0 + F/M*t
        ball1.pos = ball1.pos + ball_vel1 * delta_t  # x = x0+v*t
        x_graph1.plot(time, ball1.pos.x)
        y_graph1.plot(time, ball1.pos.y)
    else:
        continue

    # Simulates ball with the effect of drag
    if ball2.pos.y >= 0:
        weight2 = -ball_mass * grav * vector(0, 1, 0)
        drag2 = -drag_coefficient * ball_vel2
        force2 = weight2 + drag2
        ball_vel2 = ball_vel2 + force2 / ball_mass * delta_t
        ball2.pos = ball2.pos + ball_vel2 * delta_t
        x_graph2.plot(time, ball2.pos.x)
        y_graph2.plot(time, ball2.pos.y)
    else:
        continue

    # Stops simulation once both spheres touch the ground
    if ball1.pos.y == 0 and ball2.pos.y == 0:
        break

    time = time + delta_t
