from multiprocessing.sharedctypes import Value
import sympy as sp
from .angles import rotm2eul, rotm2eul_s
from .rotm import RotationMatrix

class Transform(sp.Matrix, RotationMatrix):

    def __new__(cls, arguments):
        t = super(Transform, cls).__new__(cls, arguments)
        if t.shape == (4,4):
            return t
        raise ValueError

    @staticmethod
    def eye():
        return Transform(sp.eye(4))

    @property
    def x(self):
        return self[0, 3]
    @property
    def y(self):
        return self[1, 3]
    @property
    def z(self):
        return self[2, 3]

    @property
    def rotm(self):
        return RotationMatrix(self[0:3, 0:3])

    @property
    def position(self):
        return self[0:3, 3]
