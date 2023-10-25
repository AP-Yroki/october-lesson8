def num(x):
    try:
        x = float(x)
        if x < 0:
            return "yes"
        else:
            return "no"
    except TypeError:
        return "TypeError"
    except ValueError:
        return "ValueError"



def is_even(num):
    try:
        if num % 2 == 0:
            return True
        else:
            return False
    except TypeError:
        return "TypeError"
    except ValueError:
        return "ValueError"


def count_digit(num):
    try:
        num = int(num)
        if num < 0:
            num = -num
        num = str(num)
        return len(num)
    except TypeError:
        return "TypeError"
    except ValueError:
        return "ValueError"

def arr_sum(arr):
    try:
        return sum(arr)
    except TypeError:
        return "TypeError"
    except ValueError:
        return "ValueError"


def string_sum(nums):
    try:
        nums = [int(num) for num in nums]
        return sum(nums)
    except TypeError:
        return "TypeError"
    except ValueError:
        return "ValueError"


def date_convert(date):
    try:
        res = date.split("-")
        res.reverse()
        return tuple(res)
    except AttributeError:
        return 'AttributeError'


def sum_divider(nums):
    try:
        nums = [int(num) for num in nums]
        test1 = len(nums) // 2
        res1 = sum(nums[0:test1])
        res2 = sum(nums[test1:])
        res = res1 / res2
        return res
    except TypeError:
        return "TypeError"
    except ValueError:
        return "ValueError"


def dct_join(dct1, dct2):
    res = dct1 | dct2
    return res


dct = {
    1: {1: 11, 2: 12, 3: 13},
    2: {1: 21, 2: 22, 3: 23},
    3: {1: 24, 2: 25, 3: 26},
}



def dct_sum(dct):
    total_sum = sum(sum(inner_dict.values()) for inner_dict in dct.values())
    return total_sum
