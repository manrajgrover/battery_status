import wmi
import time
import winsound

setBatteryLowLimit = 20

def battery_low():
    for i in range(1, 10):
        winsound.Beep(i * 100, 200)

def battery_check():
    battery = wmi.WMI().Win32_Battery()[0]
    print 'Current battery status is ' + str(battery.EstimatedChargeRemaining)'%'
    print 'You will be notified when battery is below '+str(setBatteryLowLimit)+'%'
    while(1):
        battery = wmi.WMI().Win32_Battery()[0]
        if battery.EstimatedChargeRemaining < setBatteryLowLimit:
            battery_low()
            print 'Battery below ' + str(setBatteryLowLimit) + '%! Connect charger!'
            break
        time.sleep(120)

def set_limit(x):
    if isinstance(x,int) and x>=0 and x <=100:
        setBatteryLowLimit = x
    else:
        print 'Please enter an integer between 0 and 100'

def check_status():
    battery = wmi.WMI().Win32_Battery()[0]
    print 'Your current battery status is ' + str(battery.EstimatedChargeRemaining)'%'
