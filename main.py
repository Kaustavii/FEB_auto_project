import numpy as np
from simulator import Simulator, centerline

sim = Simulator()

def controller(x):
    """controller for a car

    Args:
        x (ndarray): numpy array of shape (5,) containing [x, y, heading, velocity, steering angle]

    Returns:
        ndarray: numpy array of shape (2,) containing [fwd acceleration, steering rate]
    """
    ... # YOUR CODE HERE
def controller(x):
    """
    Minimal controller to see the car move in the simulator.
    """
    # Constant forward acceleration (safe)
    a = 1.0
    
    # Small constant steering rate (so the car wiggles a bit)
    phi_dot = 0
    
    return np.array([a, phi_dot]) 
def lookahead(S):
    """set lookahead distance to aim car to go to"""
    lookahead = centerline(S)
    return lookahead
sim.set_controller(controller)
lookahead(0.1)
sim.run()
sim.animate()
sim.plot()

