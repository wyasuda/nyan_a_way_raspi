import requests

tmpstr = "value1=Detected!"
requests.post("http://maker.ifttt.com/trigger/nyan_a_way_trig1/with/key/YOUR_KEY_IS?"+tmpstr)
