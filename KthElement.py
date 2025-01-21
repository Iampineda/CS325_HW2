def kthElement(Arr1, Arr2, k):

    # Base Case: Array 1 is exhausted
    if(len(Arr1) == 0):
        return Arr2[k-1]

    # Base Case: Array 2 is exhausted
    if(len(Arr2) == 0):
        return Arr1[k-1]    

    # Base Case: End of k
    if k == 1:
        return min(Arr1[0], Arr2[0])
    
    # Finds halfway points between start-k to elimenate indexes
    i = min(len(Arr1), k // 2)
    j = min(len(Arr2), k // 2)


    # Checks logic for recursions 
    if(Arr1[i-1] < Arr2[j-1]):
        return kthElement(Arr1[i:], Arr2, k-i)
    else:
        return kthElement(Arr1, Arr2[j:], k-j)

    
arr1 = [1,2,3,5,6] 
arr2 = [3,4,5,6,7]
k = 5
print(kthElement(arr1, arr2, k) ) #4


