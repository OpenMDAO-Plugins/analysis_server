
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

    from analysis_server import ASMixin

    class MyComp(Component, ASMixin):

        input_var = Float(0, iotype='in')
        output_var = Float(iotype='out')

        def execute(self):
            self.output_var = self.input_var


An example minimal configuration file allowing access to all inputs, outputs,
and remotely accessible single-argument methods (in file ``RemoteComponent.cfg``)::

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
    *: *


The server can be run using the ``-m`` option to the ``python`` command::

    python -m analysis_server.server --address localhost

We're using ``localhost`` as the address here to simplify configuration.
The default is to use the host's network address, which allows remote access,
but requires a ``hosts.allow`` file to be created specifying which hosts
clients may connect from.

When the server starts, it will look in its current directory tree for
configuration files. For each file found it will create a corresponding egg
file (if not already provided).

.. note::

    The server creates component instances from these egg files, not from the
    specified Python file.  So to have changes reflected in the components
    provided to clients either the configuration file must be updated or the
    corresponding egg file must be removed.  Either of these actions will cause
    the egg file to be recreated when the server restarts.

If a configuration file is found in a subdirectory, the path to the file
is used as a component type name prefix.

The server also supports remote publishing of components, so that you can
publish or update a component from anywhere the server may be accessed from.
This is done via the ``publish.py`` tool::

    python -m analysis_server.publish --path RemoteComponent --version 0.1 --file model.py --classname MyComp


Please consult the :ref:`analysis_server_src_label` section for more detail.


=====
Hints
=====

*Variable Configuration*
________________________

:class:`ASMixin` defines :meth:`reinitialize`. If a method of this name is found
by ModelCenter, then updated variable configurations will be automatically
detected upon model reload.  If for some reason you want your component
notified upon ModelCenter reload, you can override this. If you don't have
a definition for :meth:`reinitialize` either by using the mixin class or
defining your own, you will need to delete and re-add your component instance
in order for ModelCenter to detect any variable configuration updates.

*Debugging*
___________

Normally when a component instance is not needed anymore, its server directory
is removed.  If you want these directories to be preserved, set the
environment variable ``OPENMDAO_KEEPDIRS`` to ``1``.

The log files created by the server will have more information in them
if you add ``--debug`` to the server command line.

*Binary Files*
______________

When transferring binary file data back to ModelCenter via a File variable,
it's important that the binary nature be flagged before execution because
ModelCenter will use the binary indicator to alter how the file data is
processed when read back.  If you don't, the data is returned to ModelCenter,
but it will be stored in ``base64`` format.

One way to get the binary indicator set is to initialize the File variable
with a FileRef describing the file (even if the file doesn't exist yet)::

    from openmdao.main.api import Component
    from openmdao.main.datatypes.api import File, FileRef

    class FileComponent(Component):

        file1 = File(FileRef('iso_cp.png', binary=True), iotype='out')
        file2 = File(FileRef('fig_1.png', binary=True), iotype='out')

        def execute(self):
            # Add code which causes the files to be created.
            pass

If you happen to forget to do this and end up with the base64 data, the code
below will decode the file.  Note that due to a ModelCenter quirk (at least as
of version 10), Python's base64 decoder may not consider the ModelCenter file
well-formed.  This code handles that problem::

    import base64
    import sys

    if len(sys.argv) < 3:
        print 'usage: python decode.py encoded-file decoded-file'
        sys.exit(1)

    with open(sys.argv[1], 'r') as inp:
        data = inp.read()

    while data:
        try:
            decoded = base64.b64decode(data)
        except Exception as exc:
            print 'b64decode exception', exc
            print 'dropping %r' % data[-1]
            data = data[:-1]
        else:
            with open(sys.argv[2], 'wb') as out:
                out.write(decoded)
            break

