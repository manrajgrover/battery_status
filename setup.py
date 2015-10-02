from setuptools import setup

setup(name='battery_status',
      version='0.0.1',
      description='Battery Status Notifier',
      long_description='Check your battery status, add a notifier, set notification percentage on Windows',
      keywords='battery status notifier windows check battery status python',
      url='https://github.com/ManrajGrover/battery_status',
      author='Manraj Singh',
      author_email='manrajsinghgrover@gmail.com',
      license='MIT',
      packages=['battery_status'],
      install_requires=[
            'wmi',
            'time',
            'winsound'
      ],
      zip_safe=False)
