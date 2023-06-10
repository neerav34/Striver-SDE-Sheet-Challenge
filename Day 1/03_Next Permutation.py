#.................................Next Permutation......................................
# provide with the just next greater permutation of the given permutation
                   
   
def nextPermutation(permutation, n):
     # size of the array.

    # Step 1: Find the break point:
    ind = -1 # break point
    for i in range(n-2, -1, -1):
        if permutation[i] < permutation[i + 1]:
            # index i is the break point
            ind = i
            break

    # If break point does not exist:
    if ind == -1:
        # reverse the whole array:
        permutation.reverse()
        return permutation

    # Step 2: Find the next greater element
    #         and swap it with arr[ind]:
    for i in range(n - 1, ind, -1):
        if permutation[i] > permutation[ind]:
            permutation[i], permutation[ind] = permutation[ind], permutation[i]
            break

    # Step 3: reverse the right half:
    permutation[ind+1:] = reversed(permutation[ind+1:])

    return permutation
