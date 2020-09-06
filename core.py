import usb.core
import usb.util
import binascii
import json

def connect(idVendor, idProduct):
    dev = usb.core.find(idVendor=idVendor, idProduct=idProduct)
    if not dev: 
        raise ValueError('The device with idVendor {} and idProduct {} is not found'.format(idVendor, idProduct))
    return dev

def send(bmRequestType, bmRequest, wValue, wIndex, data):
    device.ctrl_transfer(bmRequestType, bmRequest, wValue, wIndex)

def dropResource(dev):
    usb.util.dispose_resources(dev)

def loadData(fileName) -> dict():
    try:
        with open(fileName, 'r') as fp:
            config_data = json.load(fp)
    except:
        print("No config found, creating a default dict")
        config_data = {
            'g102': {
                'bmRequestType': '0x21'
                'bmRequest': '0x9'
                'wValue': '0x210'
                'wIndex': '0x1'
            }
        }
    return config_data

def saveData(config_data, fileName):
    with open(fileName, 'w') as fp:
        json.dump(config_data, fp)

if __name__ == "__main__":
    main()

def main():
    fileName = "config.json"
    config_data = loadData(fileName)
    prod = "g102"
    configs = config_data[prod]
