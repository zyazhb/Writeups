import base64   
import zxing

f = open('base64.txt','r')
strs = f.read()
f.close()

img = base64.b64decode(strs) 

file = open('base64.png','wb') 
file.write(img)  
file.close()

reader = zxing.BarCodeReader()
barcode = reader.decode("base64.png")
print(barcode.parsed,end="")
