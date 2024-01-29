def solution(needle,haystack):
    k = len(needle)
    if len(haystack)<len(needle):
        return -1
    for i in range(len(haystack)-k+1):
        if haystack[i:i+k]==needle:
            return i
    return -1

haystack = "badbutsad"
needle = "sad"

idx = solution(needle,haystack)
print(idx)