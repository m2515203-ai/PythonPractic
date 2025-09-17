def get_dig_sum(dig):
    sum = 0
    string = str(dig)
    for digit in string:
        sum += int(digit)
    return sum


def input_num_and_print_sum(n):
    num2 = int(input(f"{n}-значное число: "))
    arr = list(str(num2))
    print(f"Сумма {len(arr)}-значного числа: {arr}, Произведение: {get_dig_sum(num2)}")


input_num_and_print_sum(2)
input_num_and_print_sum(3)
