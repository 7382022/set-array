import array as arr

#crate an array
array_num = arr.array('i', [1,3,5,7,9,3])
print("Original array: "+str(array_num))

# count number of occurences
print("Number of occurences of the number 3 in the said array:"+str(array_num.count(3)))

#reverse the array
array_num.reverse() 
print ("the order of the itens:")
print(str(array_num))