def remove_elements(arr):
    non_rep_idx = 0
    for i in range(1,len(arr)):
        if arr[i-1]!=arr[i]:
            non_rep_idx+=1
            arr[non_rep_idx],arr[i] = arr[i],arr[non_rep_idx]
    return non_rep_idx

arr = [1,2,3,4,4,5,6,7,7]
k = remove_elements(arr)
print(arr[:k])
