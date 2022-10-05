import control

class Motor:

    def __init__(self):
        self._reset()

    def _reset(self):
        self._jm = 0
        self._dm = 0
        self._kt = 0
        self._n = 0

    def to_tf(self, dt=0):
        return control.TransferFunction([1], [self._jm, self._dm, 0], dt)

    @property
    def jm(self):
        return self._jm
    @jm.setter
    def jm(self, value):
        self._jm = float(value)

    @property
    def dm(self):
        return self._dm
    @dm.setter
    def dm(self, value):
        self._dm = float(value)

    @property
    def kt(self):
        return self._kt
    @kt.setter
    def kt(self, value):
        self._kt = float(value)

class MotorBuilder:

    def  __init__(self):
        self._tmp = Motor()

    def build(self):
        motor = self._tmp
        self._tmp = Motor()
        return motor

    def setInertia(self, value):
        self._tmp.jm = float(value)
        return self
    def setFriction(self, value):
        self._tmp.dm = float(value)
        return self
    def setGearRatio(self, value):
        self._tmp.n = float(value)
        return self

    def setTrqConst(self, value):
        self._tmp.kt = float(value)
        return self
