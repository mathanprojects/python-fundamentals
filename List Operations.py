# List of 10 numbers

numbers = [12, 45, 7, 23, 89, 34, 56, 90, 11, 67]


def find_sum(nums):

    total = 0

    for i in nums:
        total = total + i

    return total


def find_average(nums):

    total = find_sum(nums)

    average = total / len(nums)

    return average


def find_max(nums):

    maximum = nums[0]

    for i in nums:

        if i > maximum:
            maximum = i

    return maximum


def find_min(nums):

    minimum = nums[0]

    for i in nums:

        if i < minimum:
            minimum = i

    return minimum



print("List :", numbers)

print("Sum :", find_sum(numbers))

print("Average :", find_average(numbers))

print("Maximum :", find_max(numbers))

print("Minimum :", find_min(numbers))