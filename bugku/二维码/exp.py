import zxing

for i in range(0,190):
    reader = zxing.BarCodeReader()
    barcode = reader.decode(str(i)+".png")
    print(barcode.parsed,end="")
