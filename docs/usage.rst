
===========
Usage Guide
===========

The ``analysis_server`` package provides both client and server sides of
communication compatible with Phoenix Integration's Analysis Server.

As a client, an instance of :class:`factory.ASFactory` must be created,
referring to the host and port of the remote AnalysisServer to connect to.
This factory is then registered with OpenMDAO via
:meth:`openmdao.main.factorymanager.register_class_factory`. Subsequent
:meth:`openmdao.main.factorymanager.create` calls referring to component types
supported by the AnalysisServer will return a proxy component populated with
proxy variables corresponding to the exposed interface of the remote component.

For example, to use a ``RemoteComponent``::

    from openmdao.main.factorymanager import register_class_factory, create
    from analysis_server import ASFactory

    register_class_factory(ASFactory())

    comp = create('RemoteComponent')
    comp.input_var = 42
    comp.run()
    print 'result:', comp.output_var


When this package is used as a server, ModelCenter can access OpenMDAO
components. To do this ``server.py`` is started in a directory containing
component configuration files (files ending in ``.cfg``) and corresponding
component Python or egg files. The configuration files specify what part of
the component interface is to be exposed.

First, a trivial component definition with the above ``RemoteComponent``
interface (in file ``model.py``)::

    from openmdao.main.api import Component
    from openmdao.lib.datatypes.api import Float

    class MyComp(Component):

        input_var = Float(0, iotype='in')
        output_var = Float(iotype='out')

        def execute(self):
            self.output_var = self.input_var


An example minimal configuration file allowing access to all inputs
and outputs, but no methods (in file ``RemoteComponent.cfg``)::

    [Description]
    version: 0.1

    [Python]
    filename: model.py
    classname: MyComp

    [Inputs]
    *: *

    [Outputs]
    *: *

    [Methods]


The server can be run using the ``-m`` option to the ``python`` command::

    python -m analysis_server.server --address localhost

We're using ``localhost`` as the address here to simplify configuration.
The default is to use the host's network address, which allows remote access,
but requires a ``hosts.allow`` file to be created specifying which hosts
clients may connect from.

When the server starts, it will look in its current directory tree for
configuration files. For each file found it will create a corresponding egg
file (if not already provided).  Note that the server creates component
instances from these egg files, not from the specified Python file.
So to have changes reflected in the components provided to clients either the
configuration file must be updated or the corresponding egg file must be
removed.  Either of these actions will cause the egg file to be recreated when
the server restarts.

If a configuration file is found in a subdirectory, the path to the file
is used as a component type name prefix.

The server also supports remote publishing of components, so that you can
publish or update a component from anywhere the server may be accessed from.
This is done via the ``publish.py`` tool::

    python -m analysis_server.publish --path RemoteComponent --version 0.1 --file model.py --classname MyComp


Please consult the :ref:`analysis_server_src_label` section for more detail.

