#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:22 2024

@author: rowynnaidoo
"""

"""
Storing data in python:
    1. Lists
    2. Dictionaries
    3. Data Frames - specific to pandas
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)

"""
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
"""

age1 = 30
age2 = 25
age3 = 29

age = [30, 25, 29, 46, 22]    #square brackets is a list, can store any data types

print(age)

"""
[30, 25, 29, 46, 22]
"""

print(age[0])    #print the first value

print(min(age))

print(max(age))

print(sum(age))

print(len(age))    #lenght of list

print(sum(age)/len(age))    #there is no average function in python, calculate it

print(age[0:2])    #prints a range, the first two elements from 0 to n-1

age.append(100)     #add a new element


#How to append the first position in a list

age.insert(0,100) #all other values shift




"""
DICTIONARIES- key: value pairs

cat: "a cute animal"

- unordered

"""

mammals = {"cat":"a cute animal", "lion":"king of the jungle", "elephant":"a gigantic herbivore"}

print(mammals["cat"])


"""
DATA FRAMES 

df = dataframe
"""

fruits = ["apple", "banana", "orange", "grape", "kiwi"]

size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {
    'fruits':fruits,
    'sizes': size_nm
    }

df = pandas.DataFrame(fruit_sizes)

print(df['fruits'])

print(df['sizes'])

print(df['sizes'].min())

print(df['sizes'].mean())

print(df.describe())

print(df[df["sizes"]> 10])   #only those with sizes >10

print(df[1:3])    #print the first two rows

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

df['prices'] = prices

df.drop(columns=["sizes"], inplace = True)     #inplace=True means the data will be modified without returning a copy of the data or the original data



























