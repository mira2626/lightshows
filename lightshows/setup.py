from setuptools import setup, find_packages

setup(
    name='lightshows',
    version='0.1.0',
    description='take home coding test - LSEG Predictive Analytics',
    author='Michael Raptakis',
    packages=['lightshows'],
    install_requires = [
        'numpy>=1.14.5'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
#packages=find_packages(include=['exampleproject', 'exampleproject.*'])
)