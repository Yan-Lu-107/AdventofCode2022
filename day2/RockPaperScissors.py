
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 15:14:59 2022

@author: yanlu
"""

my_file = open('./data.txt', "r")
data = my_file.read()
data_into_list = data.split("\n\n")
print(data_into_list)
sum_data=[]
for i in range(len(data_into_list)):
    data=data_into_list[i].split("\n")
    if ("" in data):
        data.remove("")
    sum_data.append( sum([eval(i) for i in data]))

#part1
print(max(sum_data))
#part2
print(sum(sorted(sum_data, reverse=True)[:3]))