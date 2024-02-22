import numpy as np


array = np.random.randint(0, 10000, 100)


print(f'The original array was: {array}')

print(f'Applying the sorting algorithm...')

current = 0
new_array = []

for i in range(len(array)):
    if array[i] >= current:
        print(f'The number {array[i]} is in order, it will be spared.')
        current = array[i]
        new_array.insert(len(new_array), array[i])
    else:
        print(f'Oh no! The number {array[i]} isn\'t in order. It will be executed.')
        
print(f'The resulting array is: {new_array}')
        