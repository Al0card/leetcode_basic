
def twoSum(nums: list[int], target: int) -> list[int]:
    dict = {}
    dup = {}
    a = b = 0
    for pos, val in enumerate(nums):
       
        if val not in dict:
            print('inside twoSum dict:\n')
            dict[val]  = pos
            print(f'{val}: {dict[val]}\n')
        else:
            print('inside twoSum dup:\n')
            dup[val] = pos
            print(f'{val}: {dup[val]}\n')
    for key, val in dict.items():
        if (target - key) in dict and target - key != key:
            a = val
            b = dict[target - key]
        elif target - key == key:
            a = val
            b = dup[key]

    return a,b, dict, dup


def main():
    a, b, dict, dup = twoSum([3, 3], 6)
    print(f'{a} {b} \n')
    print('dict : --------------------\n')
    for key, val in dict.items():
        print(f'{key}: {val}\n')
    print('\n')

    print('dup : --------------------\n')
    for key, val in dup.items():
        print(f'{key}: {val}\n')
    print('\n')


main()