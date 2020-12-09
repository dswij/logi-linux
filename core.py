import usb
import binascii
import json

def connect(idVendor, idProduct):
    dev = usb.core.find(idVendor=idVendor, idProduct=idProduct)
    if not dev:
        raise ValueError('The device with idVendor {} and idProduct {} is not found'.format(idVendor, idProduct))
    return dev

def send(bmRequestType, bmRequest, wValue, wIndex, data):
    device.ctrl_transfer(bmRequestType, bmRequest, wValue, wIndex)

def drop_resource(dev):
    usb.util.dispose_resources(dev)

def load_data(fileName) -> dict():
    try:
        with open(fileName, 'r') as fp:
            config_data = json.load(fp)
    except:
        print("No config found, creating a default dict")
        config_data = {
            'g102': {
                'bmRequestType': '0x21',
                'bmRequest': '0x9',
                'wValue': '0x210',
                'wIndex': '0x1'
            },
            'g304': {
                'bm_request_type': '0x21',
                'bm_request': '0x9',
                'w_value': '0x210',
                'w_index': '0x1'
                'vendor_id': '0x046d',
                'product_id': '0xc084',
            }
        }
    return config_data

def save_data(config_data, fileName):
    with open(fileName, 'w') as fp:
        json.dump(config_data, fp)

def main():
    file_namej = "config.json"
    config_data = load_data(fileName)
    prod = "g304"
    configs = config_data[prod]

if __name__ == "__main__":
    main()
