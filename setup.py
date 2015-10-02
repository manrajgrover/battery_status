from setuptools import setup

setup(name='battery_status',
      version='0.0.8',
      description='Battery Status Notifier',
      long_description='Check your battery status and add a notifier on Windows',
      keywords='battery status notifier windows check battery status python',
      url='https://github.com/ManrajGrover/battery_status',
      author='Manraj Singh',
      author_email='manrajsinghgrover@gmail.com',
      license='MIT',
      packages=['battery_status'],
      install_requires=[
            'wmi',
      ],
      zip_safe=False)
