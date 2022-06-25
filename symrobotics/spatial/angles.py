import sympy as sp
from enum import Enum

class RotationSequence:
    pass

def rotm2eul(rotm, sequence='XYZ'):
    phi = None      # First angle of the sequence
    theta = None    # Second angle of the sequence
    psi = None      # Third angle of the sequence
    sequence = sequence.lower()

    if sequence == 'xyz':
        if rotm[0, 2] < 1:
            if rotm[0, 2] > -1:
                phi = sp.atan2(-rotm[1,2], rotm[2,2])
                theta = sp.asin(rotm[0,2])
                psi = sp.atan2(-rotm[0,1], rotm[0,0])
            else:
                phi = -sp.atan2(rotm[1,0], rotm[1,1])
                theta = -sp.pi/2
                psi = 0
        else:
            phi = sp.atan2(rotm[1,0], rotm[1,1])
            theta = sp.pi/2
            psi = 0

    elif sequence == 'xzy':
        if rotm[0,1] < 1:
            if rotm[0,1] > -1:
                phi = sp.atan2(rotm[2,1], rotm[1,1])
                theta = sp.asin(-rotm[0,1])
                psi = sp.atan2(rotm[0,2], rotm[0,0])
            else:
                phi = -sp.atan2(-rotm[2,0], rotm[2,2])
                theta = sp.pi/2
                psi = 0
        else:
            phi = sp.atan2(-rotm[2,0], rotm[2,2])
            theta = -sp.pi/2
            psi = 0

    elif sequence == 'yxz':
        if rotm[1,2] < 1:
            if rotm[1,2] > -1:
                phi = sp.atan2(rotm[0,2], rotm[2,2])
                theta = sp.asin(-rotm[1,2])
                psi = sp.atan2(rotm[1,0], rotm[1,1])
            else:
                phi = -sp.atan2(-rotm[0,1], rotm[0,0])
                theta = sp.pi/2
                psi = 0
        else:
            phi = sp.atan2(-rotm[0,1], rotm[0,0])
            theta = -sp.pi/2
            psi = 0

    elif sequence == 'yzx':
        if rotm[1,0] < 1:
            if rotm[1,0] > -1:
                phi = sp.atan2(-rotm[2,0], rotm[0,0])
                theta = sp.asin(rotm[1,0])
                psi =sp.atan2(-rotm[1,2], rotm[1,1])
            else:
                phi = -sp.atan2(-rotm[2,1], rotm[2,2])
                theta = -sp.pi/2
                psi = 0
        else:
            phi = sp.atan2(-rotm[2,1], rotm[2,2])
            theta = sp.pi/2
            psi = 0

    elif sequence == 'zxy':
        if rotm[2,1] < 1:
            if rotm[2,1] > -1:
                phi = sp.atan2(-rotm[0,1], rotm[1,1])
                theta = sp.asin(rotm[2,1])
                psi = sp.atan2(-rotm[2,0], rotm[2,2])
            else:
                phi = -sp.atan2(rotm[0,2], rotm[0,0])
                theta = -sp.pi/2
                psi = 0
        else:
            phi = sp.atan2(rotm[0,2], rotm[0,0])
            theta = sp.pi/2
            psi = 0

    elif sequence == 'zyx':
        if rotm[2,0] < 1:
            if rotm[2,0] > -1:
                phi = sp.atan2(rotm[1,0], rotm[0,0])
                theta = sp.asin(-rotm[0,2])
                psi = sp.atan2(rotm[2,1], rotm[2,2])
            else:
                phi = -sp.atan2(-rotm[1,2], rotm[1,1])
                theta = sp.pi/2
                psi = 0
        else:
            phi = sp.atan2(-rotm[1,2], rotm[1,1])
            theta = -sp.pi/2
            psi = 0

    elif sequence == 'xyx':
        if rotm[0,0] < 1:
            if rotm[0,0] > -1:
                phi = sp.atan2(rotm[1,0], rotm[0,0])
                theta = sp.asin(-rotm[0,2])
                psi = sp.atan2(rotm[2,1], rotm[2,2])
            else:
                phi = -sp.atan2(-rotm[1,2], rotm[1,1])
                theta = sp.pi/2
                psi = 0
        else:
            phi = sp.atan2(-rotm[1,2], rotm[1,1])
            theta = -sp.pi/2
            psi = 0
    elif sequence == 'zyz':
        phi = sp.atan2(rotm[1,2], rotm[0,2])
        theta = sp.atan2(sp.sqrt(rotm[0,2]**2 + rotm[1,2]**2), rotm[2,2])
        psi = sp.atan2(rotm[2,1], -rotm[2,0])
    else:
        raise ValueError(f"No rotation sequence matched {sequence.upper()}")
    return (phi, theta, psi)

def rotm2eul_s(rotm, sequence='XYZ'):
    phi = None
    theta = None
    psi = None
    sequence = sequence.lower()
    if sequence == 'zyx':
        phi = sp.atan2(rotm[2,1], rotm[2,2])
        theta = sp.asin(-rotm[0,2])
        psi = sp.atan2(rotm[1,0], rotm[0,0])
    elif sequence == 'xyz':
        phi = sp.atan2(-rotm[1,2], rotm[2,2])
        theta = sp.asin(rotm[0,2])
        psi = sp.atan2(-rotm[0,1], rotm[0,0])
    elif sequence == 'zyz':
        phi = sp.atan2(rotm[1,2], rotm[0,2])
        theta = sp.atan2(sp.sqrt(rotm[0,2]**2 + rotm[1,2]**2), rotm[2,2])
        psi = sp.atan2(rotm[2,1], -rotm[2,0])
    else:
        raise ValueError(f"No rotation sequence matched {sequence.upper()}")
    return (phi, theta, psi)