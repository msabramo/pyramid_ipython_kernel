pyramid_ipython_kernel
=================================

Embed an IPython_ kernel inside your Pyramid_ app, so that you can connect to it with an IPython client and introspect.

- Configure:

  .. code-block:: ini

      pyramid.includes =
          pyramid_ipython_kernel

- Run your Pyramid app::

    $ pserve development.ini
    ...
    2015-02-06 13:42:57,181 INFO  [MainThread][pyramid_ipython_kernel.includeme][pyramid_ipython_kernel.py +41] pyramid_ipython_kernel: Starting an IPython kernel
    2015-02-06 13:42:57,183 INFO  [MainThread][pyramid_ipython_kernel.includeme][pyramid_ipython_kernel.py +44] pyramid_ipython_kernel: Started an IPython kernel: <IPythonKernelThread(IPython kernel, started daemon 4438888448)>
    NOTE: When using the `ipython kernel` entry point, Ctrl-C will not work.

    To exit, you will have to explicitly quit this process, by either sending
    "quit" from a client, or using Ctrl-\ in UNIX-like environments.

    To read more about this, see https://github.com/ipython/ipython/issues/2049

    To connect another client to this kernel, use:
        --existing kernel-48054.json
    ...

- Profit::

    $ ipython console --existing
    Python 2.7.9 (v2.7.9:648dcafa7e5f, Dec 10 2014, 10:10:46)
    Type "copyright", "credits" or "license" for more information.

    IPython 2.0.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]: # Why does this start and [1] and then jump to last used number?

    In [10]: config
    Out[10]: <pyramid.config.Configurator at 0x107e0ded0>

    In [11]: config.registry
    Out[11]: <Registry kotti>

    In [12]: settings['kotti.request_factory']
    Out[12]: [kotti.request.Request]

See also
--------

- https://github.com/msabramo/pyramid_ssh_crochet
- https://github.com/ipython/ipython/issues/4032


.. _IPython: http://ipython.org/
.. _Pyramid: http://www.trypyramid.com/
