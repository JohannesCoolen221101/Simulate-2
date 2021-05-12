import ubinascii
import time
from network import Bluetooth
bluetooth = Bluetooth()

def findDevices():
    bluetooth.start_scan(20)
    while bluetooth.isscanning():
        adv = bluetooth.get_adv()
        if adv:
            # try to get the complete name
            print(bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL))

            mfg_data = bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_MANUFACTURER_DATA)

            if mfg_data:
                print((mfg_data))
        time.sleep(2)

findDevices()
