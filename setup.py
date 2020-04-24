from distutils.core import setup

setup(
    name='Harry Parser',
    version='0.1',
    packages=[open('requirements.txt').read()],
    license='MIT License',
    long_description=open('README.txt').read(),
)
