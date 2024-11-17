from typing import List
def summaryRange2(nums: List[int]) -> List[str]:
    if not nums:
        return []  # Handling the edge case
    ans = []
    # Initially we will keep the start and end pos and at same
    start = end = str(nums[0])
    for i in range(1, len(nums)):
        print("start:", start)
        print("end:", end)
        print("next element:", nums[i])
        print("prev element + 1:", nums[i-1] + 1)
        print("i:", i)
        if nums[i] != nums[i - 1] + 1:  # Checking if numbers are bounded
            print("if nextElement is not == prevElement, run this loop")
            if start != end:  # If there exist a incrementing part
                ans.append(start+'->'+end)
                print("start - end: ", (start+'->'+end))
            else:
                print("just start:", start)
                ans.append(start)
            start = end = str(nums[i])
        else:
            end = str(nums[i])  # Increasing the size of the existing bounds
            print("else if nextElement is == prevElement, run this loop")
            print("changed value for end to be nums[i]:", end)
    if start == end:  # To handle the remaining elements out of the loop
        ans.append(start)
        print("single value: ", start)
    else:
        ans.append(start+'->'+end)
    return ans


print(summaryRange2([0,2,3,4,6,8,9]))
