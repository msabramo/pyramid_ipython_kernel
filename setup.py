from setuptools import setup


setup(
    name='pyramid_ipython_kernel',
    description='Start an IPython kernel in Pyramid app; connect to it to introspect',
    long_description=open('README.rst').read().strip(),
    version='0.0.0',
    author='Marc Abramowitz',
    author_email='marc@marc-abramowitz.com',
    license='MIT',
    url='https://github.com/msabramo/pyramid_ipython_kernel',
    py_modules=['pyramid_ipython_kernel'],
    zip_safe=False,
    install_requires=[
        'IPython',
        'pyzmq>=2.1.11',
        'pyramid',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
    ],
)
