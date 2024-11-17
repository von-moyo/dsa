from typing import List
def shuffle(nums: List[int], n: int) -> List[int]:
    num = len(nums)
    print(num)
    nums1 = [nums[item] for item in range(0, n)]
    nums2 = [nums[item] for item in range(n, num)]
    print(nums1)
    print(nums2)
    array = []
    for i in range(n):
        array.append(nums1[i])
        array.append(nums2[i])
    return array

print(shuffle([1,2,3,4,4,3,2,1], 4))