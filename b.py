s1 = [4,3,2,7,8,2,3,1] #[5,6]
s2 = [1,1] # [2]

def findDisappearedNumbers(nums):
    nums.sort()
    print(nums)
    print("[", end="")
    for i in range(1, len(nums)+1):

        print(i, end=", ")
    print("]", end="")
    print()


findDisappearedNumbers(s1)
