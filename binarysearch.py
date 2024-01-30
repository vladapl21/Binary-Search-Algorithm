list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [21, 36, 49, 50, 51, 102, 105, 131, 145]

def binarysearch(list, num):
  arr = list
  while len(arr) > 1:
    if arr[len(arr)//2] == num:
      print(f'Yes, {list.index(num)}')
      break
    elif arr[len(arr)//2] > num:
      arr = arr[0:len(arr)//2]
    else:
      arr = arr[len(arr)//2:len(arr)]
  if len(arr) == 1 and arr[0] != num:
    print('No')
  elif len(arr) == 1 and arr[0] == num:
    print(f'Yes, {list.index(num)}')
  
    

binarysearch(list1, 24) # prints: No
binarysearch(list2, 49) # prints: Yes, 2