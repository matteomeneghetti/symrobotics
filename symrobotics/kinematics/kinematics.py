from .DHTable import DHTable, JointType
from symrobotics.spatial.angles import rotm2eul_s
from symrobotics.spatial import Transform
import sympy as sp

class Kinematics:

    def __init__(self, DH: DHTable, default_angles="xyz"):
        self.DH = DH
        self._default_angles = default_angles

    def fkine(self) -> Transform:
        return self.DH.compute_all()

    def geometric_jacobian(self) -> sp.Matrix:
        fk = self.fkine()
        ee_position = fk.position
        j = sp.zeros(2, 0)
        for i in range(len(self.DH)):
            T0_i = self.DH.compute(0, i)
            z0_i = T0_i.rotz
            if self.DH.geometry[i] == JointType.CONSTANT:
                continue
            elif self.DH.geometry[i] == JointType.PRISMATIC:
                j = j.col_insert(sp.shape(j)[1], sp.Matrix([z0_i, sp.zeros(3, 1)]))
            else:
                p0_i = T0_i.position
                result = sp.trigsimp(z0_i.cross(ee_position - p0_i))
                j = j.col_insert(sp.shape(j)[1], sp.Matrix([result, z0_i]))
        return j

    def analitical_jacobian(self) -> sp.Matrix:
        fk = self.fkine()
        x = fk.x
        y = fk.y
        z = fk.z
        phi, theta, psi = rotm2eul_s(fk.rotm, self._default_angles)
        x_vec = []
        y_vec = []
        z_vec = []
        phi_vec = []
        theta_vec = []
        psi_vec = []
        for i in range(len(self.DH.jointVariables)):
            x_vec.append(sp.trigsimp(sp.diff(x, self.DH.jointVariables[i])))
            y_vec.append(sp.trigsimp(sp.diff(y, self.DH.jointVariables[i])))
            z_vec.append(sp.trigsimp(sp.diff(z, self.DH.jointVariables[i])))
            phi_vec.append(sp.trigsimp(sp.diff(phi, self.DH.jointVariables[i])))
            theta_vec.append(sp.trigsimp(sp.diff(theta, self.DH.jointVariables[i])))
            psi_vec.append(sp.trigsimp(sp.diff(psi, self.DH.jointVariables[i])))
        return sp.Matrix([x_vec, y_vec, z_vec, phi_vec, theta_vec, psi_vec])

    def evaluate(self, expression, values):
        return expression.subs(list(zip(self.DH.jointVariables, values)))
