import numpy as np
from simulator import Simulator, centerline
import math

sim = Simulator()
 # YOUR CODE HERE
def lookahead(S):
    """coordinates of centerline on track at S meters from start"""
    lookahead = centerline(S)
    return lookahead
def controller(x):
    """controller to make car go straight"""
    # Constant forward acceleration
    a = 1.0
    """first find current position of the car """
    x_pos = x[0]
    y_pos = x[1]
    """set a lookahead distance of 2 meters"""
    lookpoint = lookahead(8)
    """change in x and y after going from current to target position"""
    delta_x = lookpoint[0] - x_pos
    delta_y = lookpoint[1] - y_pos
    """heading is the """
    current_heading = x[2]
    heading_error = math.atan2(delta_y, delta_x) - current_heading
    """phi_dot is the rate of change of the steering wheel so need to do more calculations to find the phi_dot from the angle of the 
    steering"""
    target_steering = math.atan(2 * 1.58 * math.sin(heading_error) / 8)
    current_steering = x[4]
    k= 1
    phi_dot = max(-1.0, min(1.0, k * (target_steering - current_steering)))
    return np.array([a, phi_dot])

sim.set_controller(controller)
sim.run()
sim.animate()
sim.plot()

