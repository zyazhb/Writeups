#!/usr/bin/env python

username = "Hello"
counter = 0;
password = "Happy@"
for i in username:
    password = password + chr((counter + counter * ord(i) * ord(i)) % 0x42 + 33)
    counter = counter + 1
print(password)
