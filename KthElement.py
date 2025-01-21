
def kthElementHelper(Arr1, Arr2, k):

    length1 = len(Arr1)
    length2 = len(Arr2)

    if length1 == 0 and length2 == 0 :
        return -1
    
    if length1 < length2:
        return kthElement(Arr1, Arr2, k)
    
    else:
        return kthElement(Arr2, Arr1, k)
    


def kthElement(Arr1, Arr2, k):

    # Base Case: Array 1 is exhausted
    if(len(Arr1) == 0):
        return Arr2[k]

    # Base Case: Array 2 is exhausted
    if(len(Arr2) == 0):
        return Arr1[k]    
    
    # Finds halfway points between start-k to elimenate indexes

    length1 = len(Arr1)
    length2 = len(Arr2)
    print(length1)
    print(length2)
    print(k//2)
    i = min( length1, k // 2)
    j = min( length2, k // 2)
    


    print("i is: ", i, " and j is: ", j) 
    print("Array1: ", Arr1)
    print("Array2: ", Arr2)
    
    if(Arr1[i-1] < Arr2[j-1]):
        print("Arr1[i] < Arr2[j] \n")
        return kthElement(Arr1[i:], Arr2, k-i)
    else:
        print("Arr2[j] < Arr1[i] \n")
        return kthElement(Arr1, Arr2[j:], k-j)


    
arr1 = [1,2,3,5,6] 
arr2 = [3,4,5,6,7]
k = 5
print(kthElement(arr1, arr2, k))  #4
