import codecs
string = "}rQbpar_gbE{sgpbz"
string = codecs.decode(string,"rot13")
for i in range(len(string)):
    print(string[16-i],end="")
