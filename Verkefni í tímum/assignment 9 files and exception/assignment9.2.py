def is_float(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

    


print(is_float('3.45'))
print(is_float('abc'))
