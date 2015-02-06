import logging
import threading

import IPython
import mock


logger = logging.getLogger(__name__)


class IPythonKernelThread(threading.Thread):
    config = None

    def run(self):
        namespace = {
            'config': self.config,
            'registry': self.config.registry,
            'settings': self.config.registry.settings,
        }

        with mock.patch('signal.signal'):
            IPython.embed_kernel(local_ns=namespace)


def includeme(config):
    """Function that gets called when client code calls config.include"""
    config.registry.ipython_thread = IPythonKernelThread(name='IPython kernel')
    config.registry.ipython_thread.config = config
    config.registry.ipython_thread.daemon = True

    logger.info("pyramid_ipython_kernel: Starting an IPython kernel")
    config.registry.ipython_thread.start()
    logger.info("pyramid_ipython_kernel: Started an IPython kernel: %r",
                config.registry.ipython_thread)
