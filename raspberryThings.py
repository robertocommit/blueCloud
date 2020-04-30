import bluetooth
import requests
import time

hc_06 = 'RASPBERRY_BLUETOOTH_ADDRESS'

port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((hc_06, port))

url = 'GOOGLE_CLOUD_FUNCTION_URL'

while True:
    try:
        data = sock.recv(4096)
        temperature = data.splitlines()[0]
        print('Setting temperature and receiving status...')
        response = requests.get(url + str(temperature))
        status = response.text
        sock.send(status)
        print('TEMP: ' + str(temperature))
        print('STATUS: ' + status)
        print('\n\n')
        time.sleep(5)
    except:
        time.sleep(5)
