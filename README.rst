pyramid_ipython_kernel
=================================

- Configure:

  .. code-block:: ini

      pyramid.includes =
          pyramid_ipython_kernel

- Run your Pyramid app::

    $ pserve development.ini

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
