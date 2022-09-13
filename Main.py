from typing import List

def insertionSort(array) -> List[int]:
  # Write your code here
  for i in range(1,len(array)):
    min = i
    for j in range(i-1,-1,-1):
      if (array[j] > array[min]):
        array[j],array[min] = array[min],array[j]
        min -=1
  return array

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
