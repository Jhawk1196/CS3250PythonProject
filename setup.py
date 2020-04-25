from distutils.core import setup  # pragma: no cover

setup(
    name='Harry Parser',
    version='0.9',
    packages=[open('requirements.txt').read()],  # pragma: no cover
    license='MIT License',
    long_description=open('README.txt').read(),  # pragma: no cover
)
