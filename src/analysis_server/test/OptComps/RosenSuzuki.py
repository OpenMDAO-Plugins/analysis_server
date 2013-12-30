from openmdao.main.api import Component
from openmdao.main.datatypes.api import Array, Float


class RosenSuzuki(Component):
    """ From the CONMIN User's Manual:
    EXAMPLE 1 - CONSTRAINED ROSEN-SUZUKI FUNCTION. NO GRADIENT INFORMATION.

         MINIMIZE OBJ = X(1)**2 - 5*X(1) + X(2)**2 - 5*X(2) +
                        2*X(3)**2 - 21*X(3) + X(4)**2 + 7*X(4) + 50

         Subject to:

              G(1) = X(1)**2 + X(1) + X(2)**2 - X(2) +
                     X(3)**2 + X(3) + X(4)**2 - X(4) - 8   .LE.0

              G(2) = X(1)**2 - X(1) + 2*X(2)**2 + X(3)**2 +
                     2*X(4)**2 - X(4) - 10                  .LE.0

              G(3) = 2*X(1)**2 + 2*X(1) + X(2)**2 - X(2) +
                     X(3)**2 - X(4) - 5                     .LE.0

    This problem is solved beginning with an initial X-vector of
         X = (1.0, 1.0, 1.0, 1.0)
    The optimum design is known to be
         OBJ = 6.000
    and the corresponding X-vector is
         X = (0.0, 1.0, 2.0, -1.0)
    """

    x = Array([1., 1., 1., 1.], iotype='in', low=-10, high=99)
    g = Array([1., 1., 1.], iotype='out')
    result = Float(iotype='out')

    def execute(self):
        """calculate the new objective value"""
        x = self.x

        self.result = (x[0]**2 - 5.*x[0] + x[1]**2 - 5.*x[1] +
                       2.*x[2]**2 - 21.*x[2] + x[3]**2 + 7.*x[3] + 50)

        self.g[0] = (x[0]**2 + x[0] + x[1]**2 - x[1] +
                     x[2]**2 + x[2] + x[3]**2 - x[3] - 8)
        self.g[1] = (x[0]**2 - x[0] + 2*x[1]**2 + x[2]**2 +
                     2*x[3]**2 - x[3] - 10)
        self.g[2] = (2*x[0]**2 + 2*x[0] + x[1]**2 - x[1] +
                     x[2]**2 - x[3] - 5)

