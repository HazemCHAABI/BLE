from network import Bluetooth
import time
import pycom



# Initialize Bluetooth
bluetooth = Bluetooth()
bluetooth.set_advertisement(name='Pycom_TEST', service_uuid=b'1234567890123457')
service = bluetooth.service(uuid=b'1234567890123457', isprimary=True)

# Callback function for BLE writes
def on_ble_write(event, char):
    received_data = char  # Get the data written to the characteristic
    print("Data received via BLE:", received_data)
    # Here you can process the received data

# Create a characteristic with write property
data_characteristic = service.characteristic(uuid=b'ab34567890123457', properties=Bluetooth.PROP_WRITE, value=5)

# Set up the callback for when data is written to the characteristic
data_characteristic.callback(trigger=Bluetooth.CHAR_WRITE_EVENT, handler=on_ble_write)

# Main loop
while True:
    bluetooth.advertise(True)
    time.sleep(5)
