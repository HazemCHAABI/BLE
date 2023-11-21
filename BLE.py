# Function to handle connections
def conn_callback(bt_o):
    events = bt_o.events()
    if events & Bluetooth.CLIENT_CONNECTED:
        print("Client connected")
    elif events & Bluetooth.CLIENT_DISCONNECTED:
        print("Client disconnected")

# Register the connection callback
bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_callback)

# Start advertising
bluetooth.advertise(True)

# Define a service and a characteristic
service = bluetooth.service(uuid=b'1234567890123456', isprimary=True)
characteristic = service.characteristic(uuid=b'ab34567890123456', value=5)

# Function to update the characteristic value (this could be sensor data)
def update_characteristic(value):
    characteristic.value(value)
    print("Characteristic value updated:", value)

# Main loop
while True:
    update_characteristic(value=b'{}'.format(time.time()))  # Update with current time as an example
    time.sleep(10)