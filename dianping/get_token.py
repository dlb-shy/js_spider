import base64
import time
import zlib

shop_id = "l8H4I0MDsSVbgnhr"
sign_str = '"cityId=2&order=latest&shopId=' + shop_id + '&shopType=10"'
sign = base64.b64encode(zlib.compress(sign_str.encode('utf-8'))).decode('utf-8')
now_time = int(time.time() * 1000)
data_str1 = '{"rId":100041,"ver":"1.0.6","ts":' + str(now_time) + ',"cts":' + str(now_time + 9) + ',"brVD":[1366,196],"brR":[[1366,768],[1366,728],24,24],"bI":["http://www.dianping.com/shop/' + shop_id + '",null],"mT":[],"kT":[],"aT":[],"tT":[],"aM":"","sign":"' + sign + '"}'
token = base64.b64encode(zlib.compress(data_str1.encode('utf-8')))

print(token.decode())


