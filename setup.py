from setuptools import setup, find_packages  # pragma: no cover

setup(
    name='Harry Parser',
    version='1.0',
    author=[open('AUTHORS.md').read()],  # pragma: no cover
    description='An RSS Feed Reader',
    packages=find_packages(),  # pragma: no cover
    license='MIT License',
    long_description=open('README.md').read(),  # pragma: no cover
    python_requires='>=3.6'
)
