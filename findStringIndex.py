def strStr(haystack: str, needle: str) -> int:
    index = haystack.find(needle)
    print(index)
    if index != -1:
        return index
    else: 
        return -1
    
print(strStr("leetcode", "cole"))