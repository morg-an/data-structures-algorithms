from pickle import TRUE
from pip import List


nums = [2, 5, 5, 11]
target = 10


def twoSums(nums: List[int], target: int) -> List[int]:
    for num in nums:
        print("loop")
        output = []
        matchNum = target-num
        if num != matchNum:
            if matchNum in nums:
                output.append(nums.index(num))
                output.append(nums.index(matchNum))
                break
        else:
            if nums.count(num) == 2:
                output.append(nums.index(num))
                nums.remove(num)
                output.append(nums.index(matchNum)+1)
                break

    return output


print(twoSums(nums, target))
