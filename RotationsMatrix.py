import numpy as np


def zRotation3D(alpha, degrees=False):
    if degrees:
        alpha = alpha * np.pi / 180

    return np.array([   [np.cos(alpha), -np.sin(alpha), 0],
                        [np.sin(alpha), np.cos(alpha),  0],
                        [0,             0,              1]],
                        dtype=np.float32)

def yRotation3D(beta, degrees=False):
    if degrees:
        beta = beta * np.pi / 180

    return np.array([   [np.cos(beta),  0,  np.sin(beta)],
                        [0,             1,  0           ],
                        [-np.sin(beta), 0,  np.cos(beta)]],
                        dtype=np.float32)

def xRotation3D(gamma, degrees=False):
    if degrees:
        gamma = gamma * np.pi / 180

    return np.array([   [1, 0,              0             ],
                        [0, np.cos(gamma),  -np.sin(gamma)],
                        [0, np.sin(gamma),  np.cos(gamma)]],
                        dtype=np.float32)

def TranslationMat3D(x, y, z):
    return np.array([[x, y, z]], dtype=np.float32)

def TransformationMatrix3D(rot, tran):
    mat = np.eye(4, 4, dtype=np.float32)

    mat[0:3, 0:3] = rot
    mat[0:3, 3] = tran

    return mat
