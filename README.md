# battery_status
A Python Module for Windows to notify when battery is below certain set percentage

## Dependencies
[Windows Management Instrumentation module(WMI)](https://pypi.python.org/pypi/WMI/)

## How to install:
You can install it using pip. Use command `pip install battery_status` in terminal.
Alternatively you can use `easy_install battery_status` to install it.

## How to use:
You can import it in your Python Script and run. But why would you want to do that.
Since this is a background application, you can run it in Bash using commands `check_battery_status` for checking battery percentage and `start_battery_notifier` for getting notification on 20 percentage or less. You will hear sound as notification.
