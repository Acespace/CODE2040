





def prefix(array, case):
    
    new_array = []
    
    for i in xrange(len(array)):
        
        if array[i][0:3] != '820':
            new_array.append(array[i])
            
    return new_array
