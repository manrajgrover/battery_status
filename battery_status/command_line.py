import battery_status

def battery_notif():
    battery_status.battery_status()

def set_limit():
    print 'Please enter an integer between 0 and 100'
    x=raw_input()
    battery_status.set_battery_low_limit(x)

def check_status():
    battery_status.battery_check_status()
