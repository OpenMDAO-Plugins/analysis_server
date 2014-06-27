import logging

from openmdao.main.api import Component
from openmdao.main.rbac import rbac


class ASComponent(Component):
    """ Base class for AnalysisServer components. """

    @rbac(('owner', 'user'))
    def reinitialize(self):
        """ To be called when the client connects. """
        self._logger.critical('reinitialize() called.')

