import sympy as sp
from .angles import rotm2eul, rotm2eul_s

class RotationMatrix(sp.ImmutableDenseMatrix):
    def __new__(cls, *arguments):
        matrix = sp.eye(3)
        if len(arguments) > 0:
            matrix = arguments[0]
        return super(RotationMatrix, cls).__new__(cls, matrix)

    @staticmethod
    def identity():
        return RotationMatrix()
    def from_eulers(angles, sequence="xyz"):
        raise NotImplementedError()

    @property
    def rotx(self):
        return self[0:3, 0]
    @property
    def roty(self):
        return self[0:3, 1]
    @property
    def rotz(self):
        return self[0:3, 2]

    def eulers(self, *, sequence="xyz", values=tuple(), degrees=False):
        if len(values) > 0:
            return rotm2eul(self, sequence)
        else:
            return rotm2eul_s(self, sequence)
