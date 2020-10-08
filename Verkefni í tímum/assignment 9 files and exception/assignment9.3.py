num1_str = input('Input first number: ')
num2_str = input('Input second number: ')


def divide_safe(num1_str,num2_str):
    try:
        num1_int = float(num1_str)
        num2_int = float(num2_str)
        divide_nums = num1_int/num2_int
        return round(divide_nums,5)
    except ValueError:
        return None
    except ZeroDivisionError:
        return None


result = divide_safe(num1_str, num2_str)
print(result)

