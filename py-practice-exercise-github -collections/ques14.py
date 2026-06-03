def extract_digit_from_number(num):

    while num > 0:
        digit = num % 10

        # remove the last digit

        num = num // 10

        print(digit, end=",")


extract_digit_from_number(5678999)