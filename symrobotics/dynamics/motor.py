import control

class Motor:

    def __init__(self,jm,dm,kt):
        self._jm = jm
        self._dm = dm
        self._kt = kt

        self._tf = control.TransferFunction([1], [self._jm, self._dm])

    def to_tf(self):
        return self._tf

    @property
    def jm(self):
        return self._jm
    @property
    def dm(self):
        return self._dm
    @property
    def kt(self):
        return self._kt

class MotorBuilder:

    def  __init__(self):
        self._reset()

    def _reset(self):
        self._parameters = {
            "jm": None,
            "dm": None,
            "kt": None,
            "n": None
        }

    def build(self):
        jm = self._parameters["jm"]
        dm = self._parameters["dm"]
        kt = self._parameters["kt"]
        if None in (jm,dm,kt):
            raise ValueError
        self._reset()
        return Motor(jm,dm,kt)

    def setInertia(self, value):
        self._parameters["jm"] = float(value)
        return self
    def setFriction(self, value):
        self._parameters["dm"] = float(value)
        return self
    def setTrqConst(self, value):
        self._parameters["kt"] = float(value)
        return self

def motor(jm,dm,kt):
    return Motor(jm,dm,kt)
