from random import *
from sort import *
import os

n = 20
nums = []
for i in range(n):
    nums.append(randint(0,100))

print(nums)
print(nums[5:])
print(nums[:5])

print(mergeSort(nums))