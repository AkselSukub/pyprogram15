#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def list_to_dict_decorator(func):
    def wrapper(*args, **kwargs):
        list1, list2 = func(*args, **kwargs)
        return dict(zip(list1, list2))
    return wrapper

@list_to_dict_decorator
def strings_to_lists(string1, string2):
    list1 = string1.split()
    list2 = string2.split()
    return list1, list2

string1 = input("Введите первый список слов, записанных через пробел: ")
string2 = input("Введите второй список слов, записанных через пробел: ")

result_dict = strings_to_lists(string1, string2)
print(result_dict)