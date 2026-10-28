def rearrange_array(numbers):
    result = []
    for index1 in range(len(numbers)):
        column = []
        for index2 in range(len(numbers[index1])):
            column.append(numbers[index1][(len(numbers[index1])) - 1 - index2])
        result.append(column)
    return result    

print (rearrange_array([[1,2,3],[4,5,6],[7,8,9]]))
print (rearrange_array([[8,6],[2,4,5],[3],[1,4,2,8]])) 
  
