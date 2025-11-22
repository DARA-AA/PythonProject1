import array

def sum_arrays(arr1,arr2):
    result=array.array('i',[])
    for i in range(len(arr1)):
        result.append(arr1[1]+arr2[1])
    return result

array1=array.array('i',[1,2,3,4,5,])
array2=array.array('i',[6,7,8,9,10])

result=sum_arrays(array1,array2)
print(result)
