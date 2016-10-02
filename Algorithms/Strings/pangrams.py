# -*- coding: utf-8 -*-

# Challenge: https://www.hackerrank.com/challenges/pangrams

from string import ascii_lowercase as lower_letters

input_text = str(input()).lower()

def to_string_ordered(string):
    new_string = string.replace(" ","")
    new_string = list(set(new_string))
    new_string.sort()
    
    new_string = "".join(new_string)
    
    return new_string
    
if to_string_ordered(input_text) == lower_letters:
    print("pangram")
else:
    print("not pangram")