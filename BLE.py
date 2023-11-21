from network import Bluetooth
import time

# Initialize Bluetooth
# This creates a Bluetooth object that will allow us to interact with BLE features.
bluetooth = Bluetooth()

# Set up the device to advertise itself over Bluetooth
# 'PycomBLE' is the name that will be broadcasted, and '1234567890123456' is the UUID for the service.
bluetooth.set_advertisement(name='PycomBLE', service_uuid=b'1234567890123456')

# Define a function to handle Bluetooth connection events.
# This function is called whenever a client connects to or disconnects from the device.
def conn_callback(bt_o):
    events = bt_o.events()
    if events & Bluetooth.CLIENT_CONNECTED:
        print("Client connected")  # A client has connected to the device.
    elif events & Bluetooth.CLIENT_DISCONNECTED:
        print("Client disconnected")  # A client has disconnected from the device.

# Register the above function as a callback for client connect/disconnect events.
bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_callback)

# Start Bluetooth advertisement
# This makes the device discoverable by BLE clients.
bluetooth.advertise(True)

# Define a BLE service and a characteristic within that service.
# UUIDs are used to uniquely identify both.
service = bluetooth.service(uuid=b'1234567890123456', isprimary=True)
characteristic = service.characteristic(uuid=b'ab34567890123456', value=5)

# Define a function to update the value of the BLE characteristic.
# This could represent updating the characteristic with sensor data or other information.
def update_characteristic(value):
    characteristic.value(value)  # Set the new value of the characteristic.
    print("Characteristic value updated:", value)

# Main loop
# This continually updates the characteristic value and then waits for a period of time.
while True:
    # Update the characteristic with the current time.
    # The time is encoded as bytes to be compatible with BLE data formats.
    update_characteristic(value=b'{}'.format(time.time()))
    time.sleep(10)  # Wait for 10 seconds before updating again.
