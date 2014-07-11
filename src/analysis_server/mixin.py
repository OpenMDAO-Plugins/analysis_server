import logging

from openmdao.main.rbac import rbac


class ASMixin(object):
    """ Mixin class for AnalysisServer components. """

    @rbac(('owner', 'user'))
    def reinitialize(self):
        """
        Special method which causes ModelCenter to update its definition
        for this component.
        """
        self._logger.critical('reinitialize() called.')

