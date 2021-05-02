'''
Author: clingxin
Date: 2021-05-02 07:34:16
LastEditors: clingxin
LastEditTime: 2021-05-02 07:34:39
FilePath: /python-web-fastapi-docker/service/try.py
'''
print("subscribe now")

firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")

print("Your full name is ",firstname, lastname)

import matplotlib.pyplot as plt

x = [24,25,26]
y = [23,34,25]

plt.plot(x,y)
plt.show()


import json

items = json.loads('[{"id":1, "text":"Item 1"}, {"id":2, "text": "Item 2"}]')

for item in items:
    print (item['title'])
