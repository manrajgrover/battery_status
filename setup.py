from setuptools import setup

setup(name='battery_status',
      version='0.0.9',
      description='Battery Status Notifier',
      long_description='Check your battery status and add a notifier on Windows',
      keywords='battery status notifier windows check battery status python',
      url='https://github.com/ManrajGrover/battery_status',
      author='Manraj Singh',
      author_email='manrajsinghgrover@gmail.com',
      license='MIT',
      entry_points = {
          'console_scripts': [
               'check_battery_status=battery_status.command_line:check_status',
               'start_battery_notifier=battery_status.command_line:battery_notif',
          ],
      },
      packages=['battery_status'],
      install_requires=[
            'wmi',
      ],
      zip_safe=False)
