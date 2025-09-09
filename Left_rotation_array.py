def leftrotate(array,d):
     d = d % len(array)
     return array[-d:]+array[:-d]
array=input("enter the array elements ")
array=list(map(int,array.split()))
d=int(input("Enter the position "))
result = leftrotate(array,d)
print(result)