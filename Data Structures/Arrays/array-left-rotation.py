#-*- coding : utf-8 -*-

# Challenge : https://www.hackerrank.com/challenges/array-left-rotation

quantity_elements , left_times = list(map(int,input().split(" ")))
elements = list(map(int,input().split()))

for _ in range(left_times):
    removed_element = elements.pop(0)
    elements.append(removed_element)

print(" ".join(map(str,elements)))