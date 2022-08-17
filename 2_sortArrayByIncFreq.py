# Given an array of integers nums, sort the array in increasing order based on the frequency
# of the values. If multiple values have the same frequency, sort them in decreasing order.

# Return the sorted array.

from multiprocessing.connection import answer_challenge
from operator import indexOf


def sortArray(nums):
    descending = sorted(nums, reverse=True)
    numbers = []
    counts = []
    i = 0
    answer = []

    for num in descending:
        if num not in numbers:
            numbers.append(num)
            counts.append(nums.count(num))

    while i < len(counts):
        index = counts.index(min(counts))
        nextNum = numbers[index]
        nextCount = counts[index]
        j = 0
        while j < nextCount:
            answer.append(nextNum)
            j += 1
        counts.remove(counts[index])
        numbers.remove(numbers[index])
    return answer


sortArray([1, 1, 5, 6, 8, 9, 1, 5, 2])
