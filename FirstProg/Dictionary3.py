# Write a Python program to sum all the items in a dictionary.
#20CS056_Sakshi
# Function to print sum
def returnSum(myDict):
  list = []
  for i in myDict:
    list.append(myDict[i])
  final = sum(list)
  return final
# Driver Function
dict = {'a': 100, 'b':200, 'c':300}
print("Sum :", returnSum(dict))
