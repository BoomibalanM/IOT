from wifi_connect import *
from maotor import *
from data_read import *

ssid = 'Sethu'
password = 'Sethu@542'
status = wi_connect(ssid,password)
rf_id = rf_id_find()

if status and rf_id:
    # x = requests.get('https://www.google.com')
    # print(x.status_code)
    url = 'http://iotdemo.pythonanywhere.com/rfid_login'
    # myinp = {'num1': 9,'num2': 55555
    #             }
    inpu ={'num1':rf_id}
    w = requests.get(url, json = inpu)
    print(w.text)
    if w == 1:
        setServoCycle()
        url = 'http://iotdemo.pythonanywhere.com/updateproducts'
        print("user available")
    else:
        print("user unavailable")