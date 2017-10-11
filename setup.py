from distutils.core import setup

setup(
  name='django-mbills',
  packages=['mbills', 'mbills.migrations'],
  version='0.1.6',
  description='Django implementation of the Hal MBills APIs.',
  author='Boris Savic',
  author_email='boris70@gmail.com',
  url='https://github.com/boris-savic/django-mbills',
  keywords=['mbills', 'halcom', 'django' ],
  classifiers=[],
  install_requires=[
        'python_mbills>=0.1.3',
    ]
)