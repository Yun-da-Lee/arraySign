def arraySign_my_code(nums: list[int])-> int:
    ans = 1
    for v in nums:
        if v == 0:
            return 0
        if v < 0:
            ans *= -1
    return ans

def arraySign_best_runtime(data:list)-> bool:
    c_neg = 0
    zeros = 0
    for i in nums:
        if i < 0:
            c_neg += 1
        if i == 0:
            zeros += 1
    if zeros != 0:
        return 0
    if c_neg % 2 == 0:
        return 1
    else:
        return -1


def arraySign_best_memory_saving(data:list)-> bool:
    x = 1
    for i in nums:
        x *= i
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0

if __name__ == "__main__":
    nums = [9,72,34,29,-49,-22,-77,-17,-66,-75,-44,-30,-24]
    #nums = [1, 5, 0, 2, -3]
    #nums = [-1, 1, -1, 1, -1]
    my_result = arraySign_my_code(nums)
    best_runtime = arraySign_best_runtime(nums)
    best_memory_saving = arraySign_best_memory_saving(nums)
    print(my_result)
    print(best_runtime)
    print(best_memory_saving)
