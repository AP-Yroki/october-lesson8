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


print(string_sum(4))