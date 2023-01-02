from setuptools import setup

setup(
   name='datapack',
   version='0.0.1',
   author='Luis Abaitua',
   author_email='labaitua001@ikasle.ehu.eus',
   packages=['datapack', 'datpack.test'],
   url='Indicar una URL para el paquete...',
   license='LICENSE.txt',
   description='This package includes some basic functions to work with datsets',
   long_description=open('README.txt').read(),
   tests_require=['pytest'],
   install_requires=[
      "matplotlib >= 3.1.1",
      "numpy >=1.17.2"
   ],
)
