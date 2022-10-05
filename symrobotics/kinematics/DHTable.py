import sympy as sp
from enum import Enum

from symrobotics.spatial import Transform

class JointType(Enum):
    CONSTANT = 0
    REVOLUTE = 1
    PRISMATIC = 2


class DHTable:

    def __init__(self):
        self.__table: sp.Matrix = sp.zeros(0, 4)
        self.__cache = {}
        self.geometry = []
        self.jointVariables = []

    def __str__(self):
        return sp.pretty(self.__table.evalf())

    def __len__(self):
        return sp.shape(self.__table)[0]

    def __getitem__(self, index):
        return self.__table.row(index)

    def __reset(self):
        self.__table: sp.Matrix = sp.zeros(0, 4)
        self.geometry = []
        self.jointVariables = []

    @property
    def table(self):
        return self.__table

    def add_revolute(self, *, a=0, alpha=0, d=0, offset=0):
        row_index = sp.shape(self.__table)[0]
        theta = sp.symbols(f"\\theta_{row_index}")

        row = [a, alpha, d, theta + sp.sympify(offset)]

        # convert each entry to a type which sympy can actually use
        for index,entry in enumerate(row):
            row[index] = sp.sympify(entry)

        self.__table = self.__table.row_insert(
            sp.shape(self.__table)[0], sp.Matrix([row]))
        self.jointVariables.append(theta)
        self.geometry.append(JointType.REVOLUTE)

    def add_prismatic(self, *, a=0, alpha=0, theta=0, offset=0):
        row_index = sp.shape(self.__table)[0]
        d = sp.symbols(f"d_{row_index}")

        row = [a, alpha, d + sp.sympify(offset), theta]

        # convert each entry to a type which sympy can actually use
        for index,entry in enumerate(row):
            row[index] = sp.sympify(entry)

        self.__table = self.__table.row_insert(
            sp.shape(self.__table)[0], sp.Matrix([row]))
        self.jointVariables.append(d)
        self.geometry.append(JointType.PRISMATIC)

    def add_constant(self, *, a=0, alpha=0, d=0, theta=0):
        row = [a, alpha, d, theta]

        for index,entry in enumerate(row):
            row[index] = sp.sympify(entry)

        self.__table = self.__table.row_insert(
            sp.shape(self.__table)[0], sp.Matrix([row]))
        self.geometry.append(JointType.CONSTANT)


    def compute(self, fromIndex, untilIndex) -> Transform:
        result = Transform.eye()
        if fromIndex in self.__cache:
            if untilIndex in self.__cache.get(fromIndex).keys():
                return self.__cache[fromIndex][untilIndex]
        else:
            self.__cache[fromIndex] = dict()
        for row in range(fromIndex, untilIndex):
            result = result*self.compute_row(row)
        result = sp.trigsimp(result)
        self.__cache[fromIndex][untilIndex] = result
        return result

    def compute_all(self) -> Transform:
        return self.compute(0, sp.shape(self.__table)[0])

    def compute_row(self, index) -> Transform:
        row = self.__table.row(index)
        a = row[0]
        alpha = row[1]
        d = row[2]
        theta = row[3]
        return Transform([
            [sp.cos(theta), -sp.sin(theta)*sp.cos(alpha),
             sp.sin(theta)*sp.sin(alpha), a*sp.cos(theta)],
            [sp.sin(theta), sp.cos(theta)*sp.cos(alpha), -
             sp.cos(theta)*sp.sin(alpha), a*sp.sin(theta)],
            [0, sp.sin(alpha), sp.cos(alpha), d],
            [0, 0, 0, 1]
        ])
