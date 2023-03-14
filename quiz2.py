import random

# creates 5 unique elements from 1..50 and adds a + and a [0-19]+1 number
randlist = random.sample(range(1, 51), k=5) + ["+", random.choice(range(20)) + 1]
print(randlist)
nums = list(range(1,51))

random.shuffle(nums)
five_nums = nums[:5]
print(five_nums)

print("You drew {} {} {} {} {} {} {}".format(*randlist))