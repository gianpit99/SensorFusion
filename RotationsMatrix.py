import numpy as np


def zRotation3D(alpha):
    return np.array([   [np.cos(alpha), -np.sin(alpha), 0],
                        [np.sin(alpha), np.cos(alpha),  0],
                        [0              0               1]])

def yRotation3D(beta):
    return np.array([   [np.cos(beta),  0,  np.sin(beta)],
                        [0,             1,  0           ],
                        [-np.sin(beta), 0,  np.cos(beta)]])

def xRotation3D(gamma):
    return np.array([   [1, 0,              0             ],
                        [0, np.cos(gamma),  -np.sin(gamma)],
                        [0, np.sin(gamma),  np.cos(gamma)]])
