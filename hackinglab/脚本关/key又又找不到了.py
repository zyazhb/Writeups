import requests
import re
url= "http://lab1.xseclab.com/xss1_30ac8668cd453e7e387c76b132b140bb/index.php"
url= "http://lab1.xseclab.com/xss1_30ac8668cd453e7e387c76b132b140bb/search_key.php"

r =requests.get(url)
r = re.findall("key is :[ a-z_]{0,32}",r.text)
print(str(r)[11:-2])
